import reflex as rx

from GameMini.body.juego_1.reglas_2.body import (continuar_a_juego_1,
                                                 reglas_juego_uno)
from GameMini.components.navbar import navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color


@rx.page(route=routers.REGLAS_JUEGO_UNO.value)
def index () ->rx.Component:
    return rx.box(
        navbar(),
        reglas_juego_uno(),
        continuar_a_juego_1(),

        bg=Color.BACKGROUND.value,
        background_size= "cover",

        height= "100vh"

    )
