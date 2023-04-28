class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> ans(k);
        int n=points.size();
        vector<pair<int,pair<int,int>>> v;
        int dist;

        for(vector point : points){
            dist = point[0] * point[0] + point[1]*point[1];
            v.push_back({dist,{point[0],point[1]}});
        }

        sort(v.begin(),v.end());

        for(int i=0;i<k;i++){
            ans[i].push_back(v[i].second.first);
            ans[i].push_back(v[i].second.second);
        }
        return ans;
    }

};