import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.color import Color, TextoColor
from GameMini.styles.tamaños import Tamaños


#el navbar estara en todos los router , contiene el codigo de github , y el nombre de la web
def navbar() -> rx.Component:
    return rx.box(
            rx.hstack(
                rx.link(
                    rx.hstack(
                    rx.heading("Game" , color=TextoColor.ESPECIAL.value ,size="lg"),
                    rx.heading("Mini" , color=TextoColor.TITULO.value , size="lg" ),
                    rx.heading("⭐" , color=TextoColor.TITULO.value ,size="lg")
                    ),
                    href=routers.PRINCIPAL.value,
                ),
                rx.spacer(),
                rx.link(
                    rx.image(src="/github icon.png" , width="3.6em" , height="100%"),
                    href="https://github.com/santyjL/minijuegos_reflex",
                    is_external=True
                ),

            ),
            bg=Color.PRINCIPAL.value,
            border = Tamaños.BORDER.value
        )

