# coding: utf-8

import numpy as np

taula = open('taulapro.txt','w')

# escribir: taula.write( 'd')
# leer linia, cuando la lee ya pasa a next: taula.readline()
# pseudoaleatorio=np.random.rand()
# prueva: p de que llueva = 0,05
# prueva: temps entre lluvias de paràmetre: lambda=8,75
"""
SUPOSICIÓ: PRIMER DIA SENSE VENTS; PARTIM AMB DIA COMPLETAMENT SOLEJAT I ESTUPENDUU
"""

T=0
Tvent=0
tramo=1
tot_comida=0
tot_litros=0

while tramo <= 50:

    if T == Tvent:

        y = np.random.rand()

        t_entrevents = int(-8.75*np.log(y))

        Tvent += (t_entrevents +1)

        """
        pongo el mas uno xq si sale que hay 0,6 dias entre llúvias implique siempre que se dan 
        el día siguiente sinó estaríamos en el mismo día y programa a la merde xq ya no haría nada más! 
        
        piensa que si hay un dia entre 2 lluvias y se calcula dia uno que llueve; entonces el dia dos no
        llueve; es el tres! (de ahí también el +1)

        """

        p_comida1 = np.random.rand()
        epcom1 = '%.3f' % p_comida1
             
        comida = (1 + 0.5*p_comida1)
        ecomida = '%.2f' % comida


        p_litros1 = np.random.rand()
        eplit1 = '%.3f' % p_litros1
        
        litros = (4 + 3.0*p_litros1)
        elitros = '%.2f' % litros
 
        if T == 0:
            "el primer día se calcula por cojones el tiempo hasta próximo viento; es el único en el que hay que especificar que no viento malo y si tramo!"
            escribir = str(T)+';no;'+str(t_entrevents)+';'+epcom1+';'+ecomida+';'+eplit1+';'+elitros+';'+str(tramo)+'\n'
            tramo+=1

        else:

            escribir = str(T)+';si;'+str(t_entrevents)+';'+epcom1+';'+ecomida+';'+eplit1+';'+elitros+'; '+'\n'
        
        taula.write(escribir)
        
        T+=1
        
    else:
        
        p_comida1 = np.random.rand()
        epcom1 = '%.3f' % p_comida1
  
        comida = (1 + 0.5*p_comida1) 
        ecomida = '%.2f' % comida
         
        p_litros1 = np.random.rand()
        eplit1 = '%.3f' % p_litros1
               
        litros = (4 + 3.0*p_litros1) 
        elitros = '%.2f' % litros
        
        escribir = str(T)+';no; ;'+epcom1+';'+ecomida+';'+eplit1+';'+elitros+';'+str(tramo)+'\n'

        taula.write(escribir)

        tramo+=1
       
        T+=1

    tot_comida+=comida
    tot_litros+=litros

escribir = 'Resultados Expedición:;Consumo Comida:'+'%.2f' % tot_comida+' Kg '+';Consumo Agua:'+'%.2f' % tot_litros+' L '+'\n'

taula.write('\n')
taula.write(escribir)
taula.close()
