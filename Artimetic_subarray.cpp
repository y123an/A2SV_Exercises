class Solution {
public:

    bool isArtimetic(vector<int> &vec){
        int n=vec.size();
        if(n==2) return true;
        int d= vec[1]-vec[0];

        for(int i=2;i<n;i++){
            if(vec[i]-vec[i-1] != d){
                return false;
            }
        }
        return true;
    }
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> ans;
        int n= l.size();

        for(int i=0;i<n;i++){
            int s=l[i];
            int e=r[i];
            vector<int> vec;
            for(int j=s;j<=e;j++){
                vec.push_back(nums[j]);
            }
            sort(vec.begin(),vec.end());
            if(isArtimetic(vec)){
                ans.push_back(true);
            }else{
                ans.push_back(false);
            }
        }

        return ans;
      
    }
};