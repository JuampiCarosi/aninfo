CANTIDAD_FILAS_SUDOKU = 9
CANTIDAD_COLUMNAS_SUDOKU = 9
CANTIDAD_FILAS_CUADRADO = 3
CANTIDAD_COLUMNAS_CUADRADO = 3
IDENTIFICADOR_CELDA_VACIA = '?'

def validar_rango_numero(input, min, max):
    esValido = False
    if(input.isdigit()):
        numero = int(input)
        if(min <= numero <= max):
            esValido = True
        else:
            print("El numero ingresado no esta dentro del rango", end="")
    else:
        print("No ingresaste un numero", end="")
    return esValido

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
    repite = False
    contador = 0
    for fila in sudoku:
        contador += 1
        if(repite_numeros(fila)):
            print("Numero repetido en la fila {}".format(contador))
            repite = True
    return repite

def repite_columnas(sudoku):
    repite = False
    contador = 0
    for num_columna in range(CANTIDAD_COLUMNAS_SUDOKU):
        contador += 1
        columna = []
        for fila in sudoku:
            celda = fila[num_columna]
            columna.append(celda)
        if(repite_numeros(columna)):
            print("Numero repetido en la columna {}".format(contador))
            repite = True
    return repite

def repite_cuadrados(sudoku):
    repite = False
    contador = 0
    for inicio_fila in range(0, CANTIDAD_FILAS_SUDOKU, CANTIDAD_FILAS_CUADRADO):  # Itero filas dejando en inicio_fila el numero de fila donde inicia cada cuadrado
        for inicio_columna in range(0, CANTIDAD_COLUMNAS_SUDOKU, CANTIDAD_COLUMNAS_CUADRADO):  # Itero columnas dejando en inicio_columna el numero de columna donde inicia cada cuadrado
            contador += 1
            cuadrado = []
            for variante_fila in range(CANTIDAD_FILAS_CUADRADO):
                for variante_columna in range(CANTIDAD_COLUMNAS_CUADRADO): 
                    celda = sudoku[inicio_fila + variante_fila][inicio_columna + variante_columna]
                    cuadrado.append(celda)
            if(repite_numeros(cuadrado)):
                print("Numero repetido en el cuadrado {}".format(contador))
                repite = True
    return repite

def tiene_repeticiones(sudoku):
    rep_fil = repite_filas(sudoku)
    rep_col = repite_columnas(sudoku)
    rep_cuad = repite_cuadrados(sudoku)
    return rep_fil or rep_col or rep_cuad