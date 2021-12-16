# PYTHON CODE FOR FINDING THE SHORTEST REACH IN A GRAPH
def shortestReach(numOfNodes, edges, startNode):
    # Initialize a queue to keep track of distances between edges
    queue = list()
    # add the first node to the empty queue
    queue.append(startNode)
    # calculate the minimum distances between each node
    minDistance = [-1] * (numOfNodes + 1)
    minDistance[startNode] = 0
    # loop through the queue and pop the last element
    while queue:
        currentNode = queue.pop(0)
        # iterate over the elements and check the next node
        for nextNode in edges[currentNode]:
            # Assign the new distance as the current shortest distance
            newDistance = minDistance[currentNode] + edges[currentNode][nextNode]
            prevDistance = minDistance[nextNode]
            # Check if ther is an unreachable node and assign distance to -1
            if minDistance[nextNode] == -1:
                minDistance[nextNode] = newDistance
            else:
                minDistance[nextNode] = min(newDistance, minDistance[nextNode]) 
            # append updated distance to the queue 
            if prevDistance != minDistance[nextNode]:
                queue.append(nextNode)
    # delete min distance for start node      
    del minDistance[startNode]
    del minDistance[0]
    # return an array of shortest distance to each node
    print (' '.join(map(str, minDistance)))
    