import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("Enter email address here", "Enter email password here")
server.sendmail(
    "From email",
    "To email",
    "\nAssistance needed at recognition entrance")
server.quit()
