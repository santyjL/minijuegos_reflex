import reflex as rx

from GameMini.styles.color import Color, TextoColor
from GameMini.styles.tamaños import Tamaños, TamañosTextos


def box_present(width = None):
    juegos_box= dict (
        border_radius= Tamaños.BORDER_RADIUS.value,
        background = Color.SEGUNDARIO.value,
        margin_x=Tamaños.MARGIN_X.value,
        margin_y=Tamaños.MARGIN_Y.value,
        padding = Tamaños.PADDING.value,
        border=Tamaños.BORDER.value,
        box_shadow= "2px 2px 2px 0px #FF5C00",
        width=width,
    )
    return juegos_box


def box_present2(width = None):
    juegos_box= dict (
        border_radius= Tamaños.BORDER_RADIUS.value,
        background = Color.PRINCIPAL.value,
        margin_x=Tamaños.MARGIN_X.value,
        margin_y=Tamaños.MARGIN_Y.value,
        padding = Tamaños.PADDING.value,
        border=Tamaños.BORDER.value,
        box_shadow= "2px 2px 2px 0px #32135A",
        width=width,
    )
    return juegos_box

elemento_box = dict(
            border_radius= Tamaños.BORDER_RADIUS.value,
            background = Color.SEGUNDARIO.value,
            margin=Tamaños.MARGIN.value,
            padding=Tamaños.PADDING.value,
            border=Tamaños.BORDER.value,
            box_shadow= "2px 2px 2px 0px #FF5C00",
            width="40%"
)

