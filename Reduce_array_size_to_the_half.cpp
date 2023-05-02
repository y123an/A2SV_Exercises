class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int,int> mpp;
        multimap<int,int,greater<int>> mm;
        for(int x : arr){
            mpp[x]++;
        }
        for(auto x: mpp){
            mm.insert({x.second,x.first});
        }
        
        int total= arr.size();
        int count=0;

        for(auto x:mm){
            total -= x.first;
            count++;
            if(total <= arr.size()/2){
                return count;
            }
        }
        return count;
    }
};