import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.elementos.button import butto4
from GameMini.styles.tamaños import TamañosTextos


def final_del_juego(juego: str) -> rx.Component:
    return rx.hstack(
        rx.button("Regresar al Menú", on_click=rx.redirect(path=routers.PRINCIPAL.value),font_size=TamañosTextos.subtitulo.value  , style=butto4),
        rx.button("Nueva Partida", on_click=rx.redirect(path=juego) ,font_size=TamañosTextos.subtitulo.value ,  style=butto4),
    )