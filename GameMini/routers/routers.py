from enum import Enum


class routers(Enum):
    #principal
    PRINCIPAL="/principal"
    REGLAS_JUEGO_UNO="/reglas_juego_uno"
    JUEGO_UNO="/piedra_papel_tijeras_lagarto_spock"
    JUEGO_DOS="/Encuentra_el_numero"
    JUEGO_TRES="/3_en_rayas"
    JUEGO_CUATRO="/Ping_pong"

    #secundarias
    JUEGO_UNO_FIN_DEL_JUEGO_PERDISTES = f"/{JUEGO_UNO}/PERDISTES"
    JUEGO_UNO_FIN_DEL_JUEGO_GANASTES = f"/{JUEGO_UNO}/GANASTES"
    JUEGO_DOS_FIN_DEL_JUEGO_PERDISTES = f"/{JUEGO_DOS}/PERDISTES"
<<<<<<< HEAD
    JUEGO_DOS_FIN_DEL_JUEGO_GANASTES = f"/{JUEGO_DOS}/GANASTES"
=======
    JUEGO_DOS_FIN_DEL_JUEGO_GANASTES = f"/{JUEGO_DOS}/GANASTES"
    JUEGO_TRES_FIN_DEL_JUEGO_PERDISTES = f"/{JUEGO_TRES}/PERDISTES"
    JUEGO_TRES_FIN_DEL_JUEGO_GANASTES = f"/{JUEGO_TRES}/GANASTES"
>>>>>>> develop
