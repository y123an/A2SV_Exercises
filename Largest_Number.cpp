bool custom(string a ,string b){
    if(a+b>b+a) return true;
    else return false;
}
class Solution {
public:
    string largestNumber(vector<int>& nums) {

        vector<string> str_nums;
        int n= nums.size();
        for(int i=0;i<n;i++){
            str_nums.push_back(to_string(nums[i]));
        }    

        sort(str_nums.begin(),str_nums.end(),custom);

        string ans = "";

        for(string x : str_nums){
            ans.append(x);
        } 

        int start=0;
        while(ans[start]=='0' && start<ans.size()-1) start++;

        return ans.substr(start);
    }

};