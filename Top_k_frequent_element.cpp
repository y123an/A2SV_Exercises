class Solution {
public:

    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mpp;
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> heap;
        vector<int> ans;

        for(int x: nums){
            mpp[x]++;
        }


        for(auto x : mpp){
            heap.push({x.second,x.first});
            if(heap.size()>k){
                heap.pop();
            }
        }


        while(k--){
            ans.push_back(heap.top().second); 
            heap.pop();
        }

        return ans;
    }
};