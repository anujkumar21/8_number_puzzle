""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 
"""
import random

from game.digit_sqr import DigitSqr


class GeneratePuzzle:
    def __init__(self, screen):
        self.screen = screen
        self.digits = []
        self.generate_puzzle()

    def generate_puzzle(self):
        del self.digits[:]
        while len(self.digits) != 9:
            num = random.randint(1, 9)
            if num not in self.digits:
                self.digits.append(num)
        print self.digits
        if not self.is_solvable(self.digits) % 2 == 0:
            print "re-generating"
            self.generate_puzzle()

        return self.digits

    def draw_puzzle(self, digits):
        counter_x = 1
        counter_y = 1
        puzzle = []
        for digit in digits:
            puzzle.append(DigitSqr(self.screen, digit, 100 * counter_x, 100 * counter_y))
            counter_x += 1
            if counter_x % 4 == 0:
                counter_x = 1
                counter_y += 1

        return puzzle

    def is_solvable(self, digit):
        count = 0
        for i in range(0, 9):
            for j in range(i, 9):
                if digit[i] > digit[j] and digit[i] != 9:
                    count += 1

        return count
