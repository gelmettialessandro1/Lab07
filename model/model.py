from copy import deepcopy


class Model:
    def __init__(self):
        self.risultati = []



    def best_15_giorni(self,sitG:list,sitT:list,sitM:list,parziale, M, T, G): #giorni M,giorni T, giorni G

        if M>6 or G>6 or T>6:
            return

        x = len(parziale)
        if x==15:
            self.risultati.append(deepcopy(parziale))
            return

        else:
            parziale.append(sitM[x])
            if self.ammissibile(parziale) == True:
                self.best_15_giorni(sitG,sitT,sitM,parziale, M+1, T, G)
            parziale.pop()

            parziale.append(sitT[x])
            if self.ammissibile(parziale) == True:
                self.best_15_giorni(sitG, sitT, sitM, parziale, M, T+1, G)
            parziale.pop()

            parziale.append(sitG[x])
            if self.ammissibile(parziale) == True:
                self.best_15_giorni(sitG, sitT, sitM, parziale, M, T, G+1)
            parziale.pop()


    def ammissibile(self,parziale:list):
        serie=[]
        count = 0;
        citta_prec = parziale[0].Localita
        for sit in parziale:
            if sit.Localita == citta_prec:
                count = count + 1
            else:
                serie.append(count)
                count = 1
                citta_prec = sit.Localita

        serie.append(count)#appendo anche l ultimo

        for i in range(len(serie)-1): #non guardo l'ultimo
            if serie[i] < 3:
                return False
        return True




    def costo_risultato(self,risultato):
        costo = 0
        for sit in risultato:
            costo = costo + sit.Umidita

        spostamenti=0

        for i in range(15):
            if(i!=14):
                if risultato[i].Localita != risultato[i+1].Localita:
                    spostamenti = spostamenti + 1


        #costo = costo + 100*spostamenti

        risultato.append(costo) # elemento con indice 15 del risultato e il suo costo
        return risultato




