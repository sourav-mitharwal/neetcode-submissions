class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> visited;
        for (int i : nums){
            if(visited.find(i) != visited.end()){
                return true;
            }
            else{
                visited.insert(i);
            }
        }
        return false;
    }
};