import reflex as rx

from GameMini.body.juego_1.body import botones, jugador, maquina, separador
from GameMini.components.navbar import navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color
from GameMini.styles.elementos.button import button5
from GameMini.styles.tamaños import Tamaños


@rx.page(route=routers.JUEGO_UNO.value)
def index () ->rx.components:
    return rx.box(
        navbar(),

        rx.center(
            rx.hstack(
                rx.vstack(
                    jugador(),
                    botones(),
                ),
                separador(),
                rx.vstack(
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