import mail_class
#! coding:utf-8
from conf.config import contacts
"""
a=mail(mail_to="xxx@qq.com",mail_from="xxx@qq.com",
       mail_from_name="测试",mail_subject="test mess age ",message="aaaaajsljflasfldsa")
a.create_mail()
a.smtp()
"""

def sendmail(data,mail_subject = "报警"):
    mail_from = contacts['smtp_user']
    mail_from_name=contacts['smtp_show_name']
    mail_to = contacts['to_mail']
    smtp_server = contacts["smtp_server"]
    smtp_user = contacts['smtp_user']
    smtp_pass = contacts['smtp_pass']
    
    for x in mail_to.split(','):
        mail = mail_class.mail(mail_to=x.strip(),mail_from=mail_from,mail_from_name=mail_from_name,mail_subject=mail_subject
                           ,message=data)
        mail.create_mail()
        mail.smtp(smtp_server, smtp_user, smtp_pass)
    


