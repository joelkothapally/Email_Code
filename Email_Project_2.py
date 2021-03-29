import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #you can also use os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
# from name
email['from'] = 'xxxxxyyyyy'
#email ID that you want to send
email['to'] = 'email ID that you want to send'
email['subject'] = 'You are my sweet Beautiful Friend!'


email.set_content(html.substitute({'name' : 'xx'}), 'html')

# host port changes with the client - gmail,outlook,yahoo
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	#enter your email ID and password
	smtp.login('your email id', 'password')
	smtp.send_message(email)
	print('all good boss!')
