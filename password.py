import smtplib
def nitish_email(email,password,message):
      srv = smtplib.SMTP('smtp.gmail.com', 587)
      srv.starttls()
      srv.login(email,password)
      srv.sendmail(email,email,message)
      srv.quit()
nitish_email("hacktheworld378@gmail.com","7004969879nitish","hello nitish")
