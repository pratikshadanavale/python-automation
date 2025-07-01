
import smtplib
from email.message import EmailMessage
import os
import logging

logging.basicConfig(filename='email_log.log', level=logging.INFO)

def send_email():
    try:
        msg = EmailMessage()
        msg['subject'] = 'filtered employee report'
        msg['From'] = 'pratikshadanavale@gmail.com'
        msg['To'] = 'prsdshingne1@gmail.com'
        msg.set_content('Attached is the filtered excel report.')
        file_path = "C:\\JenkinsScripts\\filtered_employees.xlsx"
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)

        msg.add_attachment(file_data, maintype = 'application', subtype = 'vnd.openxmlformats-officedocument.spreadsheetml.sheet',filename=file_name)

#Email server setup
        with smtplib.SMTP('smtp.gmail.com',587) as server:
            server.starttls()
            server.login('pratikshadanavale@gmail.com' ,"vdjgwohbswnveqfn")
            server.send_message(msg)

        print("Email sent successfully")
        logging.info("Email sent successfully")

    except Exception as e:
        print(f"Error : {e}")
        logging.error(f"Error sending email:{e}")

send_email()