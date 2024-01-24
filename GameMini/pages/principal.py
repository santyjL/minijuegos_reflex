import reflex as rx

from GameMini.body.body1.body import elemento_1, juego_1, otros_juegos
from GameMini.components.navbar import navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor


@rx.page(route=routers.PRINCIPAL.value)
def index () ->rx.components:
    return rx.box(
        navbar(),
        rx.center(
            elemento_1(),

        ),
        juego_1(),
        otros_juegos(),

        bg=Color.BACKGROUND.value,
        background_size= "cover",

        height= "100vh"

    )