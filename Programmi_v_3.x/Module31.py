#!/usr/bin/env python

# Chiediamo quante sono le femmine e quanti maschi.
femmine = int (input ("Quante femmine ci sono ")) 
maschi = int (input ("Quanti maschi ci sono "))

# Facciamo la somma di maschi e femmine per sapere il numero di alunni totali.
alunni = (femmine + maschi)

# Facciamo una selezione se il denominatore e' uguale a 0.
if alunni == 0: 
    # Se alunni e' uguale a zero non si puo' effettuare la divisione.
    print ("Impossibile fare la media della classe ") 

else: 
    # Gli facciamo inserire la media delle altezze delle femmine e dei maschi.
    altezza_media_femmine = float (input ("Inserisci la media delle altezze delle femmine ")) 
    altezza_media_maschi = float (input ("Inserisci la media delle altezze dei maschi "))

    # Facciamo l'operazione con i dati inseriti.
    altezza_media_classe = ((altezza_media_femmine*femmine)+(altezza_media_maschi*maschi)) / alunni 
    
    # Facciamo visualizzare il risultato finale
    print (altezza_media_classe) 
    



