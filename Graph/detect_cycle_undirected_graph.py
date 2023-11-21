

class Solution:
    def isCyclic(self, V, adj):
        visited= [False] * V
        parent = [-1] * V

        def isCyclicUtil(vertex):
            visited[vertex] = True

            for neighbour in adj[vertex]:
                if not visited[neighbour]:
                    parent[neighbour] = vertex
                    if isCyclicUtil(neighbour):
                        return True
                elif parent[vertex] != neighbour:
                    return True
            return False

        for i in range(V):
            if not visited[i]:
                if isCyclicUtil(i):
                    return True

        return False 





if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        ob = Solution()
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)


