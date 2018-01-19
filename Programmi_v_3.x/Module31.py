#!/usr/bin/env python
femmine=int(input("Quante femmine ci sono ")) #Chiediamo quante sono le femmine
maschi=int(input("Quanti maschi ci sono ")) #Chiediamo quanti sono i maschi.
alunni=(femmine+maschi) #Facciamo la somma di maschi e femmine per sapere il numero di alunni totali.
if alunni == 0: #Facciamo una selezione se il denominatore e' uguale a 0.
    print("Impossibile fare la media della classe ") #Se alunni e' uguale a zero non si puo' effettuare la divisione.
else: #Altrimenti
    altezza_media_femmine=float(input("Inserisci la media delle altezze delle femmine ")) #Gli facciamo inserire la media delle altezze delle femmine.
    altezza_media_maschi=float(input("Inserisci la media delle altezze dei maschi ")) #Gli facciamo inserire la media delle altezze dei maschi.
    altezza_media_classe =((altezza_media_femmine*femmine)+(altezza_media_maschi*maschi))/alunni #Facciamo l'operazione con i dati inseriti.
    print (altezza_media_classe) #Facciamo visualizzare il risultato finale
    



