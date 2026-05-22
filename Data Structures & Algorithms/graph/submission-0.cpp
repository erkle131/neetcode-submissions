class Graph {
    unordered_map<int, unordered_set<int>> adjList;

public:
    Graph() : adjList() {}

    void addEdge(int src, int dst) {
        adjList[src].insert(dst);
        if (adjList.find(dst) == adjList.end()) {
            adjList[dst] = {};
        }
    }

    bool removeEdge(int src, int dst) {
        if (adjList.count(src) && adjList[src].count(dst) == 1) {
            adjList[src].erase(dst);
            return true;
        }
        return false;
    }

    bool hasPath(int src, int dst) {
        return bfs(src, dst, adjList);
    }

    bool bfs(int src, int dst, unordered_map<int, unordered_set<int>>& adjList) {
        unordered_set<int> visit;
        queue<int> queue;
        visit.insert(src);
        queue.push(src);

        while (queue.size()) {
            int queueLength = queue.size();
            for (int i = 0; i < queueLength; i++) {
                int cur = queue.front();
                queue.pop();
                if (cur == dst) {
                    return true;
                }
    
                for (int neighbor : adjList[cur]) {
                    if (visit.count(neighbor) == 0) {
                        visit.insert(neighbor);
                        queue.push(neighbor);
                    }
                }
            }
        }
        return false;
    }
};