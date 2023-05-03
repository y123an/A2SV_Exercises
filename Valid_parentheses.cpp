class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        bool ans;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('||s[i]=='['||s[i]=='{'){
                stack.push_back(s[i]);
            }else{
                if(stack.empty()) return false;
                else if(s[i]==')' && stack.back() != '(' ) return false;
                else if(s[i]=='}' && stack.back() != '{' ) return false;
                else if(s[i]==']' && stack.back() != '[' ) return false;
                else stack.pop_back();
            }
        }

        if(stack.empty()){
            ans=true;
        }else ans=false;
       

        return ans;
    }
};