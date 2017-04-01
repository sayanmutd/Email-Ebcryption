
# Import the modules required for the tool

import sys,smtplib,time,decpr
import genkey,thread, send_MAIL
from PyQt4 import QtGui
from PyQt4 import QtCore
from os.path import basename

# creating global variables for the tool
  
email=""
paswrd=""
recipient=""
subJect=""
boDy=""
recip=[]
flag=0
success=False
mail=""
pressed=False
MAIL_SENT=False

###############################################################################################################################################

def init_log_in_page_UI():

      global email
      global paswrd
      global mail

      app = QtGui.QApplication(sys.argv) 
      log_in_page = QtGui.QDialog()
      log_in_page.setWindowTitle("NcrypT")
      icon=QtGui.QIcon('Logo.png')
      log_in_page.setWindowIcon(icon)


      grid = QtGui.QGridLayout()
      grid.setSpacing(10)
   
      email = QtGui.QLabel("Email")
      password = QtGui.QLabel("Password")

      grid.addWidget(email, 1, 0)
      grid.addWidget(password, 2, 0)

      emailEdit = QtGui.QLineEdit()
      passwordEdit = QtGui.QLineEdit()
      passwordEdit.setEchoMode(QtGui.QLineEdit.Password)

      grid.addWidget(emailEdit, 1, 1)
      grid.addWidget(passwordEdit, 2, 1)
   
      def log_In():

         try:

            global email
            global paswrd
            global success
            global mail

            log_in.setEnabled(False)
   
            email=emailEdit.text()
            paswrd=passwordEdit.text()
            
            mail=smtplib.SMTP('smtp.gmail.com',25)
            mail.ehlo()
            mail.starttls()
            mail.login(str(email),str(paswrd))
            success=True
            log_in_page.accept()
            
         
         except:

      
            msg_box=QtGui.QDialog()
            msg_box.setWindowTitle("NcrypT")
            icon=QtGui.QIcon('Logo.png')
            msg_box.setWindowIcon(icon)

            grid = QtGui.QGridLayout()
            grid.setSpacing(10)
        
            info = QtGui.QLabel("Log In Unsuccessful..")
            grid.addWidget(info, 1, 0)

            def tryagain():
               msg_box.setVisible (False)
               app.closeAllWindows()
               init_log_in_page_UI()

            try_again = QtGui.QPushButton("TRY AGAIN")
            try_again.setFixedSize(100,24)
            try_again.clicked.connect(tryagain)
            grid.addWidget(try_again,2,0)

            msg_box.setLayout(grid)
            msg_box.setFixedSize(175,100)
            msg_box.exec_()


      log_in=QtGui.QPushButton("Log In")
      log_in.setFixedSize(100,24)
      log_in.clicked.connect(log_In)
      grid.addWidget(log_in,3,1)
      
      see=QtGui.QPushButton()
      see.setFixedSize(24,21)
      icon=QtGui.QIcon('search.png')
      see.setIcon(icon)
      #see.setStyleSheet("background-color: lightgreen")
      
      def SeeOrNotP():
            global pressed
            if passwordEdit.text()=="":
                  return
            pressed=True
            passwordEdit.setEchoMode(QtGui.QLineEdit.Normal)
            passwordEdit.setText(passwordEdit.text())
            #see.setStyleSheet("background-color: red")
      
      def SeeOrNotR():
            global pressed
            if passwordEdit.text()=="":
                  return
            pressed=False
            passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
            passwordEdit.setText(passwordEdit.text())
            #see.setStyleSheet("background-color: lightgreen")
                  
      see.pressed.connect(SeeOrNotP)
      see.released.connect(SeeOrNotR) 
      grid.addWidget(see,2,2)

      log_in_page.setLayout(grid)
      log_in_page.setFixedSize(450, 100)
      log_in_page.exec_()
   
      email=emailEdit.text()
      paswrd=passwordEdit.text()

      if(email=="" or paswrd==""):
         sys.exit()
         
