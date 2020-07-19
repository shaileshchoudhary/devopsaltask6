import smtplib
sender_email = "shaileshchoudhary1999@gmail.com"
receiver_email = "shaileshchoudhary1999@gmail.com"
password = "19101996"
message = "Your code is not working properly"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print('Login Successfullt')
server.sendmail(sender_email,receiver_email,message)
print("Email has been sent to", receiver_email)
server.quit()
