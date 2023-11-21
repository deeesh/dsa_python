# Task is to check weather the graph contains a cycle or not
# We can use DFS Traversal 
# Based on the idea that there is a cycle there is a cycle in graph only if there is a back edge
#  (i.e a node points to one of its ancestors in graph)


class Solution:
    def isCyclic(self, V, adj):
        visited = [0] * V

        def isCyclicUtil(vertex):
            visited[vertex] = 1

            # Recurr for all neighbour vertices
            for neighbour in adj[vertex]:
                if visited[neighbour] == 0:
                    if isCyclicUtil(neighbour):
                        return True
                elif visited[neighbour] == 1:
                    return True
            visited[vertex] == 2
            return False
        # Start DFS for alll unvisited vertices
        for i in range(V):
            if visited[i] == 0:
                if isCyclicUtil(i):
                    return True
        return False






if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = list(map(int, input().strip().aplit()))
            adj[a].append(b)
        ob = Solution()
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

