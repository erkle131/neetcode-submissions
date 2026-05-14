// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    void merge(vector<Pair>& pairs, int s, int m, int e) {
        // Copy the sorted left & right halfs to temporary arrays
        vector<Pair> L = {pairs.begin() + s, pairs.begin() + m + 1};
        vector<Pair> R = {pairs.begin() + m + 1, pairs.begin() + e + 1};

        int i = 0; // index for L
        int j = 0; // index for R
        int k = s; // index for pairs

        while (i < L.size() && j < R.size()) {
            if (L[i].key <= R[j].key) {
                pairs[k] = L[i++];
            } else {
                pairs[k] = R[j++];
            }
            k++;
        }

        // One of the halfs will have elements remaining.
        while (i < L.size()) {
            pairs[k++] = L[i++];
        }

        while (j < R.size()) {
            pairs[k++] = R[j++];
        }
    }

    vector<Pair> mergeSort(vector<Pair>& pairs) {
        if (pairs.empty()) return pairs;
        return mergeSort(pairs, 0, pairs.size() - 1);
    }

    vector<Pair> mergeSort(vector<Pair>& pairs, int s, int e) {
        if (e - s + 1 <= 1) {
            return pairs;
        }

        // The middle index of the array
        int m = (s + e) / 2;

        // Sort the left half
        mergeSort(pairs, s, m);

        // Sort the right half
        mergeSort(pairs, m + 1, e);

        // Merge sorted halfs
        merge(pairs, s, m, e);

        return pairs;
    }
};
