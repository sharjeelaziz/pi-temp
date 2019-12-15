# coding=utf-8
import os
import smtplib
import ssl
from email.mime.text import MIMEText
import config as c

critical = False
high = 60
too_high = 80


def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


cpu_temp = float(get_cpu_temperature())

if cpu_temp > high:
    if cpu_temp > too_high:
        critical = True
        subject = "Critical warning! The temperature is: {} shutting down!!".format(cpu_temp)
        body = "Critical warning! The actual temperature is: {} \n\n Shutting down the pi!".format(cpu_temp)
    else:
        subject = "Warning! The temperature is: {} ".format(cpu_temp)
        body = "Warning! The actual temperature is: {} ".format(cpu_temp)

    smtp_server = c.get_setting(c.SECTION_SETTINGS, c.SMTP_SERVER)
    port = c.get_setting(c.SECTION_SETTINGS, c.PORT)
    sender_email = c.get_setting(c.SECTION_SETTINGS, c.SENDER_EMAIL)
    password = c.get_setting(c.SECTION_SETTINGS, c.SENDER_PASSWORD)
    receiver_email = c.get_setting(c.SECTION_SETTINGS, c.RECEIVER_EMAIL)

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()

    if critical:
        os.popen('sudo halt')

