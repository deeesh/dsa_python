from typing import List
class Solution:
    def dfsOfGraph(V: int, adj:List[List[int]]) -> List[int]:
        visited = [False] * V
        result = []

        def dfs(vertex):
            visited[vertex] = True
            result.append(vertex)

            for neighbours in adj[vertex]:
                if not visited[neighbours]:
                    dfs(neighbours)
        
        for i in range(V):
            if not visited[i]:
                dfs[i]
        return result


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        u, v = map(int, input())
        adj = [[] for i in range(V)]
        adj[u].append(v)
        adj[v].append(u)
    ob = Solution()
    ob.dfsOfGraph(v, adj)
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()


