//https://www.acmicpc.net/problem/25501

#include <stdio.h>
#include <string.h>

int recursion(const char *s, int l, int r){
    if(l >= r) return 1;
    else if(s[l] != s[r]) return 0;
    else return recursion(s, l+1, r-1);
}

int isPalindrome(const char *s){
    return recursion(s, 0, strlen(s)-1);
}

int recursion_1(const char *s, int l, int r, int recount){
    if(l >= r) return recount;
    else if(s[l] != s[r]) return recount;
    else return recursion_1(s, l+1, r-1, recount+1);
}

int isPalindrome_1(const char *s){
    return recursion_1(s, 0, strlen(s)-1, 1);
}




int main(){
//    printf("ABBA: %d\n", isPalindrome("ABBA")); // 1
//    printf("ABC: %d\n", isPalindrome("ABC"));   // 0

int T = 0;
scanf("%d", &T);

int ans1[1000] = {0};
int ans2[1000] = {0};

for(int a = 0;  a < T; a ++)
{
	char tempS[1000] = {0};
	scanf("%s", tempS);
	ans1[a] = isPalindrome(tempS);
	ans2[a] = isPalindrome_1(tempS);
	}

for(int a = 0;  a < T; a ++)
{
	printf("%d %d\n", ans1[a], ans2[a]);
	}


return 0;
}