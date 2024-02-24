import reflex as rx

from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present
from GameMini.styles.elementos.button import butto
from GameMini.styles.tamaños import TamañosTextos


#en esta caja aparece como se juega el juego , son 10 reglas
def reglas_juego_uno() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.hstack(
                rx.heading("Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖" ,color=TextoColor.TITULO.value , font_size=TamañosTextos.TITULO .value)
            ),

            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.text("1.Piedra aplasta Tijeras : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value),
                        rx.text("La Piedra gana porque puede romper las Tijeras." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("2.Tijeras cortan Papel : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value),
                        rx.text("Las Tijeras ganan al cortar el Papel." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("3.Papel cubre Piedra : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Papel gana al cubrir la Piedra. " ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("4.Piedra aplasta Lagarto : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("La Piedra gana al aplastar al Lagarto." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("5.Lagarto envenena Spock :  " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Lagarto gana al envenenar a Spock." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("6.Spock destroza Tijeras:" ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("Spock gana al destrozar las Tijeras." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("7.Tijeras decapitan Lagarto : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("Las Tijeras ganan al decapitar al Lagarto." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("8.Lagarto come Papel : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Lagarto gana al comer el Papel." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("9.Papel desautoriza Spock : " ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("El Papel gana al desautorizar a Spock." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    rx.hstack(
                        rx.text("10.Spock vaporiza Piedra:" ,color=TextoColor.TITULO.value,font_size=TamañosTextos.subtitulo.value ),
                        rx.text("Spock gana al vaporizar la Piedra." ,color=TextoColor.SUBTITULOS.value,font_size=TamañosTextos.subtitulo.value),
                    ),
                    text_align="left"
                    )
            ),

        ),
            style=box_present(),


    ),
        width="100%"
)

#este botton te llevara al rauter donde se encuentra el juego
def continuar_a_juego_1():
    return rx.button(
        rx.link(
            rx.text(
                "continuar" , font_size=TamañosTextos.TITULO.value
            ),
            href=routers.JUEGO_UNO.value
        ),
        style=butto
        )

