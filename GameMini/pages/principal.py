import reflex as rx

from GameMini.body.principal1.body import elemento_1, todos_los_juegos
from GameMini.components.navbar import navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color


@rx.page(route=routers.PRINCIPAL.value)
def index () ->rx.components:
    return rx.box(
        navbar(),
        rx.center(
            elemento_1(),

        ),
        todos_los_juegos(),

        bg=Color.BACKGROUND.value,
        background_size= "cover",

        height= "100vh"

    )