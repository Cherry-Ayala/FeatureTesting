def shortestPath(graph, start, end):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        
        unseenNodes.pop(minNode)
        
    currentNode = end
    
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return None
    
    path.insert(0, start)
    
    return path

def PathDistances(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {}
    unvisited = set(graph)

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        if distances[current_node] == float('inf'):
            break

        for neighbor, weight in graph[current_node].items():
            alt_route = distances[current_node] + weight
            if alt_route < distances[neighbor]:
                distances[neighbor] = alt_route
                predecessors[neighbor] = current_node

    shortest_path = []
    node = end
    while node != start:
        shortest_path.insert(0, node)
        node = predecessors.get(node, None)
        if node is None:
            return None, float('inf')  # No path found
    shortest_path.insert(0, start)

    longest_distance = 0
    longest_path = []
    for node in graph:
        if distances[node] != float('inf'):
            temp_path = []
            temp_node = node
            while temp_node != start:
                temp_path.insert(0, temp_node)
                temp_node = predecessors.get(temp_node, None)
                if temp_node is None:
                    break
            temp_path.insert(0, start)
            if len(temp_path) > 1 and distances[node] > longest_distance:
                longest_distance = distances[node]
                longest_path = temp_path

    return shortest_path, longest_distance

def mostConnectedNode(graph):
    # Function to find the most connected node in a graph
    max_connections = 0
    most_connected_node = None
    
    for node, edges in graph.items():
        connections = len(edges)
        if connections > max_connections:
            max_connections = connections
            most_connected_node = node
            
    return most_connected_node, max_connections

#make a class that receives a graph and a given node, it calls the function 'mostConnectedNode' to find it, and uses the function 'PathDistances' using the given node as the start, the result from 'mostConnectedNode' as end, and it should return the shortest and longest path that are returned by 'PathDistances'
