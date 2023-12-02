# DSA GfG

from typing import List
from queue import Queue

class Solution:
    def bfsOfGraph(V:int, adj:List[List[int]]) -> List[int]:
        
        visited = [False]*V
        result = []

        queue = Queue()
        queue.put(0)

        while not queue.empty():
            u = queue.get()
            result.append(u)

            for v in adj[u]:
                if not visited[v]:
                    queue.put(v)
                    visited[v] = True
        return result



if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for [] in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
            print()