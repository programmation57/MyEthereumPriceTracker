import requests
from bs4 import BeautifulSoup
import smtplib, ssl

url = 'https://coinmarketcap.com/fr/currencies/ethereum/'
headers = {'User-Agent' : 'Votre User Agent}

page = requests.get(url, headers=headers)


bs = BeautifulSoup(page.content, 'html.parser')


price = bs.find(class_ = "priceValue___11gHJ").get_text()[:6]
print(price)

reduction = bs.find(class_ = "sc-15yy2pl-0 feeyND").get_text()[:5]
print("Le prix a réduit de -" + reduction)

if(price > str(2700)):
	smtp_address = 'smtp.gmail.com'
	smtp_port = 465

	# on rentre les informations sur notre adresse e-mail
	email_address = 'email_address@gmail.com'
	email_password = 'email_password'

	# on rentre les informations sur le destinataire
	email_receiver = 'email_receiver@gmail.com'

	email_subject = 'MyEthereumPriceTracker'

	# on crée la connexion
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
	  # connexion au compte
	  server.login(email_address, email_password)
	  # envoi du mail
	  server.sendmail(email_address, email_receiver, 'Le prix de l\'ethereum est a plus de 2700 euro \n \nLIEN : https://coinmarketcap.com/fr/currencies/ethereum/')
	  print("sendmail 💲💲💰")
