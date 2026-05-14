class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Assuming array only contains 0, 1, or 2
        int counts[] = {0, 0 ,0};

        // Count the quantity of each val in nums
        for (int n: nums) {
            counts[n]++;
        }

        int i = 0;
        for (int n = 0; n < 3; n++) {
            for (int j = 0; j < counts[n]; j++) {
                nums[i] = n;
                i++;
            }
        }
    }
};