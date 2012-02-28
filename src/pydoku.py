"""
    Este programa intenta ser el generador de puzzles válidos, siguiendo el
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
        """Inicia el board"""
        self.board = []
        self.poblar_board()

    def poblar_board(self):
        self.poblar_celda(0)

    def poblar_celda(self, index):
        if (index == 81):
            return True
        # probar con cada valor posible por celda
        valores_posibles = [1,2,3,4,5,6,7,8,9]
        valores_random = random.shuffle(valores_posibles)
        for i in valores_posibles:
            self.board[index] = valores_random[i]
            if self.board_valido():
                if self.poblar_celda(index+1):
                    return True
        self.board[index] = 0    # rollback esta celda
        return False

    def board_valido(self):
        if self.cumple_requisitos():
            return True
        else:
            return False

    def cumple_requisitos(self):
        return True

    def print_board(self):
        for fila in self.board:
            for item in fila:
                print item,
            print ""


if __name__ == "__main__":
    mi_board = Sudoku()
