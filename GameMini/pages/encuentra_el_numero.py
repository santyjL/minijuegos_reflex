import reflex as rx

from GameMini.body.juego_2.body import (botones, estado, estado_text, intentos,
                                        numero, reglas)
from GameMini.components.navbar import navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor


@rx.page(route=routers.JUEGO_DOS.value)
def index () ->rx.components:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                reglas(),
            )
        ),

        rx.center(

            rx.hstack(
                rx.vstack(
                    numero(),
                    botones()

                ),
                intentos(),
                rx.vstack(
                    estado(),
                    estado_text()
                    )
                )
            ),


        bg=Color.BACKGROUND.value,
        background_size= "cover",

        width="100%",
        height= "100vh"

    )