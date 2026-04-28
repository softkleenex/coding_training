#include<stdio.h>

int main() {
    int x = 0; int y = 0; int w = 0; int h = 0;
    scanf("%d %d %d %d", &x, &y, &w, &h);

    int a = (x - 0) <= (w - x) ? (x - 0) : (w - x);
    int b = (y - 0) <= h - y ? y - 0 : h - y;

    printf("%d", a <= b ? a : b);

    return 0;
}