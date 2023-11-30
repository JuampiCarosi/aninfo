CANTIDAD_FILAS_SUDOKU = 9
CANTIDAD_COLUMNAS_SUDOKU = 9
CANTIDAD_FILAS_CUADRADO = 3
CANTIDAD_COLUMNAS_CUADRADO = 3
IDENTIFICADOR_CELDA_VACIA = '?'

def repite_numeros(celdas):
    numeros_vistos = set()
    for celda in celdas:
        numero = celda['numero']
        if(numero != IDENTIFICADOR_CELDA_VACIA):
            if numero in numeros_vistos:
                return True # Número repetido encontrado
            else:
                numeros_vistos.add(numero)
    return False

def repite_filas(sudoku):
    for fila in sudoku:
        if(repite_numeros(fila)):
            return True
    return False

def repite_columnas(sudoku):
    for num_columna in range(CANTIDAD_COLUMNAS_SUDOKU):
        columna = []
        for fila in sudoku:
            celda = fila[num_columna]
            columna.append(celda)
        if(repite_numeros(columna)):
            return True
    return False

def repite_cuadrados(sudoku):
    for inicio_fila in range(0, CANTIDAD_FILAS_SUDOKU, CANTIDAD_FILAS_CUADRADO):  # Itero filas dejando en inicio_fila el numero de fila donde inicia cada cuadrado
        for inicio_columna in range(0, CANTIDAD_COLUMNAS_SUDOKU, CANTIDAD_COLUMNAS_CUADRADO):  # Itero columnas dejando en inicio_columna el numero de columna donde inicia cada cuadrado
            cuadrado = []
            for variante_fila in range(CANTIDAD_FILAS_CUADRADO):
                for variante_columna in range(CANTIDAD_COLUMNAS_CUADRADO): 
                    celda = sudoku[inicio_fila + variante_fila][inicio_columna + variante_columna]
                    cuadrado.append(celda)
            if(repite_numeros(cuadrado)):
                return True
    return False

def tiene_repeticiones(sudoku):
    return repite_filas(sudoku) or repite_columnas(sudoku) or repite_cuadrados(sudoku)