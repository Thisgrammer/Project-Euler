#include <stdio.h>
#include <math.h>


int main() {
    int k = 2000000;
    char primes[k + 1];
    for (int i = 0; i < k; i++) {
        primes[i] = 1;
    }

    for (int range = 2; range <= (ceil(sqrt(k))); range++) {
        if (primes[range] == 1) {
            for (int multiple = range * 2; multiple <= k; multiple += range) {
                primes[multiple] = 0;
            }
        }
    }
    
    long long sum = 0;
    for (int i = 2; i <= k; i++) {
        if (primes[i] == 1) {
            sum += i;
        }
    }

    printf("%lld", sum);
    return 0;
}