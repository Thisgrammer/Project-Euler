#include<stdlib.h>

int main() {
    long long number = 600851475143LL;
    int divisor = 2;

    while (number != 1) {
        if (number % divisor == 0) {
            number /= divisor;
        } else {
            divisor += 1;
        }
    }

    printf("%d", divisor);

    return 0;
}
