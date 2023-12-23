#include<stdio.h>


int divisors(int n) {
    int sum;
    int i;
    for (i = 1; i <= n/2; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }
    // perfect number if n == sum
    // deficient if sum < n
    // abundant if sum > n
    return sum;
}

int main() {
    
    printf("%d", divisors(12));
    // for (i = 12; i <= 28123; i++) {

    // }
    return 0;
}
