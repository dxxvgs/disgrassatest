# -*- coding: utf-8 -*-
import random, os, sys
import tweepy

text_file = open("palavras.txt", "r")       #Abrimos a lista de palavras
palavras = text_file.readlines()        #E convertemos numa lista

consumer_secret = "EX2zfdfSHSzRKvaQLwJ4z3a3G"
consumer_key = "ureW6vCEDZ0C2oEToE32uZblfnuzNsMfhSiKcTUMLxUIF4CYCZ"           #Credencias do twitter dev
access_token = "1231182976681156608-aNU3Deag8Cpcjh32Z1Jw1WdYg1AGlm"
access_token_secret = "O6i6LBUZ5MeZsPkGMyHTWjsQYCGnl4D4fhxZgrSwlv258"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 

numero = int(palavras[0])  #A palavra atual esta salvo no indice 0 da lista

texto = ""

if str(palavras[numero])[0] == '0':
    texto = "disgrassa de "+palavras[numero][1].lower()+"... Melhor não deixa quieto"
    #Algumas palavras não podem ser chingadas, marcamos elas com um 0
    #O bot so vai postar a primeira letra delas
    
else:
    texto = "disgrassa de " + palavras[numero].lower() 
    #Caso não seja uma palavra marcada o bot manda ela se foder msm

    
api.update_status(status=texto) #Então postamos no twitter o texto gerado

palavras[0] = str(numero + 1) + '\n'     #Incrementos o contador

with open('palavras.txt', 'w') as file:
    file.writelines(palavras)       #E salvamos devolta no arquivo
