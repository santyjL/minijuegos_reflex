import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.tamaños import Tamaños, TamañosTextos


def elemento_1 () -> rx.Component():
    return rx.box(
            rx.center(
            rx.heading("Mini Juegos disponibles" , color=TextoColor.TITULO.value  , font_size=TamañosTextos.TITULO.value ),
            ),
            border_radius= Tamaños.BORDER_RADIUS.value,
            background = Color.SEGUNDARIO.value,
            margin=Tamaños.MARGIN.value,
            PADDING_X=Tamaños.PADDING_X.value,
            border=Tamaños.BORDER.value,
            box_shadow= "1px 1px 1px 0px #FF5C00",

            width="40%"
    )

def juego_1() -> rx.Component():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.heading("Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖" ,color=TextoColor.TITULO.value , font_size=TamañosTextos.TITULO .value  ),
                        href=routers.REGLAS_JUEGO_UNO.value
                    )
                ),
                rx.hstack(
                    rx.text("El clasico juego de pieda papel o tijeras  lo conocemos todo el mundo pero no todos conocen el juego de piedra, papel, tijeras, gallina, spock" , color=TextoColor.SUBTITULOS.value , font_size=TamañosTextos.subtitulo.value , margin_x=Tamaños.MARGIN_X.value , margin_y=Tamaños.MARGIN_Y.value),
                ),
            ),
            border_radius= Tamaños.BORDER_RADIUS.value,
            background = Color.SEGUNDARIO.value,
            margin_x=Tamaños.MARGIN.value,
            PADDING_X=Tamaños.PADDING_X.value,
            border=Tamaños.BORDER.value,
            box_shadow= "1px 1px 1px 0px #FF5C00",

        ),
        width="100%",
        margin_y=Tamaños.MARGIN_Y.value
    )

def otros_juegos() -> rx.Component():
    return rx.box(
        rx.center(
        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.hstack(
                        rx.link(
                            rx.heading("Encuentra el numero 🎲" ,color=TextoColor.TITULO.value , font_size=TamañosTextos.TITULO .value  ),
                            href=routers.JUEGO_DOS.value

                    ),
                    ),
                    rx.hstack(
                        rx.text("del 1 al 100 se a perdido un numero pero cual sera, hay que entcontrarlo" , color=TextoColor.SUBTITULOS.value , font_size=TamañosTextos.subtitulo.value , margin_x=Tamaños.MARGIN_X.value , margin_y=Tamaños.MARGIN_Y.value),
                    ),
                border_radius= Tamaños.BORDER_RADIUS.value,
                background = Color.SEGUNDARIO.value,
                margin_x=Tamaños.MARGIN_X.value,
                PADDING_X=Tamaños.PADDING_X.value,
                border=Tamaños.BORDER.value,
                box_shadow= "1px 1px 1px 0px #FF5C00",
                width="50%"
            ),
            rx.spacer(),
            rx.center(
                rx.vstack(
                    rx.hstack(
                        rx.link(
                            rx.heading("Tres en raya ❌ | ⭕  " ,color=TextoColor.TITULO.value ,font_size=TamañosTextos.TITULO .value  ),
                            href=routers.JUEGO_TRES.value
                        )
                    ),
                    rx.hstack(
                        rx.text("El clasico “Tres en raya no podia faltar  un juego mitico que todos conocemos" , color=TextoColor.SUBTITULOS.value , font_size=TamañosTextos.subtitulo.value , margin_x=Tamaños.MARGIN_X.value , margin_y=Tamaños.MARGIN_Y.value),
                    ),
                ),
                border_radius= Tamaños.BORDER_RADIUS.value,
                background = Color.SEGUNDARIO.value,
                margin_x=Tamaños.MARGIN_X.value,
                PADDING_X=Tamaños.PADDING_X.value,
                border=Tamaños.BORDER.value,
                box_shadow= "1px 1px 1px 0px #FF5C00",
                width="50%",

            ),
        ),width="97%"
    )
)
    )