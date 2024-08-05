import reflex as rx

from GameMini.body.juego_3.body import TicTacToeState, ganador
from GameMini.components import final_juego, navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.elementos.button import butto3
from GameMini.styles.tamaños import Tamaños, TamañosTextos


@rx.page(route=routers.JUEGO_TRES.value)
def index() -> rx.Component:
    juego_tablero = rx.grid(
        rx.foreach(
            rx.Var.range(3),
            lambda x: rx.foreach(
                rx.Var.range(3),
                lambda y: rx.grid_item(
                    rx.cond(
                        TicTacToeState.matriz[x][y] == "",
                       rx.button(
                            rx.text("⬜", font_size=TamañosTextos.TITULO.value),
                            on_click=lambda: TicTacToeState.juego(x, y),
                            padding=10
                        ),
                        rx.button(
                            rx.text(TicTacToeState.matriz[x][y], font_size=TamañosTextos.TITULO.value),
                            disabled=True,
                            padding=10
                        )
                    ),
                    col_span=1, row_span=1
                )
            )
        ),
        template_columns="repeat(3, 1fr)",
        template_rows="repeat(3, 1fr)",
        gap=4
    )

    return rx.box(
        navbar.navbar(),
        rx.vstack(
        ganador() ,
    ),
    rx.center(
    rx.hstack(
        juego_tablero,
        box_shadow= "11px 11px 11px 0px #FF5C00 , -11px -11px 11px 0px #32135A",
        padding=10
        ),
    ),
    rx.center(
        rx.button("Reset", on_click=TicTacToeState.reiniciar_juego, style=butto3),
        margin =Tamaños.MARGIN_Y.value
    ),
    bg=Color.BACKGROUND.value,
    background_size= "cover",

    height= "100vh"
)

@rx.page(route=routers.JUEGO_TRES_FIN_DEL_JUEGO_PERDISTES.value)
def perdistes() -> rx.component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.text("HAS PERDIDO" , font_size=TamañosTextos.ENORME.value , color=TextoColor.TITULO.value , ),
            final_juego.final_del_juego(routers.JUEGO_TRES.value)
            )
        ),
        bg=Color.BACKGROUND.value,
        background_size= "cover",
        top=0,

        width="100%",
        height= "100vh"
    )


@rx.page(route=routers.JUEGO_TRES_FIN_DEL_JUEGO_GANASTES.value)
def ganastes() -> rx.component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.text("HAS GANADO" , font_size=TamañosTextos.ENORME.value , color=TextoColor.TITULO.value , ),
            final_juego.final_del_juego(routers.JUEGO_TRES.value)
            )
        ),
        bg=Color.BACKGROUND.value,
        background_size= "cover",
        top=0,

        width="100%",
        height= "100vh"
    )