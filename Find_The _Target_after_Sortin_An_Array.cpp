class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int> ans;

        for(int i = 0 ; i<nums.size()-1;i++){
            int min=i;
            for(int j=i+1;j<nums.size();j++){
                if(nums[j]<nums[min]){
                    min=j;
                }
               }
             if(min != i){
                    int temp = nums[i];
                    nums[i] = nums[min];
                    nums[min]=temp;
                }
        }

        for(int i=0 ; i<nums.size();i++){
            if(nums[i]==target){
                ans.push_back(i);
            }
        }

        return ans;
    }
};