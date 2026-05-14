class Deque {
private:
    struct Node {
    public:
        int data;
        Node* prev;
        Node* next;

        Node(int data, Node* prev = nullptr, Node* next = nullptr)
            : data(data), prev(prev), next(next) {}
    };

    Node* head;
    Node* tail;

public:
    Deque() {
        head = nullptr;
        tail = nullptr;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    void append(int value) {
        if (tail != nullptr) { // Queue isn't empty
            tail->next = new Node(value, tail, nullptr);
            tail = tail->next;
        } else { // Queue is empty
            head = tail = new Node(value, nullptr, nullptr);
        }
    }

    void appendleft(int value) {
        Node* newNode = new Node(value, nullptr, head);
        if (head != nullptr) head->prev = newNode;
        head = newNode;
        if (tail == nullptr) tail = newNode;
    }

    int pop() {
        if (tail == nullptr) return -1;

        Node* temp = tail;
        int val = temp->data;
        tail = tail->prev;
        if (tail) tail->next = nullptr;
        else head = nullptr;

        delete temp;
        return val;
    }

    int popleft() {
        if (isEmpty()) return -1;

        Node* temp = head;
        int val = temp->data;
        head = head->next;
        if (head) head->prev = nullptr;
        else tail = nullptr;

        delete temp;
        return val;
    }
};
