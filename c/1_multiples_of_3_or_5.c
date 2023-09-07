#include<stdio.h>

int multiples(int a, int b, int k) {
    int result = 0;
    int i = 1;
    for (i; i < k; i++) {
        if (i % a == 0 || i % b == 0) {
            result += i;
        }
    }
    return result;
}

int main() {
    printf("%d", multiples(3, 5, 1000));
    return 0;
}