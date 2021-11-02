class TrieNode {
    TrieNode* children[26] = {nullptr};
    bool isWord = false;
public: 
    ~TrieNode() {
        for (auto& child : children) 
            delete child; 
    }
};


class Trie {
    TrieNode* root; 
public: 
    Trie() { root = new TrieNode(); }
    ~Trie() { delete root; }

    void insert(string word) {
        TrieNode* node = root; 
        for (auto& letter : word) {
            if (!node->children[letter-'a']) 
                node->children[letter-'a'] = new TrieNode(); 
            node = node->chidlren[letter-'a'];
        }
        node->isWord = true; 
    }

    bool prefix(string word) {
        TrieNode* node = root; 
        for (auto& letter : word) {
            node = node->children[letter-'a']; 
            if (!node) return false; 
        }
        return true; 
    }

    bool search(string word) {
        TrieNode* node = root; 
        for (auto& letter : word) {
            node = node->children[letter-'a']; 
            if (!node) return false; 
        }
        return node->isWord; 
    }
}