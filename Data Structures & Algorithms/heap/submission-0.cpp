class MinHeap {
private:
    vector<int> minHeap;

public:
    MinHeap() {
        minHeap.push_back(0);
    }

    void push(int val) {
        minHeap.push_back(val);
        int i = minHeap.size() - 1;

        // percolate up
        while (i > 1 && minHeap[i] < minHeap[i / 2]) {
            int tmp = minHeap[i];
            minHeap[i] = minHeap[i / 2];
            minHeap[i / 2] = tmp;
            i = i / 2;
        }
    }

    void percolateDown(vector<int>& arr, int start) {
        int i = start;
        while (2 * i < arr.size()) {
            if (2 * i + 1 < arr.size() &&
            arr[2 * i + 1] < arr[2 * i] &&
            arr[i] > arr[2 * i + 1]) {
                // Swap right child
                int tmp = arr[i];
                arr[i] = arr[2 * i + 1];
                arr[2 * i + 1] = tmp;
                i = 2 * i + 1;
            } else if (arr[i] > arr[2 * i]) {
                // Swap left child
                int tmp = arr[i];
                arr[i] = arr[2 * i];
                arr[2 * i] = tmp;
                i = 2 * i;
            } else {
                break;
            }
        }
    }

    int pop() {
        if (minHeap.size() <= 1) return -1;

        if (minHeap.size() == 2) {
            int res = minHeap[minHeap.size() - 1];
            minHeap.pop_back();
            return res;
        }

        int res = minHeap[1];
        // Move last value to root
        minHeap[1] = minHeap[minHeap.size() - 1];
        minHeap.pop_back();
        int i = 1;
        percolateDown(minHeap, i);
        return res;
    }

    int top() {
        if (minHeap.size() <= 1) return -1;
        return minHeap[1];
    }

    void heapify(const vector<int>& arr) {
        minHeap.clear();
        minHeap.push_back(0);
        for (int x : arr) minHeap.push_back(x);

        int cur = (minHeap.size() - 1) / 2;
        while(cur > 0) {
            percolateDown(minHeap, cur);
            cur--;
        }
    }
};