#######################################################################################################################################      

def tab_Interface():

        app = QtGui.QApplication(sys.argv)
        tabs= QtGui.QTabWidget()
          
        send_mail= QtGui.QWidget()  
        decrypt_mail= QtGui.QWidget()

        def init_Send_Mail_UI(send_mail):
            
                receiver_email = QtGui.QLabel("Recipient")
                bcc=QtGui.QLabel("BCC (separate by ';')")
                sub=QtGui.QLabel("Subject")
                message = QtGui.QLabel("Message")

                receiver_emailEdit = QtGui.QLineEdit()
                bccEdit=QtGui.QLineEdit()
                subEdit=QtGui.QLineEdit()
                messageEdit = QtGui.QTextEdit()
                file_browserEdit=QtGui.QLineEdit()
                img_browserEdit=QtGui.QLineEdit()

                grid = QtGui.QGridLayout()
                grid.setSpacing(10)    

                grid.addWidget(receiver_email, 4, 0)
                grid.addWidget(receiver_emailEdit, 4, 1)        

                grid.addWidget(bcc, 5, 0)
                grid.addWidget(bccEdit, 5, 1)

                grid.addWidget(sub, 6, 0)
                grid.addWidget(subEdit, 6, 1)
        
                grid.addWidget(message, 7, 0)
                grid.addWidget(messageEdit, 7, 1, 1, 1)
        
                def selectFile():
                        path=QtGui.QFileDialog.getOpenFileName()
                        if path=='':
                                file_browserEdit.setText("")
                        elif file_browserEdit.text()=='':
                                file_browserEdit.setText(path)
                        else:
                                file_browserEdit.setText(((file_browserEdit.text()).append(";")).append(path))
        
                def selectImage():
                        img_browserEdit.setText(QtGui.QFileDialog.getOpenFileName())
                        
                img_browser = QtGui.QPushButton("Image")
                img_browser.setFixedSize(100,24)
                img_browser.clicked.connect(selectImage)

                grid.addWidget(img_browser,8,0)
                grid.addWidget(img_browserEdit, 8, 1)

                file_browser = QtGui.QPushButton("Add File")
                file_browser.setFixedSize(100,24)
                file_browser.clicked.connect(selectFile)

                grid.addWidget(file_browser,9,0)
                grid.addWidget(file_browserEdit, 9, 1) 

                def showDiag():
                      
                        mail_sent_diaglog_box=QtGui.QDialog()
                        mail_sent_diaglog_box.setWindowTitle("NcrypT")
                        icon=QtGui.QIcon('Logo.png')
                        mail_sent_diaglog_box.setWindowIcon(icon)

                        grid = QtGui.QGridLayout()
                        grid.setSpacing(10)
        
                        info = QtGui.QLabel("Send Mail?")
                        grid.addWidget(info, 1, 0)

                        def send_mail():

                              global recipient
                              global subJect
                              global boDy
                              global mail
                              global MAIL_SENT
                                
                              recipient=receiver_emailEdit.text()
                              subJect=subEdit.text()
                              boDy=messageEdit.toPlainText()
                                
                              def SeNd():
                                  mail_sent_diaglog_box.accept()
                                  global email
                                  global paswrd
                                  global recipient
                                  global subJect
                                  global boDy
                                  global recip
                                  global flag
                                  global MAIL_SENT
                                
                                  mail_sending_diaglog_box=QtGui.QDialog()
                                  mail_sending_diaglog_box.setWindowTitle("NcrypT")
                                  icon=QtGui.QIcon('Logo.png')
                                  mail_sending_diaglog_box.setWindowIcon(icon)
                                
                                  grid = QtGui.QGridLayout()
                                  grid.setSpacing(10)
                                  
                                  info = QtGui.QLabel("Sending Mail..", mail_sending_diaglog_box)

                                  mail_sending_diaglog_box.setFixedSize(175,100)
                                  mail_sending_diaglog_box.show()
                                  
                                  if str(bccEdit.text())=="":
                                      recipient=str(receiver_emailEdit.text())
                                  else:
                                      recipient=str(str(receiver_emailEdit.text())+";"+str(bccEdit.text()))

                                  subJect=subEdit.text()
                                  boDy=messageEdit.toPlainText()

                                  rpt=str(recipient)
                                  recip=str(rpt).split(";")
                                  if str(file_browserEdit.text())=='':
                                        files=[]
                                  else:
                                        files=(str(file_browserEdit.text())).split(";")
                                  for r in recip:
                                      send_MAIL.send_mail(str(email),paswrd,str(r),str(subJect),str(boDy),str(img_browserEdit.text()),files)
                                      
                                      MAIL_SENT=True
                                  
                              SeNd()
                              while not MAIL_SENT:
                                    pass
                              
                              sys.exit()
                                

                        yes = QtGui.QPushButton("Yes")
                        yes.setFixedSize(75,24)
                        yes.clicked.connect(send_mail)
                        grid.addWidget(yes,2,0)
                        
                        no = QtGui.QPushButton("No")
                        no.setFixedSize(75,24)
                        no.clicked.connect(mail_sent_diaglog_box.accept)
                        grid.addWidget(no,2,1)
        
                        mail_sent_diaglog_box.setLayout(grid)
                        mail_sent_diaglog_box.setFixedSize(175,100)
                        mail_sent_diaglog_box.show()

                send = QtGui.QPushButton("Send")
                send.setFixedSize(100,24)
                send.clicked.connect(showDiag)
                grid.addWidget(send,10,0)
        
                send_mail.setLayout(grid)

        def init_Decrypt_Mail_UI(decrypt_mail):
        
                encrypted_message = QtGui.QLabel("Encrypted Message")
                decrypted_message = QtGui.QLabel("Decrypted Message")

                encrypted_messageEdit = QtGui.QTextEdit()
                decrypted_messageEdit = QtGui.QTextEdit()
                img_browserEdit=QtGui.QLineEdit()

                grid = QtGui.QGridLayout()
                grid.setSpacing(10)
                
                def selectImage():
                        img_browserEdit.setText(QtGui.QFileDialog.getOpenFileName())
                        

                img_browser = QtGui.QPushButton("Image")
                img_browser.setFixedSize(100,24)
                img_browser.clicked.connect(selectImage)

                grid.addWidget(img_browser,2,0)
                grid.addWidget(img_browserEdit, 2, 1) 

                def decRypt():
                        d=decpr.decrypted_message(str(img_browserEdit.text()),str(encrypted_messageEdit.toPlainText()))
                        decrypted_messageEdit.setPlainText(str(d))
                        

                decrypt = QtGui.QPushButton("Decrypt Message")
                decrypt.clicked.connect(decRypt)
                
                grid.addWidget(decrypt,8,0)
                grid.addWidget(encrypted_message, 1, 0)
                grid.addWidget(encrypted_messageEdit, 1, 1)
        
                grid.addWidget(decrypted_message, 3, 0)
                grid.addWidget(decrypted_messageEdit, 3, 1)

                decrypt_mail.setLayout(grid)
               
                      
    
        init_Send_Mail_UI(send_mail)
        init_Decrypt_Mail_UI(decrypt_mail)

        tabs.setFixedSize(690, 536)
    
        tabs.addTab(send_mail,"Send Mail")
        tabs.addTab(decrypt_mail,"Decrypt Mail")
        tabs.setWindowTitle("NcrypT")
        tabs.show()
        icon=QtGui.QIcon('Logo.png')
        tabs.setWindowIcon(icon)        
    
        app.exec_()

##############################################################################################################################

init_log_in_page_UI() # Generatting the User Interface for Login page

if success==False:
      sys.exit()

tab_Interface() # Generating the User Interface after the Login page

mail.close()


