# pi-temp

A simple script to monitor CPU temperature on a Raspberry PI and send out an email.
 
### Setup a Gmail account
To set up a Gmail address for testing your code, do the following:

* Create a new Google account.
* Turn [Allow less secure apps](https://myaccount.google.com/lesssecureapps) to ON. Be aware that this makes it easier for others to gain access to your account.

### Update settings
Copy the supplied ```settings.ini.sample``` file to ```settings.ini``` and update the values inside the file with you values.

```
[Settings]
smtp_server = smtp.gmail.com
port = 587
sender_email = my_send_email@gmail.com
sender_password = my_send_email_password
receiver_email = recipient_email@gmail.com
```

### Add it as a cron job to run every 30 minutes
Use ```crontab -e``` command to add the following line. Please update the path if it is different:

```30 * * * * python3 /home/pi/pi-temp/pi-temp.py```

