import reflex as rx

from GameMini.body.juego_3.body import ganador
from GameMini.components import final_juego, navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color


@rx.page(route=routers.JUEGO_TRES.value)
def index () ->rx.components:
    return rx.box(
        navbar.navbar(),

        rx.vstack(
            ganador(),
        ),

        bg=Color.BACKGROUND.value,
        background_size= "cover",

        height= "100vh"

    )