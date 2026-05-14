class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        vector<int> nums1_copy = {nums1.begin(), nums1.begin() + m};
        int i = 0; // index for nums1
        int j = 0; // index for nums2
        int k = 0; // write position in nums1

        while (k < m + n) {
            // if j >= n then we've checked all vals in nums2
            if (j >= n || (i < m && nums1_copy[i] < nums2[j])) {
                nums1[k++] = nums1_copy[i++];
            } else {
                nums1[k++] = nums2[j++];
            }
        }
    }
};