class DynamicArray {
private:
    int* arr;
    int length;
    int capacity;

public:

    DynamicArray(int cap) : length(0), capacity(cap) {
        arr = new int[cap];
    }

    ~DynamicArray() {
        delete[] arr;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (length == capacity) {
            resize();
        }
        arr[length++] = n;
    }

    int popback() {
        return arr[--length];
    }

    void resize() {
        capacity = 2 * capacity;
        int* newArray = new int[capacity];
        
        for (int i = 0; i < length; i++) {
            newArray[i] = arr[i];
        }
        arr = newArray;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
