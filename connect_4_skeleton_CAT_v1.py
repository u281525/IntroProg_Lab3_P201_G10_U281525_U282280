"""
Connecta 4 — Plantilla per al Laboratori 2 (Introducció a la Programació)

Entrega:
- Un únic fitxer Python: PNNN_TNN_P3_U1_U2.py
- Ha d'executar-se localment amb: `python PNNN_TNN_P2_U1_U2.py`

Restriccions / Regles d'estil:
- Requereix pygame (instal·la amb `pip install pygame` si encara no el tens)
- Sí a `list`, `tuple`. No a `class`, no a `dict` ni cap estructura que no hàgim vist a classe
- Aquesta vegada no donem la signatura de cap funció. Tu decideixes l'estructura del programa!
- Totes les funcions han de rebre la informació necessària com a paràmetres, sense variables globals!
- Per aquest motiu, potser caldrà definir alguna variable dins de la funció main(), abans d'iniciar el bucle principal
- La part de renderitzat és totalment funcional i es proporciona al bucle principal; no cal canviar-la
- Però caldrà que hi afegeixis tota la lògica del joc

Control anti-IA de copiar/enganxar:
- Has de ser capaç d'explicar al professor tot el teu codi
- Has de ser capaç d'explicar seccions específiques del programa per verificar-ne la comprensió

Quin codi es proporciona:
Una vista simple però totalment funcional en pygame perquè l'alumnat es pugui centrar en el model i la lògica del joc.
La part de pygame (vista):
- dibuixa el tauler buit
- converteix els clics del ratolí a la franja superior en un índex de columna per detectar la columna de l'usuari
- dibuixa una fitxa en una posició (col,row) quan se li demana
Tota la lògica l'has d'implementar tu

Què heu d'implementar:
Dins de main():
- abans d'entrar al bucle principal i abans d'inicialitzar pygame, crida get_config() i pregunta a l'usuari si vol modificar condicions
- dins del bucle principal, has d'implementar tota la lògica del joc
- FES-HO TOT D'UNA MANERA BEN ESTRUCTURADA
- DEFINEIX I TRUCA TANTES FUNCIONS COM CONSIDERIS CONVENIENT

Fora de main:
defineix totes les funcions que es cridin:
- per a la configuració (get_config() i el que es cridi des d'aquí)
- per gestionar tota la lògica del joc
"""

import sys
import pygame
from random import randint

# =========================
# Configuració de tauler i UI
# =========================

# no cal canviar cap constant aquí — fes-ho sota la teva responsabilitat
# si canvies alguna d'aquestes opcions a get_config(), crea una nova variable — no sobreescriguis cap constant
COLS = 7
ROWS = 6
CELL_SIZE = 100            # píxels per cel·la
GRID_LINE = 6              # gruix de les línies de la graella del tauler
PADDING = 40               # marge exterior al voltant del tauler
TOKEN_MARGIN = 10          # marge interior dins d'una cel·la per al radi de la fitxa
SELECT_STRIP_HEIGHT = 60   # franja clicable sobre el tauler per seleccionar columna

WIDTH = PADDING * 2 + COLS * CELL_SIZE
HEIGHT = PADDING * 2 + ROWS * CELL_SIZE + SELECT_STRIP_HEIGHT

# Alguns colors predefinits (RGB)
# Pots crear els teus propis colors si vols (fes-ho des de get_config())
BG = (20, 24, 28)
BOARD_BG = (35, 60, 120)
GRID_COLOR = (15, 35, 85)
EMPTY_COLOR = (12, 16, 22)
RED = (220, 50, 47)
YELLOW = (253, 216, 53)
WHITE = (240, 240, 240)

# =========================
# Geometria (només vista)
# =========================
# millor no tocar res
BOARD_LEFT = PADDING
BOARD_TOP = PADDING + SELECT_STRIP_HEIGHT
BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

# =========================
# Globals (només vista)
# =========================
screen = None   # per a pygame

# =========================
# Escriviu aquí les vostres funcions !!!!!!!!
# =========================

# Part 1: Configuració (es crida abans d'iniciar el bucle principal)
def get_config():
    """ PENDENT ALUMNES: Actualment NO FA RES. Hauria de preguntar a l'usuari si vol modificar condicions, com ara:
    - 2 humans o humà vs màquina
    - colors dels 2 jugadors
    - mida del tauler (opcional)
    - qualsevol altra cosa que vulguis... (opcional)
        
    Ha de retornar allò que hagi canviat (NO utilitzeu variables globals)

    Esteu MOLT animats a reutilitzar funcions del laboratori 2, sempre que sigui possible, com ara:
    * ask_yes_no()
    * read_int_in_range()
    * read_int_in_range_w_default()
    * change_colors()
    * read_color()
    """

    # PENDENT: afegeix tot el codi necessari
    return None

# defineix aquí totes les funcions addicionals que calguin per a la configuració
# mantén-ho net, clar i ben estructurat

# ==============================================
# Part 2: Lògica del joc (es crida des del bucle principal)

# Defineix tantes funcions com consideris convenient
# per mantenir-ho net, clar i ben estructurat


def paint_piece_demo(col):
    """ Aquest codi només mostra com fer servir place_piece()
    place_piece() dibuixa una fitxa d'un color determinat en una posició donada (col i row)
    En aquesta demo només fem servir valors aleatoris (modifica-ho/elimina-ho!)"""
    
    rand_row = randint(0,ROWS-1) # fila aleatòria
    rand_color = (randint(0,255),randint(0,255),randint(0,255)) # color aleatori
    print(f"col:{col}, row:{rand_row}, color:{rand_color}")
    place_piece(col, rand_row, rand_color)



