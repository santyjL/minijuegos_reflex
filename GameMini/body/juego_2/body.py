import random

import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.elementos.box import box_present, elemento_box
from GameMini.styles.elementos.button import button
from GameMini.styles.tamaños import Tamaños, TamañosTextos


class Count(rx.State):
    num: int = random.randint(1 , 101)
    count: int = 1

    def increment_max(self):
        self.count +=10

    def decrementt_max(self):
        self.count -=10

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def reglas() -> rx.component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.text("Encuentra el numero , tenes 5 oportunidades para encontrar el numero , si lo logras habras ganado y si no habras perdido suerte" , color=TextoColor.SUBTITULOS.value ,font_size=TamañosTextos.subtitulo.value),

                margin_x=Tamaños.MARGIN_X.value,
                margin_y=Tamaños.MARGIN_Y.value
            ),
        ),
        style=box_present("70%") , margin=Tamaños.MARGIN.value,
  )

def numero() -> rx.component:
    return rx.box(
            rx.hstack(
                rx.text(Count.count , font_size=TamañosTextos.ENORME.value , color=TextoColor.ESPECIAL.value )
            ),text_alig="left",style=box_present("50%")
    )

def estado() -> rx.component:
    return rx.box(
            rx.hstack(
                rx.text(Count.count , font_size=TamañosTextos.ENORME.value , color=TextoColor.ESPECIAL.value )
            ),style=box_present("50%")
    )
