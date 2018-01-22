""" "Soffiamo" un palloncinocon pygame. """

# Importiamo la libreria pygame.
import pygame
# Questa e' la libreria con le impostazioni di tempo.
import time

# Impostiamo un foglio bianco.
pygame.init ()

# Prepariamo il foglio impostandone le dimensioni.
areapalloncino = pygame.display.set_mode ((400, 500))

# Dichiarazione variabili.
i = 0

while i < 600:
      # Disegniamo un cerchio, il primo parametro conterra' il colore,
      # il secondo le coordinate ,come terzo il raggio e quarto lo spessore
      # della linea.
      pygame.draw.circle (areapalloncino, (255, 0, 0), (300, 350), 30)

      # Serve a disegnare un segmento,partiamo dai parametri tra parentesi il
      # primo ci indica il colore,
      # il secondo sono le coordinate del primo estremo e il terzo le coordinate
      # del secondo.
      pygame.draw.line (areapalloncino,(255, 255, 0), (300, 380), (300, 580))

      # Ordiniamo di aggiornare il disegno
      pygame.display.update ()

      # Il programma "dorme" per un certo periodo  espresso in secondi per poi
      # riprendere.
      time.sleep (0.03)

      # Impostiamo uno sfondo modificabile tramite i  parametri.
      areapalloncino.fill ((255, 205, 255))
      i = i + 1