# ========================================
# Funcions d'ajuda per a la vista — No cal canviar res
# ========================================

def cell_center(col, row):
    """Retorna el centre en píxels (x, y) d'una cel·la donada."""
    x = BOARD_LEFT + col * CELL_SIZE + CELL_SIZE // 2
    y = BOARD_TOP + row * CELL_SIZE + CELL_SIZE // 2
    return x, y

def draw_board():
    """Dibuixa l'estructura del tauler (fons + franja de selecció + forats buits)."""
    # Fons
    screen.fill(BG)

    # Franja de selecció (part superior)
    sel_rect = pygame.Rect(PADDING, PADDING, BOARD_WIDTH, SELECT_STRIP_HEIGHT)
    pygame.draw.rect(screen, (50, 50, 55), sel_rect, border_radius=10)
    # Marques de columna a la franja
    for c in range(COLS):
        cx = BOARD_LEFT + c * CELL_SIZE + CELL_SIZE // 2
        cy = PADDING + SELECT_STRIP_HEIGHT // 2
        pygame.draw.circle(screen, WHITE, (cx, cy), 8)

    # Rectangle de fons del tauler
    board_rect = pygame.Rect(BOARD_LEFT, BOARD_TOP, BOARD_WIDTH, BOARD_HEIGHT)
    pygame.draw.rect(screen, BOARD_BG, board_rect, border_radius=16)

    # Forats de la graella (buits)
    token_radius = (CELL_SIZE // 2) - TOKEN_MARGIN
    for row in range(ROWS):
        for col in range(COLS):
            cx, cy = cell_center(col, row)
            pygame.draw.circle(screen, GRID_COLOR, (cx, cy), token_radius + GRID_LINE // 2)
            pygame.draw.circle(screen, EMPTY_COLOR, (cx, cy), token_radius)

    pygame.display.flip()

def place_piece(col:int, row:int, color:tuple) -> bool: 
    """ Dibuix només-vista: pinta una fitxa a (col,row) amb el color donat (R,G,B).
    Retorna True si (col,row) és dins dels límits i la dibuixa; False en cas contrari.

    Sense comprovacions d'ocupació, gravetat ni torns. El teu model decideix la validesa
    i després crida aquesta funció per reflectir el canvi visualment. """
    if screen is None:
        return False
    if not (0 <= col < COLS and 0 <= row < ROWS):
        return False

    cx, cy = cell_center(col, row)
    token_radius = (CELL_SIZE // 2) - TOKEN_MARGIN
    pygame.draw.circle(screen, color, (cx, cy), token_radius)
    pygame.draw.circle(screen, WHITE, (cx, cy), token_radius, width=2)
    pygame.display.flip()
    return True

def sel_column(mouse_pos):
    """Converteix una posició del ratolí en un índex de columna només dins de la franja superior de selecció.
    Retorna None si és fora. No hi ha lògica del joc aquí."""
    # comprova que el clic ha estat a la franja superior de selecció
    x, y = mouse_pos
    if not (PADDING <= x <= PADDING + BOARD_WIDTH and PADDING <= y <= PADDING + SELECT_STRIP_HEIGHT):
        return None
    
    # comprova la validesa de la columna
    col = (x - BOARD_LEFT) // CELL_SIZE
    if 0 <= col < COLS:
        return col
    else: 
        return None

def handle_mouse_click(mouse_pos):
    """Gestor mínim: només ens interessen els clics dins de la franja 
    i simplement cridem sel_col() per comprovar-ho"""
    return sel_column(mouse_pos)


# =========================
# Principal (basat en esdeveniments, espera bloquejant, sense FPS)
# =========================

def main():
    """PENDENT ALUMNES: Haureu d'afegir coses aquí, 
    per a la configuració d'usuari (abans del bucle principal)
    i per gestionar tota la lògica del joc (dins del bucle principal) """
    global screen

    # PENDENT: Defineix algunes variables abans d'iniciar pygame, com ara ...
    # board         # crea una matriu COLSxROWS plena de zeros
    # vs_machine    # booleà
    # ..... 
    # fes qualsevol configuració necessària, entrada d'usuari, etc.
    # pots preguntar opcions com colors, 2 o 1 jugadors, etc.
    get_config() # actualment no fa res
                
    # inici de pygame — No cal tocar res aquí
    pygame.init()
    pygame.display.set_caption("Connect 4 Basic")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Permetre només el conjunt mínim d'esdeveniments
    pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN])
    draw_board() # el tauler es dibuixa a l'inici

    running = True
    while running:
        event = pygame.event.wait()  # espera bloquejant fins que arribi un esdeveniment
        # només considerem 2 esdeveniments: QUIT (tancar la finestra) i 
        # MOUSEBUTTONDOWN a la part superior de la finestra, per triar una columna
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            col = handle_mouse_click(event.pos) # retorna el número de columna o None
            if col is not None: # el/la jugador/a ha clicat triant una columna

                # PENDENT ALUMNES:
                # comprova si la columna té espai lliure
                # troba la fila lliure més baixa d'aquesta columna
                # actualitza l'estat del tauler (tenint en compte quin jugador juga)
                # crida place_piece() per pintar la nova fitxa
                paint_piece_demo(col) # crida place_piece() aquí només per a la demo
                # detecta si hi ha 4 en línia -> si el joc ha acabat -> running = False
                # si no ha acabat, si vs_machine fes el moviment de la màquina, altrament canvia de jugador (1<->2)

                # AIXÒ SÓN NOMÉS PISTES, L'ORDRE POT SER DIFERENT
                # PERÒ FES-HO TOT D'UNA MANERA BEN ESTRUCTURADA
                # DEFINEIX I TRUCA TANTES FUNCIONS COM CONSIDERIS CONVENIENT


    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()