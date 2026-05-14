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
    vector<Pair> quickSort(vector<Pair>& pairs) {
        if (pairs.empty()) return pairs;
        return quickSort(pairs, 0, pairs.size() - 1);
    }


    vector<Pair> quickSort(vector<Pair>& pairs, int s, int e) {
        if (e - s + 1 <= 1) {
            return pairs;
        }

        Pair pivot = pairs[e];
        int left = s;

        for (int i = s; i < e; i++) {
            if (pairs[i].key < pivot.key) {
                Pair temp = pairs[left];
                pairs[left] = pairs[i];
                pairs[i] = temp;
                left++;
            }
        }

        pairs[e] = pairs[left];
        pairs[left] = pivot;

        quickSort(pairs, s, left - 1);
        quickSort(pairs, left + 1, e);

        return pairs;
    }
};
