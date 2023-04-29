class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> ans;
        int n=nums.size();
        int mid= n/2;
        int i=0;
        int j=mid+1;

        while(i<=mid && j<n){
            ans.push_back(nums[i]);
            ans.push_back(nums[j]);
            i++;
            j++;
        }
        while(i<=mid ){
            ans.push_back(nums[i++]);
        }
        while(j<n){
            ans.push_back(nums[j++]);
        }

        return ans;

    }
};