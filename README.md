Este repositorio fue desarrollado por Nicolás Aguilera Varona, Juan David Bermúdez y Santiago Velandia. Tiene como objetivo usar la lógica proposicional para representar el problema de las ocho damas y resolverlo computacionalmente.

## I. DESCRIPCIÓN DEL PROBLEMA
El problema de las ocho damas consiste en colocar ocho damas de ajedrez en un tablero estándar 8x8, donde la principal
condición es que ninguna de las ocho damas debe ser capaz de atacar a otra.
En el ajedrez la dama es capaz de moverse y atacar en línea recta cualquier número de casillas que le sea posible en dirección
horizontal, vertical y diagonal. Por lo tanto, el objetivo es encontrar una configuración de las ocho damas en el tablero, de tal
forma que no existan dos damas que compartan la misma columna, la misma fila o la misma diagonal.

## II. DEFINICIÓN DE LETRAS PROPOSICIONALES
Para representar las posibles configuraciones del tablero de ajedrez utilizaremos un descriptor.
#### Descriptor:
La letra proposicional EN (x, y) se define como:
EN (x, y) ↔ Hay una dama ubicada en la casilla (x, y)
#### Conjuntos de Dominio:
Los parámetros x (filas), y (columnas) pertenecen a los conjuntos:
Filas = {1, 2, ... , 8} = F
Columnas = {1, 2, ... , 8} = C
Donde x ∈ Filas, y ∈ Columnas.
#### Letras Proposicionales:
De esta forma, el número total de letras proposicionales necesarias para describir el problema es:
8 filas × 8 columnas = 64 letras proposicionales

## III. ENUMERACIÓN DE LAS REGLAS DEL PROBLEMA
Ahora, para que la configuración de damas en el tablero se considere modelo, debe cumplir con las siguientes reglas:
**1. Regla de cantidad de piezas:** Debe haber al menos una dama en cada fila.
Observe que la regla de arriba funciona como reemplazo de la regla "debe haber al menos ocho damas".
**2. Regla de las filas:** No puede haber más de una dama en la misma fila.
**3. Regla de las columnas:** No puede haber más de una dama en la misma columna.
**4. Regla de las diagonales:** No puede haber más de una dama en la misma diagonal.

## IV. SIMBOLIZACIÓN DE LAS REGLAS DEL PROBLEMA
**1. Regla de cantidad de piezas:**
<div align="center">
  <img src="assets/images/regla1.png" alt="Regla 1" width="18%"/>
</div>

**2. Regla de las filas:**
<div align="center">
  <img src="assets/images/regla2.png" alt="Regla 2" width="40%"/>
</div>

**3. Regla de las columnas:**
<div align="center">
  <img src="assets/images/regla3.png" alt="Regla 3" width="40%"/>
</div>

**4. Regla de las diagonales:**  
<div align="center">
  <img src="assets/images/regla4.png" alt="Regla 4" width="40%"/>
</div>
