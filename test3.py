def add_3_nums(x,y,z):    
    return x + y + z


def floyd_warshall_algorithm(graph):
    num_vertices = len(graph)
    distance = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j]:
                distance[i][j] = graph[i][j]
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    
    return distance

def appen_element_to_list(element,list):
    list.append(element)
    return list

def squareRoot(x):
    iteration_limit = 100
    guess = x / 2.0

    for _ in range(iteration_limit):
        better_guess = (guess + x / guess) / 2
        if abs(better_guess - guess) < x * 1e-10:
            return better_guess
        guess = better_guess

    return guess


def sum_of_two_nums(x,y):
    result = x+y
    return result

def x_minus_y(x,y):
    if y<x:
        return x-y
    else:        return y - x

