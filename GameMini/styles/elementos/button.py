import reflex as rx

from GameMini.styles.color import Color
from GameMini.styles.tamaños import Tamaños

#paleta de estilo todos son iguales solo cambia el orden de colores
butto= dict(
        border_radius= Tamaños.BORDER_RADIUS.value,
        background = Color.PRINCIPAL.value,
        border=Tamaños.BORDER.value,
        box_shadow= "2px 2px 2px 0px #32135A",
        margin_left = "75%"
)

butto2= dict(
        border_radius= Tamaños.BORDER_RADIUS.value,
        background = Color.SEGUNDARIO.value,
        border=Tamaños.BORDER.value,
        box_shadow= "2px 2px 2px 0px #32135A",
        margin_left = "75%"
)

#estos no tienen el margin left
butto3= dict(
        border_radius= Tamaños.BORDER_RADIUS.value,
        background = Color.SEGUNDARIO.value,
        border=Tamaños.BORDER.value,
        box_shadow= "2px 2x 2px 0px #FF5C00",
)

#paleta de estilo todos son iguales solo cambia el orden de colores
butto4= dict(
        border_radius= Tamaños.BORDER_RADIUS.value,
        background = Color.PRINCIPAL.value,
        border=Tamaños.BORDER.value,
        box_shadow= "2px 2px 2px 0px #32135A",
)