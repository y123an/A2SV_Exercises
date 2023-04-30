class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {

        sort(nums.begin(),nums.end());
        int l=0,r=0;
        long long int total=0;
        int res = 0;
        int n = nums.size();

        for(int i =0;i<n;i++){
            total +=nums[r];
            long long int windowSize = r-l+1;
            if(nums[r]*windowSize > total+k){
                total -= nums[l];
                l++;
            }
            res= max(res,r-l+1);
            r++;
        }
        return res;

    }
};