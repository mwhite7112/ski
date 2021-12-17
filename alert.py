import smtplib
from email.message import EmailMessage

def sendMessage(subject: str, body: str, to: str) -> None:
    #init message and setting fields
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    #email account to link 

    user = "skialertsystem@gmail.com" #must enable 2fa
    msg['from'] = user
    password = "umjgwcinbvoqsghr"

    #server init
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    

if __name__ == '__main__':
    sendMessage('test', 'this script works. yay!', 'mwhite7112@gmail.com')