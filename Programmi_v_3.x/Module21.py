#!/usr/bin/env python

py = "Python" #Dentro la variabile py ci mettiamo la nostra stringa.
i=0 #Variabile contatore inizializzata.
while i < 6: #Condizione del ciclo dove i  minore di 6.
   print (py[i],'\t', py [0:i+1],'\t', py[i]+py[i-1]+py[i-2])#Nella prima parte stampiamo lettera per lettera la parola python grazie al contatore i che si incrementa.
                                                             #Dopo la prima tabulazione invece stampiamo la parola da zero compreso e aumentare il contatatore+1 per stampare ad ogni riga tutta la parola python a piccoli passi.
                                                             #Infine con l'ultimo modo uniamo un po i primi due con la differenza che concateniamo le diverse parti.
   i=i+1 #Incrementiamo il contatore.

