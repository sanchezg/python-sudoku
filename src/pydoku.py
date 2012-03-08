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

class Sudoku(object):

    def __init__(self):
        """Inicializa el board (tablero) vacio."""
        self.limpiar_board()

    def limpiar_board(self):
        """Para indicar un casillero vacio, se utiliza la convencion del foro,
        donde se explicita que un casillero vacio se representa con un punto (.)"""
        self.board = []
        for fila in xrange(9):
            self.board.append([None for i in xrange(9)])

    def print_board(self):
        """Funcion que imprime el board sin los corchetes y por fila"""
        for fila in self.board:
            for item in fila:
                print item,
            print ""

    def en_fila(self, fila, numero):
        """Devuelve True si 'numero' se encuentra en la fila."""
        if numero in self.board[fila] and numero != None:
            return True
        else:
            return False

    def en_columna(self, col, numero):
        """Devuelve True si 'numero' se encuentra en la columna 'col'"""
        for fila in xrange(9):
            if self.board[fila][col] == numero and numero != None:
                return True
        return False

    def en_cuadro(self, f_cuadro, c_cuadro, numero):
        """Devuelve True si 'numero' se encuentra en el cuadro [f_cuadro, c_cuadro]"""
        for fila in range(3 * f_cuadro, 3 * f_cuadro + 3):
            for col in range(3 * c_cuadro, 3 * c_cuadro + 3):
                if self.board[fila][col] == numero and numero != None:
                    return True
        return False

#    def poblar_board(self, index):
#        if index == 81:
#            return True
#
#        valores_posibles = [1,2,3,4,5,6,7,8,9]
#        random.shuffle(valores_posibles)
#        test_board = self.board
#
#        for i in xrange(9):
#            test_board[int(index/9)][index%9] = valores_posibles[i]
#            if (self.en_fila(int(index/9), valores_posibles[i]) == False) and (self.en_columna(index%9, valores_posibles[i]) == False) and (self.en_cuadro(int(round(int(index/9))/3), int(round((index%9)/3)), valores_posibles[i]) == False):
#		self.board[int(index/9)][index%9] = test_board[int(index/9)][index%9]
#                if (self.poblar_board(index+1) == True):
#                    return True
#        self.board[int(index/9)][index%9] = None
#        return False

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
                    if (self.en_columna(col, valores_posibles[elem]) or self.en_fila(fila, valores_posibles[elem]) or self.en_cuadro(int(round(fila / 3)), int(round(col / 3)), valores_posibles[elem])):
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
                    while (self.en_columna(col, numero) or self.en_fila(fila, numero) or self.en_cuadro(int(round(fila / 3)), int(round(col / 3)), numero)):
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

#    def puzzle_solver(self):
        # candidatos es una matriz triple con una lista de candidatos por conjunto de fila-columna.
#        self.candidatos = [[[1,2,3,4,5,6,7,8,9] for i in xrange(9)] for j in xrange(9)]
#        tiene_solucion = True
#        while tiene_solucion ==  True:
#            for fila in xrange(9):
#                for col in xrange(9):
#                    if len(self.candidatos[fila][col]) == 1:
                        # si hay un unico valor para esa celda, entonces es seguro que va ahi, sacarlos de las demas celdas
#                        self.board[fila][col] == int(self.candidatos[fila][col])
#                        for fila_t in xrange(9):
#                            self.candidatos[fila_t][col].remove(self.board[fila][col])
#                        for col_t in xrange(9):
#                            self.candidatos[fila][col_t].remove(self.board[fila][col])
#        return

#    def crear_puzzle(self, index):
#        fila = random.randint(1,9)
#        col = random.randint(1,9)

#        while 



if __name__ == "__main__":
    mi_board = Sudoku()
    mi_board.poblar_board(0)
    mi_board.print_board()
