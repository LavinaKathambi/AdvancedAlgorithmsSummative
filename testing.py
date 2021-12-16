# Complete the shortestReach function below.
def shortestReach(n, distanceMatrix, s):
    queue = list()
    queue.append(s)

    minDistances = [-1] * (n + 1)
    minDistances[s] = 0

    while queue:
        currentNode = queue.pop(0)

        for neighbor in distanceMatrix[currentNode]:
            newDistance = minDistances[currentNode] + distanceMatrix[currentNode][neighbor]
            prevDistance = minDistances[neighbor]
            if minDistances[neighbor] == -1:
                minDistances[neighbor] = newDistance
            else:
                minDistances[neighbor] = min(newDistance, minDistances[neighbor]) 

            if prevDistance != minDistances[neighbor]:
                queue.append(neighbor)      

    del minDistances[s]
    del minDistances[0]
    print (' '.join(map(str, minDistances)))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        distanceMatrix = [dict() for _ in range(n + 1)]
        for _ in range(m):
            edge = list(map(int, input().rstrip().split()))
            i = edge[0]
            j = edge[1]
            weight = edge[2]
            if i not in distanceMatrix[j]:
                distanceMatrix[i][j] = distanceMatrix[j][i] = weight    
            else:
                distanceMatrix[i][j] = distanceMatrix[j][i] = min(weight, distanceMatrix[i][j])

        s = int(input())

        shortestReach(n, distanceMatrix, s)

# t = 1
# n = 44
# distanceMatrix = {(1, 2):24.0,(1, 4):20.0,(3, 1):3.0,(4, 3):12.0} 

print(input(t))
print(input(n))
print(input(distanceMatrix))
print(input(s))
print(shortestReach(n,distanceMatrix,s))