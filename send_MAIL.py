import smtplib, genkey
from os.path import basename
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email.mime.application import MIMEApplication

def send_mail(sender,password,recpnt,subject,body,img,files):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
 
    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=recpnt
    msg['Subject']=subject
    genkey.encryptIT(body,img)
    msg.attach(MIMEText(genkey.encrypted,'plain'))

    fp = open('output.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-Disposition', 'inline', filename='output.png')
    msg.attach(msgImage)
    
    for f in files:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(),Name=basename(f))
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    server.sendmail(sender, recpnt, msg.as_string())
    server.quit()
