import reflex as rx

from GameMini.body.juego_2.body import estado, numero, reglas
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

            rx.center(
                rx.hstack(
                    numero(),
                    rx.spacer(),
                    estado(),
                    ),width="100%"
                )
            )
        ),

        bg=Color.BACKGROUND.value,
        background_size= "cover",

        width="100%",
        height= "100vh"

    )