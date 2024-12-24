#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#import getpass

class EmailSender:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, sender, receiver, subject, body):
        """
        发送邮件

        """
        # 创建 MIMEText 对象
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = sender
        message['To'] = ','.join(receiver)
        message['Subject'] = subject

        try:
            smtpobj = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtpobj.starttls()
            smtpobj.login(self.smtp_user, self.smtp_password)
            smtpobj.sendmail(sender, receiver, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件", e)

if __name__ == "__main__":
    smtp_server = 'mail.example.com'
    smtp_port = 587
    smtp_user = 'user@example.com'
    smtp_password = 'password'
    # 创建EmailSender实例
    email_sender = EmailSender(smtp_server, smtp_port, smtp_user, smtp_password)

    sender = 'sender@example.com'
    receiver = ['user01@example.com', 'user02@example.com']
    subject = 'TEST Email with attachment'
    body = 'This is  a test email.'

    # 发送邮件
    email_sender.send_email(sender, receiver, subject, body)
  
