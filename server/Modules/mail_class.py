#! /usr/bin/env python
#! coding:utf8

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Utils,Encoders
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication 
import mimetypes,sys,os
import smtplib,log

"""
用于发送邮件class
a=mail(mail_to="xxx@qq.com",mail_from="xxx@qq.com",
       mail_from_name="测试",mail_subject="test mess age ",message="aaaaajsljflasfldsa")
a.create_mail()
a.smtp()
    
"""

class  mail(object):
    def __init__(self,mail_to,mail_from,mail_from_name,mail_subject,message):
        self.mail_to= mail_to 
        self.mail_from= mail_from
        self.mail_from_name= mail_from_name
        self.mail_subject= mail_subject
        self.message= message
        self.contenttype = "text/html"
    def getpart(self,data,contenttype):
        maintype,subtype = contenttype.split('/')
        if maintype == 'text':
            retval = MIMEText(data,_subtype=subtype)
        else:
            retval = MIMEBase(maintype,subtype)
            retval.set_payload(data)
            Encoders.encode_base64(retval)
        return retval
    def attachment(self,filename):
        if not os.path.exists(filename):
                return None
        fd = open(filename)
        mimetype,mimeencoding = mimetypes.guess_type(filename)
        if mimeencoding or (mimetype is None):
            mimetype = 'application/octet-stream'
        retval = self.getpart(fd.read(),mimetype)
        retval.add_header('Content-disposition','attachment',
                      filename=filename)
        fd.close()
        return retval
        
    def create_mail(self):
        msg = MIMEMultipart()
        msg['To'] = self.mail_to
        msg['From'] = "<%s>%s" % (Header(self.mail_from_name,"UTF-8"),self.mail_from)
        msg['Subject'] = Header(self.mail_subject,"UTF-8")
        msg['Date'] = Utils.formatdate(localtime=1)
        msg['Message-ID'] = Utils.make_msgid()
        body = MIMEMultipart('alternative')
        body.attach(self.getpart(self.message,self.contenttype))
        msg.attach(body)
        self.msg = msg.as_string()

        
    def smtp(self,smtp_server,smtp_user,smtp_pass):
        s = smtplib.SMTP()
        if s:
            try:
                s.connect(smtp_server, 25) 
                s.login(smtp_user,smtp_pass)
                s.sendmail(self.mail_from,self.mail_to,self.msg)
                s.close()
            except Exception,e:
                log.log(e)

    