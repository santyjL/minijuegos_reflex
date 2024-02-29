import reflex as rx

from GameMini.components.bottones import button3
from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present
from GameMini.styles.elementos.button import button5
from GameMini.styles.tamaños import Tamaños, TamañosTextos


class TicTacToeState(rx.State):
    matriz: list[list[str]] = [["", "", ""],
                               ["" , "" , ""],
                               ["" , "" , ""]]
    Jugador_actual: str = "X"
    ganador: str = None

    def juego(self, x, y):
        if not self.matriz[x][y] and not self.ganador:
            self.matriz[x][y] = self.Jugador_actual
            self.check_ganador()
            self.Jugador_actual = "O" if self.Jugador_actual == "X" else "X"

    def check_ganador(self):
        # Check horizontal, vertical and diagonal for ganador
        tablero = self.matriz
        lines = [tablero[fila] for fila in range(3)] + [[tablero[fila][columnas] for fila in range(3)] for columnas in range(3)] + \
                [[tablero[fila][fila] for fila in range(3)], [tablero[fila][2 - fila] for fila in range(3)]]
        for line in lines:
            if line[0] == line[1] == line[2] and line[0] != "":
                self.ganador = line[0]
                return

    def reiniciar_juego(self):
        self.matriz = [["", "", ""],
                       ["" , "" , ""],
                       ["" , "" , ""]]
        self.Jugador_actual = "X"
        self.ganador = None


def ganador() -> rx.component:
    return rx.box(
            rx.hstack(

                rx.vstack(
                    rx.heading("-Tu-" ,
                               color=TextoColor.ESPECIAL.value,
                               size="2xl"),

                    rx.heading(f"Puntaje: " ,
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

                    rx.heading(f"Puntaje: " ,
                               color=TextoColor.ESPECIAL.value,
                               size="xl"),
                ),
                spacing="16em"

            ),
            margin_x=Tamaños.MARGIN_X.value,
            margin_y=Tamaños.MARGIN_Y.value,

  )

