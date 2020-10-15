#include <stdio.h>

int main(void) {
    double x, y, qaly = 0;
    scanf("%d");
    while (scanf("%lf %lf", &x, &y) == 2){
        qaly += x * y;
    }
    printf("%lf", qaly);
    return 0;
}