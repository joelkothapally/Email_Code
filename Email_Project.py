import smtplib

from email.message import EmailMessage

email = EmailMessage()

#from name
email['from'] = 'xxxxxx'
#email ID that you want to send
email['to'] = 'xxxxx'
email['subject'] = 'You won 1,000,000 dollars!'


email.set_content('I am a Datascience master and developer!')

# host port changes with the client - gmail,outlook,yahoo
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
#enter your email ID and password
	smtp.login('xxxxxx', 'xxxx')
	smtp.send_message(email)
	print('all good boss!')
