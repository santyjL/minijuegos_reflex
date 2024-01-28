import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present, elemento_box
from GameMini.styles.tamaños import Tamaños, TamañosTextos


def elemento_1 () -> rx.Component():
    return rx.box(
            rx.center(
            rx.heading("Mini Juegos disponibles" , color=TextoColor.TITULO.value  , font_size=TamañosTextos.TITULO.value ),
            ),
            style=elemento_box
    )

def juego_1() -> rx.Component():
    return rx.box(
        rx.center(
            rx.vstack(
                    rx.link(
                        rx.heading("Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖" ,color=TextoColor.TITULO.value , font_size=TamañosTextos.TITULO .value  ),
                        href=routers.REGLAS_JUEGO_UNO.value
                    ),


                    rx.text("El clasico juego de pieda papel o tijeras  lo conocemos todo el mundo pero no todos conocen el juego de piedra, papel, tijeras, gallina, spock" , color=TextoColor.SUBTITULOS.value , font_size=TamañosTextos.subtitulo.value ),

                    margin_x=Tamaños.MARGIN_X.value , margin_y=Tamaños.MARGIN_Y.value
            ),
            style=box_present()

        ),
        width="100%",
        margin_y=Tamaños.MARGIN_Y.value
    )

def juego_2() -> rx.Component():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.link(
                    rx.heading("Encuentra el numero 🎲" ,color=TextoColor.TITULO.value , font_size=TamañosTextos.TITULO .value  ),
                    href=routers.JUEGO_DOS.value
                ),
                rx.text("del 1 al 100 se a perdido un numero pero cual sera, hay que entcontrarlo" , color=TextoColor.SUBTITULOS.value , font_size=TamañosTextos.subtitulo.value ),
                margin_x=Tamaños.MARGIN_X.value , margin_y=Tamaños.MARGIN_Y.value
            ),
            style=box_present("92.4%")
        ),
        width="100%"
    )

def juego_3() -> rx.Component():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.link(
                    rx.heading("Tres en raya ❌ | ⭕  " ,color=TextoColor.TITULO.value ,font_size=TamañosTextos.TITULO .value  ),
                    href=routers.JUEGO_TRES.value
                ),
                rx.text("El clasico “Tres en raya no podia faltar  un juego mitico que todos conocemos" , color=TextoColor.SUBTITULOS.value , font_size=TamañosTextos.subtitulo.value ,),
                margin_x=Tamaños.MARGIN_X.value , margin_y=Tamaños.MARGIN_Y.value
            ),
            style=box_present("92.4%")
        ),
        width="100%"
    )

def todos_los_juegos() -> rx.Component():
    return rx.box(
        rx.center(
            rx.vstack(
                juego_1(),
                rx.center(
                    rx.hstack(
                        juego_2(),
                        rx.spacer(),
                        juego_3(),
                    ),
                    width="100%"
                ),
            ),
        ),
        width="100%"
    )
