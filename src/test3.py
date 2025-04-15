def add_3_nums(x,y,z):    
    return x + y + z

def divide_two_nums(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x / y

def pop_element_from_list(a_list):
    if a_list:
        return a_list.pop()
    return None

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

def append_element_to_list(element,list):
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

#deleted functions



def shortest_distance(graph, start_vertex):
    num_vertices = len(graph)
    distance = [float('inf')] * num_vertices
    distance[start_vertex] = 0

    for _ in range(num_vertices - 1):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] and distance[i] != float('inf') and distance[i] + graph[i][j] < distance[j]:
                    distance[j] = distance[i] + graph[i][j]
    
    return distance


def shortestPath(graph, start_vertex):    
    num_vertices = len(graph)
    distance = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        distance[i][i] = 0
        for j in range(num_vertices):
            if graph[i][j]:
                distance[i][j] = graph[i][j]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

def shortest_Path(graph, start_vertex):
    num_vertices = len(graph)
    distance =     [float('inf')] * num_vertices
    distance[start_vertex] = 0

    for _ in range(num_vertices - 1):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] and distance[i] != float('inf') and distance[i] + graph[i][j] < distance[j]:
                    distance[j] = distance[i] + graph[i][j]

    return distance


def power_of_two(x):
    if x < 0:
        return None
    result = 1
    while x > 0:
        result *= 2
        x -= 1
    return result

def greeting(name):
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"

def salutation(name, surname):
    if not name or not surname:
        return "Hello, Stranger!"
    return f"Hello, {name} {surname}!"

def number_to_string(n):
    if n < 0:
        return "Negative numbers are not supported."
    return str(n)

def number_to_word(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n == 0:
        return "zero"
    elif n < 10:
        return ones[n]
    elif n < 20:
        return teens[n-10]
    elif n < 100:
        return tens[n//10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    elif n < 1000:
        return ones[n//100] + " hundred" + (" and " + number_to_word(n % 100) if n % 100 != 0 else "")
    else:
        return "Number out of range"
    

#create a function that solves the tsp
def solve_tsp(graph):
    num_vertices = len(graph)
    all_visited = (1 << num_vertices) - 1
    dp = [[float('inf')] * num_vertices for _ in range(1 << num_vertices)]

    # Start at each node
    for i in range(num_vertices):
        dp[1 << i][i] = 0

    # Iterate over all subsets of nodes
    for mask in range(1 << num_vertices):
        for u in range(num_vertices):
            if mask & (1 << u):
                # Try to find a shorter path to each node v from u
                for v in range(num_vertices):
                    if not mask & (1 << v) and graph[u][v]:
                        next_mask = mask | (1 << v)
                        dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + graph[u][v])

    # Find the minimum cost to return to the start node
    min_cost = float('inf')
    for i in range(num_vertices):
        if graph[i][0]:
            min_cost = min(min_cost, dp[all_visited][i] + graph[i][0])

    return min_cost if min_cost < float('inf') else None


def quickSort(arr):
    # Function to sort an array using the Quick Sort algorithm
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)
    

