import random

import reflex as rx

from GameMini.components.bottones import button1, button2
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.elementos.box import (box_present, box_present2,
                                           elemento_box)
from GameMini.styles.elementos.button import butto, butto2, butto3
from GameMini.styles.tamaños import Tamaños, TamañosTextos


class Count(rx.State):
    num: int = random.randint(1 , 101)
    count: int = 0
    estado : str = "¡¡¡¡!!!"
    intentos : int = 5


    def increment_max(self):
        if self.count < 91 :
            self.count +=10
        else :
            return

    def decrementt_max(self):
        if self.count >9 :
            self.count -=10
        else :
            return

    def increment(self):
        if self.count <100:
            self.count += 1
        else :
            return

    def decrement(self):
        if self.count >0 :
            self.count -=1
        else :
            return

    def start(self):
        match self.num:
            case _ if self.num < self.count : self.estado = "<<<"
            case _ if self.num > self.count : self.estado = ">>>"
            case _ if self.num == self.count :self.estado = "==="

        self.intentos -= 1

    @rx.var
    def get_count(self) -> int:
        return self.count

    @rx.var
    def get_estado(self) -> str:
        return self.estado



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

def intentos() -> rx.component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.text(Count.intentos , font_size=TamañosTextos.MEDIANO.value ,color=TextoColor.ESPECIAL.value,     PADDING_X=Tamaños.PADDING.value )
            )
        ),style=box_present2("100%")
    )


def botones() -> rx.component:
    return rx.box(
        rx.hstack(
            button1(butto3 , "+10" , Count.increment_max , "100%"),
            button1(butto3 ,"+1" ,Count.increment , "100%"),
            button1(butto3 , "Start" , Count.start , "100%"),
            button1(butto3 , "-10" , Count.decrementt_max , "100%"),
            button1(butto3 , "-1" ,Count.decrement , "100%")
        )
    )

def estado_text() -> rx.component:
    return rx.box(
        rx.hstack(
            rx.cond(
                Count.estado != "===",
                button2(butto3,"no es igual" ,  "100%"),
                button2(butto3,"es igual" , "100%"),
            ),
        )
    )

def numero() -> rx.component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(Count.count , font_size=TamañosTextos.ENORME.value , color=TextoColor.ESPECIAL.value )
            ),

        ),style=box_present2("100%" ),

    )

def estado() -> rx.component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(Count.estado , font_size=TamañosTextos.ENORME.value , color=TextoColor.ESPECIAL.value )
            ),
                ),style=box_present2("100%")
        )
