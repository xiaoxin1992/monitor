#! /usr/bin/env python
#! coding:utf8

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Utils,Encoders
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication 
import mimetypes,sys
import smtplib