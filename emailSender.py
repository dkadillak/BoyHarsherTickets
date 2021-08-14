
import smtplib
from email.message import EmailMessage

# this method uses a gmail that does not have duel authentication and has the 'Access for less secure apps setting' turned on
def send_mail(message):
    pswd = ''
    fromemail = ''
    toemail = ''

    msg = EmailMessage()
    msg.set_content(message)
    msg["From"] = fromemail
    msg["To"] = toemail
    msg["Subject"] = "Python email!"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #server.starttls()
        server.login(fromemail, pswd)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()
        print("success")
    except Exception as e:
        print(e)
        print("fail")





if __name__=="__main__":
    send_mail()