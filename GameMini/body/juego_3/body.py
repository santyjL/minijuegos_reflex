import random

import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present
from GameMini.styles.tamaños import Tamaños, TamañosTextos


class TicTacToeState(rx.State):
    matriz: list[list[str]] = [["", "", ""] for _ in range(3)]
    jugador: str = "❌"
    ganador: str = None
    jugador_puntuacion = 0
    npc_puntuacion = 0

    def juego(self, x, y):
        if not self.matriz[x][y] and not self.ganador:
            self.matriz[x][y] = self.jugador
            self.check_ganador()
            if self.ganador:
                self.sumar_punto()

            if not self.ganador:
                self.jugar_npc()

    def jugar_npc(self):
        posiciones_vacias = [(fila, columna) for fila in range(3) for columna in range(3) if self.matriz[fila][columna] == ""]
        if posiciones_vacias:
            fila_elegida, columna_elegida = random.choice(posiciones_vacias)
            self.matriz[fila_elegida][columna_elegida] = "⭕"
            self.check_ganador()
            if self.ganador:
                self.sumar_punto()

    def check_ganador(self):
        tablero = self.matriz
        lineas = [set(tablero[fila]) for fila in range(3)] + \
                 [set(tablero[fila][columnas] for fila in range(3)) for columnas in range(3)] + \
                 [set(tablero[fila][fila] for fila in range(3)), set(tablero[fila][2 - fila] for fila in range(3))]

        for linea in lineas:
            if len(linea) == 1 and "" not in linea:
                self.ganador = linea.pop()

    def reiniciar_juego(self):
        self.matriz = [["", "", ""] for _ in range(3)]
        self.jugador = "❌"
        self.ganador = None

        if self.puntuacion_jugador >= 5 or self.puntuacion_npc >= 5 :
            self.jugador_puntuacion = 0
            self.npc_puntuacion = 0
            return self.redireccion()

    def sumar_punto(self):
        if self.ganador == "❌":
            self.jugador_puntuacion += 1

        elif self.ganador == "⭕":
            self.npc_puntuacion += 1

        return self.redireccion()

    def redireccion(self):
        if self.puntuacion_jugador >= 5:
            self.reiniciar_juego()
            # Redirige a la ruta del jugador ganador
            return rx.redirect(path=routers.JUEGO_TRES_FIN_DEL_JUEGO_GANASTES.value)

        if self.puntuacion_npc >= 5:
            self.reiniciar_juego()
            # Redirige a la ruta del jugador perdedor o un mensaje genérico
            return rx.redirect(path=routers.JUEGO_DOS_FIN_DEL_JUEGO_PERDISTES.value)



    @rx.var
    def puntuacion_npc(self) -> int:
        return self.npc_puntuacion

    @rx.var
    def puntuacion_jugador(self) -> int:
        return self.jugador_puntuacion

def ganador() -> rx.component:
    return rx.box(
            rx.hstack(
                rx.vstack(
                    rx.heading("-NPC-" ,
                               color=TextoColor.ESPECIAL.value,
                               size="2xl"),

                    rx.heading(f"Puntaje:{TicTacToeState.puntuacion_npc}" ,
                               color=TextoColor.ESPECIAL.value,
                               size="xl"),
                ),
                rx.stack(
                    rx.text("El primero de 5 gana" ,
                            color=TextoColor.TITULO.value ,
                            font_size=TamañosTextos.TITULO.value),


                    style=box_present("100%") , margin=Tamaños.MARGIN.value,
                ),
                rx.vstack(
                    rx.heading("-Tu-" ,
                               color=TextoColor.ESPECIAL.value,
                               size="2xl"),

                    rx.heading(f"Puntaje:{TicTacToeState.puntuacion_jugador}" ,
                               color=TextoColor.ESPECIAL.value,
                               size="xl"),
                ),
                spacing="16em"

            ),
            margin_x=Tamaños.MARGIN_X.value,
            margin_y=Tamaños.MARGIN_Y.value,

  )

