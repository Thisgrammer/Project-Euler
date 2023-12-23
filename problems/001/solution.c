#include <stdio.h>

int main() {
    int a = 3;
    int b = 5;
    int sum_multiples = 0;

    int k = 1000;
    
    int i;
    for (i = 1; i < k; i++) {
        if (i % a == 0 || i % b == 0) {
            sum_multiples += i;
        }
    }

    printf("%d\n", sum_multiples);

    return 0;
}