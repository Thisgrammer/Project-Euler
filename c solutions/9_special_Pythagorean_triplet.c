#include<stdio.h>
#include<math.h>


int main() {
    int a, b, c;
    int limit = 1000;

    for (int m = 2; m < 51; m++) {
        int n = limit / 2 / m - m;
        a = m*m - n*n;
        b = 2*m*n;
        c = m*m + n*n;
        if (n < 0 || n >= m) {
            continue;
        }
        if (2 * m * (m + round(n)) == limit) {
            printf("%ld", a*b*c);
        }
    }

    return 0;
}