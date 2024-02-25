import random

import reflex as rx

from GameMini.components.bottones import button3
from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present
from GameMini.styles.elementos.button import button5
from GameMini.styles.tamaños import Tamaños, TamañosTextos


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
