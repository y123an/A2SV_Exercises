class Solution {
public:
    void flip(vector<int>& arr ,int  index){
        for(int i=0;i<=index/2;i++){
            int temp= arr[i];
            arr[i]=arr[index-i];
            arr[index-i]=temp;
        }
    }
    
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> ans;

        for(int i=arr.size()-1;i>0;i--){
            for(int j=1;j<=i;j++){
                if(arr[j]==i+1){
                    flip(arr,j);
                    ans.push_back(j+1);
                    break;
                }
            }
            flip(arr,i);
            ans.push_back(i+1);
        }

        return ans;
    }
};