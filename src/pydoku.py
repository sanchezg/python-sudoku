"""
Este programa intenta ser el generador de puzzles vlidos, siguiendo el
siguiente algoritmo[1]:

PopulateBoard() 
{ 
 PopulateCell(0) 
} 

bool PopulateCell(index) 
{ 
 if (index==81 
  return true; // the board is full!! 

 // try setting each possible value in cell 
 set cellorder = {1..9} // this list contains 1..9 in a *random* order 

 for (i=0; i<9; i++) 
 { 
  // set this test value 
  set cell[index] = cellorder[i] 

  // is this board still valid? 
  if(BoardValid()) 
  { 
   // it is so try to populate next cell 
   if (PopulateCell(index+1)) 
   { 
    // if this cell returned true, then the board is valid 
    return true; 
   } 
  } 
 } 
 // rollback this cell 
 return false; 
} 

bool BoardValid() 
{ 
 // test constraints 
 if (constraintsValid) 
  return true; 
 else 
  return false; 
}
    
[1] http://www.setbb.com/sudoku/viewtopic.php?t=314

"""

__author__="Gonzalo"
__date__ ="$21/02/2012 18:56:55$"

import random

FACIL = 35
MEDIO = 50
DIFICIL = 63

class Sudoku(object):
    def __init__(self, dificultad):
        """Inicializa el board (tablero) vacio."""
        self.limpiar_board()
        self.dificultad = dificultad
        self.solucion = []
        self.puzzle = []

    def limpiar_board(self):
        """Para indicar un casillero vacio, se utiliza la convencion del foro,
        donde se explicita que un casillero vacio se representa con un punto (.)"""
        self.board = []
        for fila in xrange(9):
            self.board.append([None for i in xrange(9)])

    def print_board(self, board):
        """Funcion que imprime el board sin los corchetes y por fila"""
        miboard = []
        if board == 'b':
            # imprime el sudoku generado
            miboard = self.board
        elif board == 'p':
            # imprime el puzzle generado a partir del board
            miboard = self.puzzle
        elif board == 's':
            # imprime la solucion al puzzle realizada con el solver
            #miboard == self.solucion
            print self.solucion
            return
        for fila in miboard:
            for item in fila:
                print item,
            print ""
        print ""

    def en_fila(self, board, fila, numero):
        """Devuelve True si 'numero' se encuentra en la fila."""
        if numero in board[fila] and numero != None:
            return True
        else:
            return False

    def en_columna(self, board, col, numero):
        """Devuelve True si 'numero' se encuentra en la columna 'col'"""
        for fila in xrange(9):
            if board[fila][col] == numero and numero != None:
                return True
        return False

    def en_cuadro(self, board, f_cuadro, c_cuadro, numero):
        """Devuelve True si 'numero' se encuentra en el cuadro [f_cuadro, c_cuadro]"""
        for fila in range(3 * f_cuadro, 3 * f_cuadro + 3):
            for col in range(3 * c_cuadro, 3 * c_cuadro + 3):
                if board[fila][col] == numero and numero != None:
                    return True
        return False

    def poblar_board(self):
        """Esta funcion completa el tablero creando un sudoku con las reglas basicas (level-1)"""
        random.seed()
        col = 0
        while col < 9:
            valores_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(valores_posibles)
            fila = 0
            prueba = 0
            # Se prueban los valores por fila unas 200 veces
            while fila < 9 and prueba < 200:
                malas = 0
                parar = 0
                for elem in range(0, len(valores_posibles)):
                    if (self.en_columna(self.board, col, valores_posibles[elem]) or self.en_fila(self.board, fila, valores_posibles[elem]) or self.en_cuadro(self.board, int(round(fila / 3)), int(round(col / 3)), valores_posibles[elem])):
                        malas += 1
                # Si llegue al maximo de malas (valores que quedan por probar), tengo que reiniciar
                if malas == len(valores_posibles):
                    # limpiar todos los valores de la columna
                    for fila_t in xrange(9):
                        self.board[fila_t][col] = None
                    valores_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    parar = 1
                    fila = 0
                    prueba += 1
                if parar == 0:
                    numero = random.randint(1, 9)
                    while (self.en_columna(self.board, col, numero) or self.en_fila(self.board, fila, numero) or self.en_cuadro(self.board, int(round(fila / 3)), int(round(col / 3)), numero)):
                        random.seed()
                        numero = random.randint(1, 9)
                    # El numero no se encuentra y cumple las condiciones, entonces asignar...
                    self.board[fila][col] = numero
                    # ... y quitar de valores_posibles para esa columna
                    valores_posibles.remove(numero)
                    fila += 1
            col += 1
            if prueba == 200:
                self.limpiar_board()
                col = 0

    def solver(self, board):
        # Intenta resolver un puzzle con backtracking recursivo
        mi_puzzle = board
        try:
            # encontrar una celda vacia0
            pos = mi_puzzle.index(0)
        except ValueError:
            # se encontro una solucion
            return mi_puzzle

        for i in range(1,10):
            mi_puzzle[pos] = i
            #if self.pos_valida(mi_puzzle, pos):
            if self.posicion_valida(mi_puzzle, pos):
                # si asi como esta es valido, pasar al siguiente
                soluc = self.solver(mi_puzzle)
                if soluc:
                    return soluc

    def posicion_valida(self, puzzle, pos):
        #esta funcion comprueba si la celda dada es valida dentro del puzzle indicado
        #uso una unica funcion aca para comprobar por celda, y no por el board entero
        fila, col = divmod(pos, 9)

        v_tmp = []
        h_tmp = []
        for i in range(9):
            nv = puzzle[(i*9)+col]
            nh = puzzle[(fila*9)+i]

            if nv in v_tmp or nh in h_tmp:
                return False
            if nv:
                v_tmp.append(nv)
            if nh:
                h_tmp.append(nh)
        f_cuadro = (fila/3)*3
        c_cuadro = (col/3)*3
        tmp = []
        for i in range(3):
            for j in range(3):
                n = puzzle[(i*9)+(f_cuadro*9)+c_cuadro+j]
                if n and n in tmp:
                    return False
                if n:
                    tmp.append(n)
        return True

    def gen_puzzle(self):
        # con el board lleno genera un puzzle, vaciando celdas al azar
        # obtener posicion al azar
        self.puzzle = self.board
        i = 0
        while (i < self.dificultad):
            # esto es para dejar tantos casilleros como me defina el nivel de dificultad
            pos = int(random.randint(0, 80))
            fila, col = divmod(pos, 9)
            if self.puzzle[fila][col] != 0:
                self.puzzle[fila][col] = 0
                i = i + 1

    def puzzle_solver(self):
        # esta fucnoin intenta generar una solucion al puzzle generado
        #while self.solucion == []:
        puzzle_t = []
        for i in range(0,9):
            for j in range(0,9):
                puzzle_t.append(self.puzzle[i][j])
        #print puzzle_t
        self.solucion = self.solver(puzzle_t)

if __name__ == "__main__":
    mi_board = Sudoku(FACIL)
    mi_board.poblar_board()
    mi_board.print_board('b')
    mi_board.gen_puzzle()
    mi_board.print_board('p')
    mi_board.puzzle_solver()
    mi_board.print_board('s')
