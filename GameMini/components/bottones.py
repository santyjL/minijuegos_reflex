import reflex as rx

from GameMini.styles.color import Color, TextoColor
from GameMini.styles.tamaños import Tamaños, TamañosTextos


def button1(estilo , texto , funcion , width ):
    return rx.button(
        rx.text(texto , font_size=TamañosTextos.TITULO.value , color = TextoColor.TITULO.value ),
        on_click=funcion,
        width=width,
        style=estilo,

    )

def button2(estilo , texto , width ):
    return rx.button(
        rx.text(texto , font_size=TamañosTextos.TITULO.value , color = TextoColor.TITULO.value ),
        width=width,
        style=estilo,

    )
