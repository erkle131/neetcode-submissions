class LinkedList {
private:
    struct Node {
        int data;
        Node* next;
        Node(int val) : data(val), next(nullptr) {}
    };

    Node* head;
    Node* tail;

public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    ~LinkedList() {
        Node* curr = head;
        while (curr) {
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }

    int get(int index) {
        Node* curr = head;
        int i = 0;
        while (curr != nullptr) {
            if (i == index) {
                return curr->data;
            }
            curr = curr->next;
            i++;
        }
        return -1;
    }

    void insertHead(int val) {
        Node* curr = new Node(val);
        curr->next = head;
        head = curr;
        if (!tail) tail = curr;
    }
    
    void insertTail(int val) {
        Node* curr = new Node(val);
        if (!tail) { // empty list
            head = tail = curr;
        } else {
            tail->next = curr;
            tail = curr;
        }
    }

    bool remove(int index) {
        if (!head) return false;

        if (index == 0) {
            Node* toDel = head;
            head = head->next;
            delete toDel;
            if (!head) tail = nullptr; // list became empty
            return true;
        }

        Node* curr = head;
        int i = 0;
        while (curr != nullptr && curr->next != nullptr) {
            if (i == (index - 1)) {
                Node* toDel = curr->next;
                curr->next = toDel->next;
                if (toDel == tail) tail = curr;
                delete toDel;
                return true;
            }
            curr = curr->next;
            i++;
        }

        return false;
    }

    vector<int> getValues() {
        vector<int> values;

        Node* curr = head;
        while (curr != nullptr) {
            values.push_back(curr->data);
            curr = curr->next;
        }

        return values;
    }
};
