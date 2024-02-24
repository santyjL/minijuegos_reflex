import random

import reflex as rx

from GameMini.components.bottones import button3
from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present2
from GameMini.styles.elementos.button import button5
from GameMini.styles.tamaños import TamañosTextos


#Back -end del juego
class Estados(rx.State):
    #variables del NPC
    lista : list = ["🥌","📋","✂","🦎","🖖"]
    jugada_npc : str = "❓"
    puntuacion_npc : int = 0

    #variables del jugador
    jugada_jugador : str = "❓"
    puntuacion_jugador : int = 0

    #funciones de las acciones de los botones , para seleccionar la jugada que resalizara el jugador
    def piedra(self):

        self.jugada_jugador = "🥌"
        self.jugada_npc =random.choice(self.lista)
        return self.comprobador_ganador()


    def papel(self):
        self.jugada_jugador = "📋"
        self.jugada_npc =random.choice(self.lista)
        return self.comprobador_ganador()


    def tijeras(self):
        self.jugada_jugador = "✂"
        self.jugada_npc =random.choice(self.lista)
        return self.comprobador_ganador()


    def lagarto(self):
        self.jugada_jugador = "🦎"
        self.jugada_npc =random.choice(self.lista)
        return self.comprobador_ganador()


    def spock(self):
        self.jugada_jugador = "🖖"
        self.jugada_npc =random.choice(self.lista)
        return self.comprobador_ganador()

    #comprueba si el jugador o el npc gana la ronda y le da el punto correspondido , como tambien el empate
    def comprobador_ganador(self):
        #listas de las posibles jugadas
        piedra_pierde = ["📋","🖖"]
        tijeras_pierde = ["🥌","🖖"]
        papel_pierde = ["✂","🦎"]
        lagarto_pierde = ["🥌","✂"]
        spock_pierde = ["📋" , "🦎"]
        match self.jugada_jugador:
            case _ if self.jugada_jugador== self.jugada_npc : self.puntuacion_jugador -=0
            case _ if self.jugada_jugador=="🥌" and self.jugada_npc not in piedra_pierde: self.puntuacion_jugador +=1
            case _ if self.jugada_jugador=="✂" and self.jugada_npc not in tijeras_pierde : self.puntuacion_jugador +=1
            case _ if self.jugada_jugador=="📋" and self.jugada_npc not in papel_pierde: self.puntuacion_jugador +=1
            case _ if self.jugada_jugador=="🦎" and self.jugada_npc not in lagarto_pierde: self.puntuacion_jugador +=1
            case _ if self.jugada_jugador=="🖖" and self.jugada_npc not in spock_pierde: self.puntuacion_jugador +=1
            case _ : self.puntuacion_npc +=1

        return self.redirrecion()

    #verifica quien tiene mayor puntuacion y te manda una pantalla de perdido o ganado
    def redirrecion (self):
        if self.puntuacion_jugador == 3 :

            self.jugada_npc  = "❓"
            self.puntuacion_npc  = 0

            self.jugada_jugador = "❓"
            self.puntuacion_jugador  = 0
            return rx.redirect(path=routers.JUEGO_UNO_FIN_DEL_JUEGO_GANASTES.value)

        if self.puntuacion_npc == 3:

            self.jugada_npc  = "❓"
            self.puntuacion_npc  = 0

            self.jugada_jugador = "❓"
            self.puntuacion_jugador  = 0
            return rx.redirect(path=routers.JUEGO_UNO_FIN_DEL_JUEGO_PERDISTES.value)

    #variables mutables que se muestran en el front -end
    @rx.var
    def jugadas_npc(self):
        return self.jugada_npc


    @rx.var
    def jugadas_jugador(self):
        return self.jugada_jugador


    @rx.var
    def puntuaciones_npc(self):
        return self.puntuacion_npc


    @rx.var
    def puntuaciones_jugador(self):
        return self.puntuacion_jugador


#texto donde se muestra la puntuacion del jugador
def puntuacion_jugador() -> rx.Component:
    return rx.text(
            rx.span("puntuación : " , color=TextoColor.TITULO.value) ,
            rx.span(f"{Estados.puntuacion_jugador}" , color="blue" , font_weight="bold"),

            font_size = TamañosTextos.subtitulo.value ,
                )


#texto donde se muestra la puntuacion del npc
def puntuacion_NPC() -> rx.Component:
    return rx.text(
            rx.span("puntuación : " , color=TextoColor.TITULO.value) ,
            rx.span(f"{Estados.puntuacion_npc}" , color="blue" , font_weight="bold"),

            font_size = TamañosTextos.subtitulo.value ,
                )

#aqui se muestra la jugada que eligio el jugador
def jugador() -> rx.Component:
    return rx.box(
        rx.center(
            rx.heading(Estados.jugadas_jugador ,
                    font_size=TamañosTextos.ENORME.value ,
                    padding="0.3em"
                ),
            ),
        style=box_present2("100%"),
    )


#aqui se muestra la jugada random del NPC
def maquina() -> rx.Component:
    return rx.box(
        rx.center(
            rx.heading(Estados.jugadas_npc ,
                    font_size=TamañosTextos.ENORME.value ,
                    padding="0.3em"),
            ),
        style=box_present2("100%"),
    )



def separador() ->rx.component:
    return rx.vstack(
        rx.heading("El Primero De 3 Gana", font_size=TamañosTextos.subtitulo.value ,color=TextoColor.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value,color=TextoColor.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value,color=TextoColor.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value,color=TextoColor.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value,color=TextoColor.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value,color=TextoColor.TITULO.value),
        rx.heading("|", font_size=TamañosTextos.TITULO.value,color=TextoColor.TITULO.value),
        )

#se crean los botones donde que el jugador eliga su siguiente jugada
def botones() -> rx.Component:
    return rx.box(
        rx.hstack(
            button3(button5, "🥌",  Estados.piedra, "50%"),
            button3(button5, "📋",  Estados.papel, "50%"),
            button3(button5, "✂",  Estados.tijeras, "50%"),
            button3(button5, "🦎",  Estados.lagarto, "50%"),
            button3(button5, "🖖",  Estados.spock, "50%"),
        )
   )