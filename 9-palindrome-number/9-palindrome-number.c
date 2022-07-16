

bool isPalindrome(int x){
    if (x < 0) return false;
    
    long int reversed = 0, reminder, original = x;
    
    while (x != 0) {
        reminder = x % 10;
        reversed = reversed * 10 + reminder;
        x /= 10;
    }
    
    return original == reversed;
}