from enum import Enum


#tamaños generales
class Tamaños(Enum):
    PADDING = "0.8"
    PADDING_X="0.6em"
    PADDING_Y="0.3em"
    MARGIN="3em"
    MARGIN_X="1.5em"
    MARGIN_Y="1em"
    BORDER_RADIUS="0.9em"
    BORDER_RADIUS_COMPLETO="10em"
    BORDER="1px solid #000"

#tamaños para el texto
class TamañosTextos(Enum):
    TITULO="2.7em"
    subtitulo="1.4em"
    MEDIANO="6.5em"
    ENORME= "13.5em"