import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("adamhallab", "damzeezationCR7!")
server.sendmail(
    "adamhallab@gmail.com",
    "adamhallab@gmail.com",
    "\nAssistance needed at recognition entrance")
server.quit()