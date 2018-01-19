#!/usr/bin/env python

import pygame #Importiamo la libreria pygame.
import time #Questa e' la libreria con le impostazioni di tempo.
pygame.init () #Diciamo che vogliamo avere il foglio bianco.
areapalloncino = pygame.display.set_mode ((400,500)) #Prepariamo il foglio da disegno.
i = 0 #Variabile contatore.
while i < 600:
      pygame.draw.circle (areapalloncino, (255,0,0), (300,350), 30) #Disegniamo un cerchio e il primo parametro conterra' il colore, il secondo le coordinate ,come terzo il raggio e quarto lo spessore della linea.
      pygame.draw.line(areapalloncino,(255,255,0),(300,380),(300, 580)) #Serve a disegnare un segmento,partiamo sempre dai parametri tra parentesi il primo ci indica il colore, il secondo sono le coordinate del primo estremo e il terzo le coordinate del secondo.
      pygame.display.update () #Ordiniamo di aggiornare il disegno
      time.sleep (0.03) #Il programma "dorme" per un certo periodo  espresso in secondi per poi riprendere.
      areapalloncino.fill ((255,205,255)) #Impostiamo uno sfondo modificabile tramite i  parametri.
      i = i + 1 #Incremetiamo la varibile contatore.

