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
    JUEGO_DOS_FIN_DEL_JUEGO_PERDISTES = f"/{JUEGO_DOS}/PERDISTES"
    JUEGO_DOS_FIN_DEL_JUEGO_GANASTES = f"/{JUEGO_DOS}/GANASTES"