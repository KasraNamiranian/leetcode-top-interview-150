//The answer of leetcode top 1nterview 150 the question number 58 (length of last word) written by Kasra Namiranian.

int lengthOfLastWord(char* s) {
    int l = 0;
    int i = strlen(s);
    while(i>0){
        i--;
        if (s[i] != ' ')
            l++;
        else if (l!=0)
            break;
    }

    return l;
}
