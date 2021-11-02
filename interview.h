vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> ans; 
    vector<int> stk; 
    for (int x = 0; true; ) {
        if (stk.size() == k) ans.push_back(stk); 
        if (stk.size() == k || k - stk.size() > n - x) {
            if (stk.empty()) break; 
            x = 1 + stk.back(); stk.pop_back(); 
        } else stk.push_back(x++); 
    }
    return ans; 
}
