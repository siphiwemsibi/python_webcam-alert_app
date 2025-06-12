import os
import smtplib
import imghdr
from email.message import EmailMessage

PASS = os.getenv("PASS")
SENDER = os.getenv("GMAIL")
RECIEVER = os.getenv("GMAIL")

def send_email(image_path):
    print("Sending email...")
    msg = EmailMessage()
    msg['Subject'] = 'Motion Detected'
    msg.set_content('Motion has been detected in your surveillance area. Please find the attached image.')

    with open(image_path, 'rb') as img:
        img_data = img.read()
    msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASS)
    gmail.sendmail(SENDER, RECIEVER, msg.as_string())
    gmail.quit()
    print("Email sent successfully.")
    

    if __name__ == "__main__":
        send_email(image_path='images/sqlmi.png')  # Replace with a valid image path for testing