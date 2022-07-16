

bool isPalindrome(int x){
    bool ans = false;
    if(x < 0) {
        return ans;
    }
    
    char str[32];
    sprintf(str, "%d", x);
    int l = 0, r = strlen(str) - 1;
    
    while(l < r && str[l] == str[r]) {
        l++;
        r--;
    }
    
    return l >= r;
}