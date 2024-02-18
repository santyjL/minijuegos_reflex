import random
import time

import reflex as rx

from GameMini.components.bottones import button3
from GameMini.styles.elementos.box import box_present2
from GameMini.styles.elementos.button import button5
from GameMini.styles.tamaños import TamañosTextos


class Estados(rx.State):
    lista : list = ["🥌","📋","✂","🦎","🖖"]
    jugada_npc : str = "❓"
    puntuacion_npc : int = 0

    jugada_jugador : str = "❓"
    puntuacion_jugador : int = 0

    def piedra(self ):
        self.jugada_jugador = "🥌"
        self.jugada_npc =random.choice(self.lista)

    def papel(self ):
        self.jugada_jugador = "📋"
        self.jugada_npc =random.choice(self.lista)

    def tijeras(self ):
        self.jugada_jugador = "✂"
        self.jugada_npc =random.choice(self.lista)

    def lagarto(self ):
        self.jugada_jugador = "🦎"
        self.jugada_npc =random.choice(self.lista)

    def spock(self ):
        self.jugada_jugador = "🖖"
        self.jugada_npc =random.choice(self.lista)


    @rx.var
    def jugadas_npc(self):
        return self.jugada_npc

    @rx.var
    def jugadas_jugador(self):
        return self.jugada_jugador


def jugador() -> rx.Component:
    return rx.box(
        rx.center(
            rx.heading(Estados.jugadas_jugador ,
                    font_size=TamañosTextos.ENORME.value ,
                    padding="0.3em"
                ),
            ),
        style=box_present2("100%"),
    )

def maquina() -> rx.Component:
    return rx.box(
        rx.center(
            rx.heading(Estados.jugadas_npc ,
                    font_size=TamañosTextos.ENORME.value ,
                    padding="0.3em"),
            ),
        style=box_present2("100%"),
    )

def separador() ->rx.component:
    return rx.vstack(
        rx.heading("El primero de 3 gana", font_size=TamañosTextos.subtitulo.value , ),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        )

def botones() -> rx.Component:
    return rx.box(
        rx.hstack(
            button3(button5, "🥌",  Estados.piedra, "50%"),
            button3(button5, "📋",  Estados.papel, "50%"),
            button3(button5, "✂",  Estados.tijeras, "50%"),
            button3(button5, "🦎",  Estados.lagarto, "50%"),
            button3(button5, "🖖",  Estados.spock, "50%"),
        )
   )