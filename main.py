import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'ghiyaathwilliams2@gmail.com'
receiver_email_id = 'thapelo@lifechoices.co.za, aneeqahjones@2gmail.com'
password = input("Enter your password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = "Hello there im Ghiyaath \n"
body = body + "Hope to see you soon"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()
