class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();

        for(int i = 0;i<n-1;i++){
            int min=i;
            for(int j=i+1;j<n;j++){
                if(nums[min]>nums[j]){
                    min=j;
                }
            }
            if(min != i){
                int temp=nums[i];
                nums[i]=nums[min];
                nums[min]=temp;
            }
        }

        for(int i=0;i<n;i++){
            cout<<nums[i]<<" ";
        }
    }
};