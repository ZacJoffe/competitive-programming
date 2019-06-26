class Solution {
private:
    bool isStoneJewel(string J, char S) {
        for (int i = 0; i < J.length(); i++) {
            if (J[i] == S) {
                return true;
            }
        }
        
        return false;
    }
public:
    int numJewelsInStones(string J, string S) {
        int numJewels = 0;
        for (int i = 0; i < S.length(); i++) {
            char stone = S[i];
            if (isStoneJewel(J, stone)) {
                numJewels++;
            }
        }
        
        return numJewels;
    }
};
