import flet as ft

from UI.view import View
from model.model import Model
from database.meteo_dao import MeteoDao
from model.situazione import SituazioneDTO


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        meseScelto = self._view.dd_mese.value
        mese = int(meseScelto)

        sitG = []
        sitT = []
        sitM = []

        for situazione in MeteoDao.get_situazioni_mese(mese):
            if situazione.Localita=="Genova":
                sitG.append(situazione)
            if situazione.Localita == "Torino":
                sitT.append(situazione)
            if situazione.Localita == "Milano":
                sitM.append(situazione)

        sommaUG=0
        for situazione in sitG:
            sommaUG = sommaUG + int(situazione.Umidita)
        UmiditaMediaGenova = sommaUG/len(sitG)

        sommaUT = 0
        for situazione in sitT:
            sommaUT = sommaUT + int(situazione.Umidita)
        UmiditaMediaTorino = sommaUT / len(sitT)

        sommaUM = 0
        for situazione in sitM:
            sommaUM = sommaUM + int(situazione.Umidita)
        UmiditaMediaMilano = sommaUM / len(sitM)

        self._view.lst_result.controls.append(ft.Text(f"Genova: {UmiditaMediaGenova}"))
        self._view.lst_result.controls.append(ft.Text(f"Milano: {UmiditaMediaMilano}"))
        self._view.lst_result.controls.append(ft.Text(f"Torino: {UmiditaMediaTorino}"))

        self._view.update_page()



    def handle_sequenza(self, e):
        meseScelto = self._view.dd_mese.value
        mese = int(meseScelto)

        sitG = [] #primi 15 GG di situazione a Genova
        sitT = [] #primi 15 GG di situazione a Torino
        sitM = [] #primi 15 GG di situazione a Milano

        for situazione in MeteoDao.get_situazioni_mese(mese):
            if situazione.Localita == "Genova":
                sitG.append(situazione)
            if situazione.Localita == "Torino":
                sitT.append(situazione)
            if situazione.Localita == "Milano":
                sitM.append(situazione)


        M = Model()
        M.best_15_giorni(sitG, sitT, sitM, [],0,0,0)
        risultati = M.risultati
        risultati_con_costo=[]
        for risultato in risultati:
            risultati_con_costo.append(M.costo_risultato(risultato))

        risultati_ordinati = sorted(risultati_con_costo, key=lambda x: x[15])



        risultato_ottimo = risultati_ordinati[0]

        for i in range(0,15):
            self._view.lst_result.controls.append(ft.Text(f"{risultato_ottimo[i].Localita}---{risultato_ottimo[i].Data}---{risultato_ottimo[i].Umidita}"))
        self._view.lst_result.controls.append(ft.Text(f"{risultato_ottimo[15]}"))
        self._view.update_page()