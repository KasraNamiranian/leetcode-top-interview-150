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