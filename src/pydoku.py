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
        #self.board = [1,2,3,4,5,6,7,8,9,4,5,6,7,8,9,1,2,3,7,8,9,1,2,3,4,5,6,2,3,4,5,6,7,8,9,1,5,6,7,8,9,1,2,3,4,8,9,1,2,3,4,5,6,7,3,4,5,6,7,8,9,1,2,6,7,8,9,1,2,3,4,5,9,1,2,3,4,5,6,7,8]

    def poblar_board(self):
        self.poblar_celda(0)

    def poblar_celda(self, index):
        if (index == 10):
            return True
        # probar con cada valor posible por celda
        valores_posibles = [1,2,3,4,5,6,7,8,9]
        # el shuffle es para que cada celda pruebe con los valores en distinto orden
        random.shuffle(valores_posibles)
        for i in xrange(len(valores_posibles)):
            self.board[index] = valores_posibles[i]
            if self.board_valido():
                if self.poblar_celda(index+1):
                    return True
        self.board[index] = None    # rollback esta celda
        return False

    # Esta funcion se encarga de definir si el board asi como esta es valido.
    # Para esto, recorre las 81 celdas, y por cada Ci verifica:
    # 1) Que Ci no se repita en la misma columna
    # 2) Que Ci no se repita en la misma fila
    # 3) Que Ci no se repita dentro del mismo recuadro.
    # Si estas condiciones son validas, se retorna un True.
    def board_valido(self):
    	for celda in xrange(len(self.board)):
            if self.en_fila(celda) or self.en_columna(celda) or self.en_cuadro(celda):
                return False
        return True

    # Para que se cumpla la condicion de que no esten en la misma fila, hay que verificar que:
    # 1) filas iguales
    # 2) datos iguales
    # 3) haya datos
    # index especifica la posicion del nuevo dato ingresado
    # celda especifica la posicion del dato contra el cual hay que verificar
    def en_fila(self, celda):
        fila = int(celda/9)
        for index in xrange(len(self.board)):
            if int(index/9) == fila:
                if celda != index:
                    if self.board[index] == self.board[celda]:
                        return True
        return False

    # Para que se cumpla la condicion de que no esten en la misma columna, hay que verificar que:
    # 1) columnas iguales
    # 2) datos iguales
    # 3) haya datos
    def en_columna(self, celda):
        columna = celda % 9
        for index in xrange(len(self.board)):
            if index%9 == columna:
                if celda != index:
                    if self.board[celda] == self.board[index]:
                        return True
	return False

    # Para que se cumpla la condicion de que no esten en el mismo recuadro, hay que verificar que:
    # 1) recuadros iguales
    # 2) datos iguales
    # 3) haya datos
    def en_cuadro(self, celda):
        recuadro = self.cuadro(celda)
        for index in xrange(len(self.board)):
            if recuadro == self.cuadro(index):
                if index != celda:
                    if self.board[celda] == self.board[index]:
                        return True
        return False

    def fila(self, celda):
	return int(celda/9)
		
    def columna(self, celda):
	return celda%9
		
    def cuadro(self, celda):
	return (int(self.fila(celda)/3), self.columna(celda)%3)
	
    def print_board(self):
        print self.board


if __name__ == "__main__":
    mi_board = Sudoku(9)
#    if mi_board.board_valido():
    mi_board.print_board()
