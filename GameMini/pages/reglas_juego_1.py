import reflex as rx

from GameMini.body.reglas_2.body import continuar_a_juego_1, reglas_juego_uno
from GameMini.components.navbar import navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor


@rx.page(route=routers.REGLAS_JUEGO_UNO.value)
def index () ->rx.components:
    return rx.box(
        navbar(),
        reglas_juego_uno(),
        continuar_a_juego_1(),

        bg=Color.BACKGROUND.value,
        background_size= "cover",

        height= "100vh"

    )
