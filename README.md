# Sudoku
## ¿Qué es esto?
Es una simple app para jugar al Sudoku con una simple interfaz via cli.

## Tecnologías utilizadas
- [Python](https://www.python.org/downloads/)
- [termcolor](https://pypi.org/project/termcolor/)

## ¿Cómo correr el programa?
Para correr el juego en primero lugar se debe clonar el repositorio:
```
git clone https://github.com/JuampiCarosi/aninfo sudoku
```
Instalar la dependencia de termcolor:
```
pip3 install termcolor
```
Y luego entrar a la carpeta y ejecutar el programa principal:
```
cd sudoku && python3 sudoku.py
```
## ¿Cómo jugar?
Primero, el jugador deberá elegir la dificultad deseada mediante un número del 1 al 3, siendo 1 la dificultad más fácil, 2 la media y 3 la más difícil. Luego, se le mostrara el tablero con algunos números iniciales y se le brindara ciertas opciones para realizar.
- **1**: Ingresar un numero en una celda.
- **2**: Pedir una pista.
- **3**: Limpiar el tablero.
- **4**: Finalizar el juego.

### Ingresar un numero en una celda
El formato es muy simple, se debe ingresar un numero de dos dígitos, siendo el primero el numero de la fila y el segundo el numero de la columna. Luego, se pedirá el número que se desea ingresar en la celda. Por ejemplo, si se desea ingresar el número 5 en la celda de la fila 1 y columna 2, se deberá ingresar el numero 12 primero y luego el 5. Solo se podrán ingresar números del 1 al 9 y no se podrán ingresar números en celdas que estén coloreadas de rojo.

### Pedir una pista
El jugador contara con un total de 3 pistas. Al pedir una pista, se verificará que el camino que este tomando el usuario sea correcto, o sea, que no tenga números repetidos en la misma fila, columna o cuadrante. Haya números repetidos o no, se le restara una pista al jugador. Si el jugador no tiene más pistas, se le informara que no puede pedir más pistas.

### Limpiar el tablero
Esta opción permite al jugador limpiar el tablero y empezar de nuevo.

### Finalizar el juego
Esta opción permite al jugador finalizar el juego en cualquier momento. Al finalizar el juego, se validará el tablero y se le informará si ganó o perdió.
