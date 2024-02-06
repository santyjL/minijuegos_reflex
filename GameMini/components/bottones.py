import reflex as rx

from GameMini.styles.color import Color, TextoColor
from GameMini.styles.tamaños import Tamaños, TamañosTextos


#el botton uno tiene el parametro de estilo , texto , funcion y el ancho
def button1(estilo , texto , funcion , width ):
    return rx.button(
        rx.text(texto , font_size=TamañosTextos.TITULO.value , color = TextoColor.TITULO.value ),
        on_click=funcion,
        width=width,
        style=estilo,

    )

#el botton uno tiene el parametro de estilo , texto y el ancho(botones que no hacen nada)
def button2(estilo , texto , width ):
    return rx.button(
        rx.text(texto , font_size=TamañosTextos.TITULO.value , color = TextoColor.TITULO.value ),
        width=width,
        style=estilo,

    )
