# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="gonzalo"
__date__ ="$21/02/2012 18:56:55$"

import random

def random_list(list):
    count = len(list)
    for i in count:
        val = random.choice(list)
        list.remove(val)
        list_temp.append(val)
    return list_temp


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
        #valores_posibles = random.random()
        #random.choice([1,2,3,4,5,6,7,8,9])
        valores_posibles = [1,2,3,4,5,6,7,8,9]
        valores_random = random.shuffle(valores_posibles)
        for i in valores_posibles:
            celda[index] = valores_random[i]
            if self.board_valido():
                if self.poblar_celda(index+1):
                    return True
        celda[index] = 0    # rollback esta celda
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
    print "Hello World"
