import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Piotr Zel'
email['to'] = '<receiver email>'
email['subject'] = 'Odbierz nagrodę!!!'

email.set_content(html.substitute({'name': 'Piotr'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587)as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('<your email>', '<password>')
	smtp.send_message(email)
	print('Wyszło!!!')