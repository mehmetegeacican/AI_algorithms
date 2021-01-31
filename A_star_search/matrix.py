from a_star import *
import random

#FOR DEMONSTRATION
matrix = [
          ["1","2","3"],
          ["4","5","6"],
          ["7","8","-"]
          ]


def print_matrix_values(matrix):
    for row in matrix:
        print(row)

def set_matrix_values(number_order):

    row_1 = [number_order[0],number_order[1],number_order[2]]
    row_2 = [number_order[3],number_order[4],number_order[5]]
    row_3 = [number_order[6],number_order[7],number_order[8]]

    matrix = [row_1,row_2,row_3]

    return matrix

def get_matrix_values(matrix):
    string_value = ""
    for row in matrix:
        for x in range(len(row)):
            string_value += row[x] 
    return str(string_value)



if __name__ == "__main__":

    goal_1 = "12345678-"
    num = list(goal_1)
    random.shuffle(num)
    result = ''.join(num)
    start_1 = str(result)

    print("Starting")
    a = A_Star_Solver(start_1,goal_1)
    a.solve()
    for i in range(len(a.path)):
        x = a.path[i]
        print("Step",i,")",a.path[i])
        matrice = set_matrix_values(x)
        print_matrix_values(matrice)
        
