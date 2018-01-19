#!/usr/bin/env python


def interrogazione (domanda,risposta_esatta): #Andiamo a definire la funzione che sara' ripresa dal programma quando serve.
	risposta_allievo = input (domanda) #Andiamo a scrivere la prima domanda.
	if risposta_esatta == risposta_allievo: #Se la risposta data e' uguale a quella esatta.
	  print ("La risposta e' esatta") #Gli diciamo che e' giusto.
	  print ("Bravissimo") #E perche' no dei complimenti.
	else: #Altrimenti.
	  print ("Risposta errata") #Gli diciamo che e' sbagliata.
	  print ("La risposta esatta e' ", risposta_esatta,".") #Facciamo vedere la risposta corretta.
	  print (" Studia di piu'!") #Gli diamo un piccolo consiglio.
domanda1 = "In che anno e' caduto l'impero romano d'occidente? " #Questa variabile contiene la prima domanda.
risposta_esatta1 = "476" #Questa  e' la risposta alla prima domanda.
interrogazione (domanda1, risposta_esatta1) #Richiamiamo la funzione interrogazione.
domanda2 = "Chi e' stato il primo presidente degli Stati Uniti? " #Questa variabile contiene la seconda domanda.
risposta_esatta2 = "Washington" #Questa e' la risposta alla seconda domanda.
interrogazione (domanda2, risposta_esatta2) #Richiamiamo nuovamente la funzione interrogazione.
domanda3 = "In che anno e' terminata la prima guerra mondiale? " #Questa variabile contiene la terza domanda.
risposta_esatta3 = "1918" #Questa e' la risposta alla terza domanda.
interrogazione (domanda3, risposta_esatta3) #Richiamiamo di nuovo la funzione.

