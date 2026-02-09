from IPython.display import Image, display
import requests
from types import MethodType

from Logica import *

def escribir_damas(self, literal):
    if '-' in literal:
        atomo = literal[1:] #eliminar el primer elemento, aka el "no"
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    f, c = self.unravel(atomo) #La letra, se decodifica
    return f"Hay una Dama en la casilla ({f},{c})" #escribir devuelta en español


class Damas:

    '''
    Clase para representar el problema de poner
    ocho damas en un tablero de ajedrez sin que
    se ataquen entre sí
    '''
    
    def __init__(self, F = 8, C = 8):
        self.F = F
        self.C = C
        self.EN = Descriptor([F, C])
        self.EN.escribir = MethodType(escribir_damas, self.EN)
        r1 = self.regla1()
        r2 = self.regla2()
        r3 = self.regla3()
        r4 = self.regla4()
        self.reglas = [r1, r2, r3, r4]

    def regla1(self):
        '''
        En cada fila debe haber al menos una reina.
        '''
        filas = [x for x in range(self.F)]
        columnas = [y for y in range (self.C)]
        lista = []
        for x in filas:
            lista_o = []
            for y in columnas:
                lista_o.append(self.EN.ravel([x,y]))
            lista.append(Otoria(lista_o))
        return Ytoria(lista)
    def regla2(self): # Mi mejor esfuerzo
        '''
        No pueden haber reinas en la misma fila
        '''
        filas = [x for x in range(self.F)]
        columnas = [y for y in range (self.C)]
        lista = []
        for x in filas:
            for y in columnas:
                otras_columnas = [k for k in range(self.C) if k!=y]
                lista_o = []
                for k in otras_columnas:
                    lista_o.append(self.EN.ravel([x ,k]))
                form = '(' + self.EN.ravel([x, y]) + ">-" + Otoria(lista_o) + ')'
                lista.append(form)
        return Ytoria(lista)
    def regla3(self):
        '''
        No pueden haber reinas en la misma columna
        '''
        filas = [x for x in range(self.F)]
        columnas = [y for y in range (self.C)]
        lista = []
        for y in columnas:
            for x in filas:
                otras_filas = [k for k in range(self.F) if k!=x]
                lista_o = []
                for k in otras_filas:
                        lista_o.append(self.EN.ravel([k ,y]))
                form = '(' + self.EN.ravel([x, y]) + ">-" + Otoria(lista_o) + ')'
                lista.append(form)
        return Ytoria(lista)
    def regla4(self):
        '''
        No pueden haber reinas en la misma diagonal
        '''
        filas = [x for x in range(self.F)]
        columnas = [y for y in range (self.C)]
        lista = []
        for x in filas:
            for y in columnas:
                lista_o = []
                for k in filas:
                    for u in columnas:
                        if (k,u) != (x,y) and abs(x-k) == abs (y-u):
                            lista_o.append(self.EN.ravel([k, u]))
                form = '(' + self.EN.ravel([x, y]) + ">-" + Otoria(lista_o) + ')'
                lista.append(form)
        return Ytoria(lista)
    
    def visualizar(self, Interpretacion: dict) -> None:
        self.visualizar_tablero(self.Interpretacion_To_Fen(Interpretacion))

    def visualizar_tablero(self, fen_url: str) -> None:
        # El FEN correcto
        fen = "4Q3%2F7Q%2F3Q4%2F1Q6%2F6Q1%2FK7%2F5Q2%2F2Q5"
        
        # URL para obtener la imagen desde Lichess con los parámetros correctos
        url = f"https://lichess1.org/export/fen.gif?fen={fen_url}+w+-+-+0+1&color=white&variant=standard&theme=brown&piece=cburnett"
        
        # Realizamos la solicitud HTTP para obtener la imagen
        response = requests.get(url)
        
        # Verificamos si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Mostrar la imagen directamente en el Jupyter Notebook
            display(Image(data=response.content))
        else:
            print(f"Error al obtener la imagen. Código de estado: {response.status_code}")
            print(url)
    
    
    def Interpretacion_To_Fen(self, Interpretacion: dict) -> str:
        if Interpretacion != None:
            FEN_array = ["........"] * 8
            for k in Interpretacion:
                if not (self.EN.chrInit <= ord(k) < self.EN.chrInit + self.F * self.C):
                    continue
                if Interpretacion[k] == True:
                    fila, columna = self.EN.unravel(k)
                    # print(f"Tenemos la fila: {fila}, y la columna {columna}")
                    FEN_row = list(FEN_array[7 - fila])
                    FEN_row[columna] = "Q" # Como solo usamos damas es muy xD
                    # print(FEN_row)
                    FEN_array[7 - fila] = "".join(FEN_row)
            for i in range(8):
                FEN_array[i] = self.convert_to_fen_row(FEN_array[i])
    
            FEN = "%2F".join(FEN_array)
            return FEN
                
        else:
            print("No hay solución")  
            return None
    
    def convert_to_fen_row(self, row: str) -> str:
        fen_row = ""
        empty_count = 0
        for char in row:
            if char == '.':
                empty_count += 1  # Contamos las casillas vacías
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)  # Escribimos el número de casillas vacías
                    empty_count = 0  # Reseteamos el contador
                fen_row += char  # Añadimos la pieza
        if empty_count > 0:  # Si terminamos la fila con vacíos, los añadimos
            fen_row += str(empty_count)
        return fen_row  
    