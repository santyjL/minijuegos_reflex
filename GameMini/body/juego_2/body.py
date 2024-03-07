import random

import reflex as rx

from GameMini.components.bottones import button1, button2
from GameMini.routers.routers import routers
from GameMini.styles.color import TextoColor
from GameMini.styles.elementos.box import box_present, box_present2
from GameMini.styles.elementos.button import butto3
from GameMini.styles.tamaños import Tamaños, TamañosTextos


#back-end
class Count(rx.State):

    #variables
    num: int = random.randint(1 , 101)
    count: int = 0
    estado : str = "¡¡¡¡!!!"
    intentos : int = 5


    def intentos_count(self):
        if self.intentos > 0:
            return False

        else :
            return True


    #verifica si se puede aumentar el numero si es haci lo aumenta
    def increment_max(self):
        if self.count < 91 :
            self.count +=10
        else :
            return


    def increment(self):
        if self.count <100:
            self.count += 1
        else :
            return

    #verifica si se puede disminuir el numero si es haci lo aumenta
    def decrementt_max(self):
        if self.count >9 :
            self.count -=10
        else :
            return


    def decrement(self):
        if self.count >0 :
            self.count -=1
        else :
            return

    #verifica si el numero es mayor o menor al numero a encontrar (por alguna razon no sirven los elif por eso uso match)
    def start(self):
        match self.num:
            case _ if self.num < self.count : self.estado = "<<<"
            case _ if self.num > self.count : self.estado = ">>>"
            case _ if self.num == self.count :self.estado = "==="

        self.intentos -= 1
        return self.redireccion()

    #define si el jugador a ganado o perdido y restablece las variables
    def redireccion(self):
        if self.estado == "===":
            self.intentos = 5
            self.estado = "¡¡¡¡!!!"
            self.num = random.randint(1 , 101)
            self.count = 0
            return rx.redirect(path=routers.JUEGO_DOS_FIN_DEL_JUEGO_GANASTES.value)

        if self.intentos <= 0:
            self.intentos = 5
            self.estado = "¡¡¡¡!!!"
            self.num = random.randint(1 , 101)
            self.count = 0
            return rx.redirect(path=routers.JUEGO_DOS_FIN_DEL_JUEGO_PERDISTES.value)

    #se crean las 2 variables que se muestran en la web y que son mutables
    @rx.var
    def get_count(self) -> int:
        return self.count

    @rx.var
    def get_estado(self) -> str:
        return self.estado

#se crea un apartado para el enunciado que indica de que trata el juego
def reglas() -> rx.component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.text("Encuentra el numero , tenes 5 oportunidades para encontrar el numero , si lo logras habras ganado y si no habras perdido suerte" , color=TextoColor.SUBTITULOS.value ,font_size=TamañosTextos.subtitulo.value),

                margin_x=Tamaños.MARGIN_X.value,
                margin_y=Tamaños.MARGIN_Y.value
            ),
        ),
        style=box_present("70%") , margin=Tamaños.MARGIN.value,
  )



#se crean todos los botones que modifica el estado de count
def botones() -> rx.component:
    return rx.box(
        rx.hstack(
            button1(butto3 , "+10" , Count.increment_max , "100%"),
            button1(butto3 ,"+1" ,Count.increment , "100%"),
            button1(butto3 , "Start" , Count.start , "100%"),
            button1(butto3 , "-10" , Count.decrementt_max , "100%"),
            button1(butto3 , "-1" ,Count.decrement , "100%")
        )
    )


#se muestra si el estado count es menor , mayor o igual al numero a encontrar
def estado_text() -> rx.component:
    return rx.box(
        rx.hstack(
            rx.cond(
                Count.estado != "===",
                button2(butto3,"no es igual" ,  "100%"),
                button2(butto3,"es igual" , "100%"),
            ),
        )
    )


#se crea la caja donde aparece el count
def numero() -> rx.component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(Count.count , font_size=TamañosTextos.ENORME.value , color=TextoColor.ESPECIAL.value )
            ),

        ),style=box_present2("100%" ),

    )


#se crea la caja donde aparece el estado
def estado() -> rx.component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(Count.estado , font_size=TamañosTextos.ENORME.value , color=TextoColor.ESPECIAL.value )
            ),
                ),style=box_present2("100%")
        )


#se crea la caja donde se actualiza los la cantidad de intentos
def intentos() -> rx.component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.text(Count.intentos , font_size=TamañosTextos.MEDIANO.value ,color=TextoColor.ESPECIAL.value,     PADDING_X=Tamaños.PADDING.value )
            )
        ),style=box_present2("100%")
    )
