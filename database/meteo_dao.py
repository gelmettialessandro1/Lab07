from database.DB_connect import DBConnect
from model.situazione import SituazioneDTO


class MeteoDao():

    @staticmethod
    def get_situazioni_mese(mese:int):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("""SELECT Umidita,Localita,Data
                              FROM situazione 
                              WHERE MONTH(Data)=%s
                              ORDER BY Data""",(mese,))
            for row in cursor:
                result.append(SituazioneDTO(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result


