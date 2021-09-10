import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
FROM_EMAIL = os.getenv('FROM_EMAIL')
FROM_EMAIL_PSWD = os.getev('FROM_EMAIL_PSWD')
TO_EMAIL = os.getenv('TO_EMAIL')

# this method uses a gmail that does not have duel authentication and has the 'Access for less secure apps setting' turned on
def send_mail(message: str) -> None:
    '''
    Sends an email with the desired message argument using the fields determined by the user in the .env file
    :param message: What the email body should contain
    :return: None
    '''

    msg = EmailMessage()
    msg.set_content(message)
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = "Python email!"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(FROM_EMAIL, FROM_EMAIL_PSWD)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()
        print("success")

    except Exception as e:
        print(e)
        print("fail")


if __name__=="__main__":
    send_mail('blah blah test')