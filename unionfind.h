class UnionFind {
public: 
    vector<int> parent, rank; 
    UnionFind(int n) {
        parent.resize(n); 
        iota(begin(parent), end(parent), 0); 
        rank.resize(n); 
        fill(rank.begin(), rank.end(), 1); 
    } 
    
    int find(int p) {
        /* find with path compression */
        if (parent[p] != p) 
            parent[p] = find(parent[p]); 
        return parent[p]; 
    }
    
    bool connect(int p, int q) {
        /* union with rank */
        int prt = find(p), qrt = find(q); 
        if (prt == qrt) return false; 
        if (rank[prt] > rank[qrt]) swap(prt, qrt);
        parent[prt] = qrt; 
        rank[qrt] += rank[prt]; 
        return true; 
    }
};