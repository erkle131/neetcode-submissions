class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adj_list and dst in self.adj_list[src]:
            self.adj_list[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        def dfs(curr):
            if curr == dst:
                return True
            visited.add(curr)
            for neighbor in self.adj_list.get(curr, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(src)