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

    def __init__(self, tamanio):
        """Inicia el board"""
        self.board = [None for i in xrange(tamanio*tamanio)]
        self.poblar_board()

    def poblar_board(self):
        self.poblar_celda(0)

    def poblar_celda(self, index):
        if (index == 81):
            return True
        # probar con cada valor posible por celda
        valores_posibles = [1,2,3,4,5,6,7,8,9]
        random.shuffle(valores_posibles)
        for i in xrange(len(valores_posibles)):
            self.board[index] = valores_posibles[i]
            if self.board_valido():
                if self.poblar_celda(index+1):
                    return True
        self.board[index] = 0    # rollback esta celda
        return False

    def board_valido(self):
    	for celda in xrange(len(self.board)):
    		 if self.en_fila(celda) or self.en_columna(celda) or self.en_cuadro(celda):
    		 	return False
        return True

    # Para que se cumpla la condicion de que no esten en la misma fila, hay que verificar que:
    # 1) filas iguales
    # 2) datos iguales
    # 3) haya datos
    def en_fila(self, celda):
	for pos in xrange(len(self.board)):
		if int(pos/9) == int(celda/9) and self.board[pos] == self.board[celda] and pos != celda and self.board[pos] != None:
			return True
        return False

    # Para que se cumpla la condicion de que no esten en la misma columna, hay que verificar que:
    # 1) columnas iguales
    # 2) datos iguales
    # 3) haya datos
    def en_columna(self, celda):
	for pos in xrange(len(self.board)):
            if pos % 9 == celda % 9 and self.board[pos] == self.board[celda] and pos != celda and self.board[pos] != None:
                return True
	return False

    # Para que se cumpla la condicion de que no esten en el mismo recuadro, hay que verificar que:
    # 1) recuadros iguales
    # 2) datos iguales
    # 3) haya datos
    def en_cuadro(self, celda):
        for pos in xrange(len(self.board)):
            if self.cuadro(pos) == self.cuadro(celda) and self.board[pos] == self.board[celda] and celda != pos and self.board[pos] != None:
                return True
        return False

    def fila(self, celda):
	return int(celda/9)
		
    def columna(self, celda):
	return celda%9
		
    def cuadro(self, celda):
	return (int(self.fila(celda)/3), self.columna(celda)%3)
	
    def print_board(self):
        for fila in self.board:
            print fila
            print ""


if __name__ == "__main__":
    mi_board = Sudoku(9)
    mi_board.print_board()
