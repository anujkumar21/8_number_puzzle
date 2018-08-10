"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date:
"""
import math
import random
from copy import deepcopy


class Node:
    def __init__(self, parent, puzzle, cost):
        self.parent = parent
        self.puzzle = puzzle
        self.children = []
        self.cost = cost

    def sort_children(self):

        size = len(self.children)

        for i in range(0, size):
            for j in range(i + 1, size):
                if self.children[i].cost < self.children[j].cost:
                    temp = self.children[i]
                    self.children[i] = self.children[j]
                    self.children[j] = temp

        for i in range(0, size - 1):
            if self.children[i].cost == self.children[i + 1].cost:

                if self.calculate_manhattan(self.children[i].puzzle) < self.calculate_manhattan(
                        self.children[i + 1].puzzle):
                    temp = self.children[i]
                    self.children[i] = self.children[i + 1]
                    self.children[i + 1] = temp

    def get_less(self, puzzle):
        count = 0
        for i in range(0, len(puzzle)):
            for j in range(i, len(puzzle)):
                if puzzle[i] > puzzle[j] and puzzle[i] != 9:
                    count += 1

        return count

    def calculate_manhattan(self, puzzle):
        # print "PUZZLE: %s" % puzzle
        sum = 0
        for i in range(0, len(puzzle)):
            if puzzle[i] != 9:
                act_pos = self.get_actual_position(i)
                exp_pos = self.get_expected_position(puzzle[i])
                to_reach = self.path_to_reach(act_pos, exp_pos)
                # print puzzle[i], act_pos, exp_pos, to_reach
                sum += to_reach
        return sum

    def get_actual_position(self, i):
        row = i / 3
        col = i % 3
        return (row, col)

    def get_expected_position(self, num):

        num = num - 1
        row = num / 3
        col = num % 3
        # print (row,col)
        return (row, col)

    def path_to_reach(self, act_pos, exp_pos):

        row_diff = math.fabs(act_pos[0] - exp_pos[0])
        col_diff = math.fabs(act_pos[1] - exp_pos[1])
        # print "row-diff: %d" % row_diff
        # print "col-diff: %d" % col_diff
        to_reach = int(row_diff + col_diff)
        return to_reach


class Solution:
    def __init__(self, puzzle):
        print "SOLUTION"
        self.puzzle = puzzle
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.open_stack = []
        self.closed_stack = []
        self.sol_stack = []

    def solution(self):
        root = Node(None, self.puzzle, 0)

        self.open_stack.append(root)
        itr = 0
        while len(self.open_stack) != 0:
            last_index = len(self.open_stack) - 1
            curr_node = self.open_stack[last_index]

            self.closed_stack.append(self.open_stack[last_index])
            self.open_stack.remove(self.open_stack[last_index])
            if curr_node.puzzle == self.goal:
                print "goal"
                path_node = curr_node
                # self.sol_stack.append(curr_node.puzzle)
                while path_node.parent is not None:
                    self.sol_stack.append(path_node.puzzle)
                    path_node = path_node.parent

                print "Sol path: %d" % len(self.sol_stack)
                print "Sol path: %s" % self.sol_stack
                break
            possible_children = self.possible_moves(curr_node.puzzle)
            for t_child in possible_children:
                if self.should_be_added(t_child[0]):
                    child = Node(curr_node, t_child[0], t_child[1])
                    curr_node.children.append(child)
            curr_node.sort_children()
            for child in curr_node.children:
                self.open_stack.append(child)
            itr += 1

    def should_be_added(self, puzzle):

        is_present_in_open_stack = False
        for node in self.open_stack:
            if puzzle == node.puzzle:
                is_present_in_open_stack = True
                break

        is_present_in_closed_stack = False
        for node in self.closed_stack:
            if puzzle == node.puzzle:
                is_present_in_closed_stack = True
                break

        if not is_present_in_open_stack and not is_present_in_closed_stack:
            return True
        return False

    def possible_moves(self, puzzle):

        index = puzzle.index(9)
        row = index / 3
        col = index % 3
        moves = [1, -1, -1, 1]
        x = 0
        possible_indexs = []
        for i in moves:
            si = -1
            if x % 2 == 0:
                if row + i >= 0 and row + i <= 2:
                    si = (row + i) * 3 + col
            else:
                if col + i >= 0 and col + i <= 2:
                    si = row * 3 + (col + i)
            x += 1
            if si >= 0 and si <= 8:
                possible_indexs.append(si)

        temp = []

        if puzzle[0] == 1 and puzzle[1] == 2 and puzzle[2] == 3:
            for i in possible_indexs:
                if i >= 0 and i <= 2:
                    possible_indexs.remove(i)
        if puzzle[0] == 1 and puzzle[3] == 4 and puzzle[6] == 7:
            for i in possible_indexs:
                if i % 3 == 0:
                    possible_indexs.remove(i)

        for i in possible_indexs:
            p = self.swap_with_blank(deepcopy(puzzle), index, i)
            temp.append(p)
        return temp

    def swap_with_blank(self, puzzle, i, j):

        temp = puzzle[i]
        puzzle[i] = puzzle[j]
        puzzle[j] = temp
        if random.randint(1, 3) == 1:
            cost = self.calculate_cost(puzzle)
        else:
            cost = self.get_less(puzzle)
        if not self.get_less(puzzle) % 2 == 0:
            print "************ NOT SOLVABLE **************"

        return (puzzle, cost)

    def calculate_cost(self, puzzle):
        count = 0
        for i, j in zip(self.goal, puzzle):
            if i != j and j != 9:
                count += 1
        return count

    def get_less(self, puzzle):
        count = 0
        for i in range(0, len(puzzle)):
            for j in range(i, len(puzzle)):
                if puzzle[i] > puzzle[j] and puzzle[i] != 9:
                    count += 1

        return count
