def dijkstras(start, end, graph):

    '''
    In this algorithm, we're trying to find the shortest distance
    between two nodes on a graph. This is a directed graph represented
    as an adjacency matrix. I'm assumming all weights are positive. 

    The algorithm is essentially:
        - mark all tentative distances as infinity, except where we start (which is 0)
        - make sure to keep track of visited and unvisited nodes
        - calculate actual distance, and if actual distance is < tentative, 
          replace the tentative distance with the actual distance
        - move to the next node that is the least distance from start, 
          and is also unvisited
        - stop once we're at the target node, then break and just return
          what the tentative distance to that node was, since it's the shortest path
    '''

    # keep track of what we've visited so we don't
    # end up in a cycle

    visited = set()
    unvisited = set()
    current = start
    tentative_distances = {}

    # set up tentative distances, default infinity
    for i in range(len(graph)):
        tentative_distances[i] = float('inf')
        unvisited.add(i)
        print (unvisited)
    
    # distance from start to start is 0
    tentative_distances[start] = 0
  
    current = start 
    # keep looping until we've found the end
    while True:
        visited.add(current)
        unvisited.discard(current)

        # loop through neighbors
        for i in range(len(graph)):
            # we haven't visited it yet nor is it unconnected, update it
            if i not in visited and graph[current][i] != None:
                # if we've found a shorter path to it, update our distance
                if tentative_distances[i] >= tentative_distances[current] + graph[current][i]:
                    tentative_distances[i] = tentative_distances[current] + graph[current][i]

        # now visit the next shortest unvisited node and repeat
        for i in unvisited:
            temp_min = float('inf')
            if tentative_distances[i] <= temp_min:
                temp_min = tentative_distances[i]
        
        current = temp_min

        if current == end:
            break

    return tentative_distances[end]
  


if __name__ == "__main__":
    # graph source = http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/weighted.html

    graph1 = [[None, 3, None, 2, None, None, None, None, 4],
    [3, None, None, None, None, None, None, 4, None],
    [None, None, None, 6, None, 1, None, 2, None],
    [2, None, 6, None, 1, None, None, None, None],
    [None, None, None, 1, None, None, None, None, 8],
    [None, None, 1, None, None, None, 8, None, None],
    [None, None, None, None, None, 8, None, None, None],
    [None, 4, 2, None, None, None, None, None, None],
    [4, None, None, None, 8, None, None, None, None],
    ]

    print('shortest from 8 to 1 should be 7')
    print(' our answer is', dijkstras(8, 1, graph1))
    print('shortest from 8 to 5 should be 13')
    print(' our answer is', dijkstras(8, 5, graph1))



    
