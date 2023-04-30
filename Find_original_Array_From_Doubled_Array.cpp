class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {

        vector<int> ans;
        int n=changed.size();
        
        if(n%2) return {};

        unordered_map<int,int> mpp;

        for(int x: changed){
            mpp[x]++;
        }

        sort(changed.begin(),changed.end(), greater<int>());

        for(int x: changed){
            if(x==1) continue;
            if(x==0 && mpp[0]<2) continue;

            if(x%2==0 && mpp[x]>=1 && mpp.find(x/2) != mpp.end() && mpp[x/2]>=1){
                ans.push_back(x/2);
                mpp[x]--;
                mpp[x/2]--;
            }
        }
        
            if(ans.size()==n/2) return ans;
            return {};
    }

};