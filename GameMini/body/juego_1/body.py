import reflex as rx
import random

from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present2, elemento_box
from GameMini.styles.tamaños import Tamaños, TamañosTextos


class Estados(rx.State):
    lista : list = ["🦎","🖖","✂","🥌","📋"]
    jugadas : str =random.choice(lista)

    @rx.var
    def jugada(self):
        return self.jugadas

def jugador() -> rx.Component:
    return rx.box(
        rx.center(
        rx.heading(Estados.jugada ,font_size=TamañosTextos.ENORME.value , padding=20),  # Texto o componentes internos
        ),
        style=box_present2("25%")
    )

def separador() ->rx.component:
    return rx.vstack(
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("El primero de 3 ganas", font_size=TamañosTextos.TITULO.value , ),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value),
        )