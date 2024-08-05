import reflex as rx

from GameMini.body.juego_2.body import (botones, estado, estado_text, intentos,
                                        numero, reglas)
from GameMini.components import final_juego, navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.tamaños import TamañosTextos


@rx.page(route=routers.JUEGO_DOS.value)
def index () ->rx.Component:
    return rx.box(
        navbar.navbar(),
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


@rx.page(route=routers.JUEGO_DOS_FIN_DEL_JUEGO_PERDISTES.value)
def perdistes() -> rx.component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.text("HAS PERDIDO" , font_size=TamañosTextos.ENORME.value , color=TextoColor.TITULO.value , ),
            final_juego.final_del_juego(routers.JUEGO_DOS.value)
            )
        ),
        bg=Color.BACKGROUND.value,
        background_size= "cover",
        top=0,

        width="100%",
        height= "100vh"
    )


@rx.page(route=routers.JUEGO_DOS_FIN_DEL_JUEGO_GANASTES.value)
def ganastes() -> rx.component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.text("HAS GANADO" , font_size=TamañosTextos.ENORME.value , color=TextoColor.TITULO.value , ),
            final_juego.final_del_juego(routers.JUEGO_DOS.value)
            )
        ),
        bg=Color.BACKGROUND.value,
        background_size= "cover",
        top=0,

        width="100%",
        height= "100vh"
    )