import smtplib
content = 'hatt1992@gmail.com'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('hatt1992@gmail.com','thuha1992')
mail.sendmail('hatt1992@gmail.com','hatt1992@gmail.com','hi there')
mail.close()
