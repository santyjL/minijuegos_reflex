import reflex as rx

from GameMini.body.juego_3.body import TicTacToeState, ganador
from GameMini.components import final_juego, navbar
from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.elementos.button import butto3, button5


@rx.page(route=routers.JUEGO_TRES.value)
def index () ->rx.components:
    juego_tablero = rx. grid(
        rx.foreach(
            rx.Var.range(3),
            lambda x: rx.foreach(
                rx.Var.range(3),
                lambda y: rx.cond(
                    TicTacToeState.matriz[x][y] == "",
                    rx.button("-", on_click=lambda: TicTacToeState.juego(x, y)),
                    rx.button(TicTacToeState.matriz[x][y], disabled=True)
                )
            ),
        ),
        columns="3",
        spacing="4",
    )

    ganador_texto = rx.cond(
        TicTacToeState.ganador,
        rx.text(f"Player {TicTacToeState.ganador} wins!", color=TextoColor.ESPECIAL.value),
        rx.text("")
    )  # Utiliza 'rx.cond' para mostrar el texto del ganador condicionalmente

    return rx.box(
        navbar.navbar(),
        rx.vstack(
        ganador() ,



    ),
    rx.center(
    rx.hstack(
        juego_tablero,
        ),
    ),
    rx.button("Reset", on_click=TicTacToeState.reiniciar_juego, style=butto3),
    bg=Color.BACKGROUND.value,
    background_size= "cover",

    height= "100vh"
)