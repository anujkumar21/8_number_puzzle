""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 
"""
import pygame


class HighlightDigit:
    def __init__(self, screen):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.screen = screen

        self.highlight_x = 100
        self.highlight_y = 100
        self.highlight_side = 100

        self.hfont = pygame.font.SysFont('Segoe Print', 30)
        self.highlight_digit = pygame.draw.rect(self.screen, self.white,
                                                [self.highlight_x, self.highlight_y, self.highlight_side,
                                                 self.highlight_side], 5)
        self.index = 0
        self.m_count = 0

    def highlight_digit_to_be_swapped(self, x, y, key, puzzle):
        # print self.highlight_digit
        # print "(%d,%d)" % (self.highlight_digit.y / 100, self.highlight_digit.x / 100 - 1)
        self.index = ((self.highlight_digit.y / 100) * 3 + (self.highlight_digit.x / 100 - 1))
        # print "(%d)" % self.index

        self.highlight_x = self.highlight_digit.x + x
        self.highlight_y = self.highlight_digit.y + y

        if self.highlight_x < 400 and self.highlight_x >= 100 and self.highlight_y >= 98 and self.highlight_y < 300:
            self.screen.fill(self.black)
            self.highlight_digit = self.highlight_digit.move(x, y)
            pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
            if key == "LEFT":
                return self.swap(self.index, self.index - 1, puzzle)
            elif key == "RIGHT":
                return self.swap(self.index, self.index + 1, puzzle)
            elif key == "UP":
                return self.swap(self.index, self.index - 3, puzzle)
            elif key == "DOWN":
                return self.swap(self.index, self.index + 3, puzzle)
            else:
                print ":)"
        return False

    def swap(self, index, index2, puzzle):
        # # print "SWAP: (%d,%d) - %s" % (index, index2, puzzle)
        if puzzle[index2] == 9:
            temp = puzzle[index]
            puzzle[index] = puzzle[index2]
            puzzle[index2] = temp
            self.m_count += 1
            # self.move_count(self.m_count)
            print "SWAP: %s" % puzzle
        self.move_count("Moves: %s" % str(self.m_count))
        print "COMPARISON: %s" % (puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 9])
        if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print "You Win !!!"
            return True
        else:
            print ""

        return False

    def move_count(self, text, x=50, y=400):
        try:
            self.hfont.render(text, True, self.white)
            self.htextsurface = self.hfont.render(text, True, self.white)
            self.screen.blit(self.htextsurface, (x, y))

        except Exception, e:
            # print 'Font Error, saw it coming'
            raise e
