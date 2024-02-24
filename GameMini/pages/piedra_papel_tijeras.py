import reflex as rx

from GameMini.body.juego_1.body import (botones, jugador, maquina,
                                        puntuacion_jugador, puntuacion_NPC,
                                        separador)
from GameMini.components import final_juego, navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.elementos.button import button5
from GameMini.styles.tamaños import Tamaños, TamañosTextos


@rx.page(route=routers.JUEGO_UNO.value)
def index () ->rx.components:
    return rx.box(
        navbar.navbar(),

        rx.center(
            rx.hstack(
                rx.vstack(
                    puntuacion_jugador(),
                    jugador(),
                    botones(),
                ),
                separador(),
                rx.vstack(
                    puntuacion_NPC(),
                    maquina(),
                    rx.button("###N . P . C###" , style=button5)
                ),
                margin=Tamaños.MARGIN.value,
                spacing="6em"

            ),
        ),

        bg=Color.BACKGROUND.value,
        background_size= "cover",

        height= "100vh"

    )


@rx.page(route=routers.JUEGO_UNO_FIN_DEL_JUEGO_PERDISTES.value)
def perdistes() -> rx.component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.text("HAS PERDIDO" , font_size=TamañosTextos.ENORME.value , color=TextoColor.TITULO.value , ),
            final_juego.final_del_juego(routers.JUEGO_UNO.value)
            )
        ),
        bg=Color.BACKGROUND.value,
        background_size= "cover",
        top=0,

        width="100%",
        height= "100vh"
    )


@rx.page(route=routers.JUEGO_UNO_FIN_DEL_JUEGO_GANASTES.value)
def ganastes() -> rx.component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.text("HAS GANADO" , font_size=TamañosTextos.ENORME.value , color=TextoColor.TITULO.value , ),
            final_juego.final_del_juego(routers.JUEGO_UNO.value)
            )
        ),
        bg=Color.BACKGROUND.value,
        background_size= "cover",
        top=0,

        width="100%",
        height= "100vh"
    )