# cotacao do dolar for menor do que 5.40

import requests

# pegar a informação você quer
requisao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisao_dicionario = requisao.json()
cotacao = float(requisao_dicionario['USDBRL']['bid'])
print(cotacao)

# enviar um aviso - email
import smtplib
import email.message

def enviar_email(cotacao):
    corpo_email = f"""
    <p>Dólar está abaixo de R$5.40. Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar está hoje abaixo de R$5.20"
    msg['From'] = 'daniellemdemoura@gmail.com'
    msg['To'] = 'daniellemdemoura@gmail.com'
    password = 'korrpbpbvsdkkqfo'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.40:
    enviar_email(cotacao)