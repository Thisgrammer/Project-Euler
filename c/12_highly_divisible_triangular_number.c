#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int countDivisors(int n) {
    int divisors = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            divisors += 1;
        }
    }
    return divisors;
}

int *sieve(int k) {
    int *array = (int *)malloc(sizeof(int) * k);
    int primesCount = 0;
    char primes[k + 1];

    for (int i = 0; i <= k; i++) {
        primes[i] = 1;
    }

    for (int range = 2; range <= (int)sqrt(k); range++) {
        if (primes[range] == 1) {
            for (int multiple = range * 2; multiple <= k; multiple += range) {
                primes[multiple] = 0;
            }
        }
    }

    for (int i = 2; i <= k; i++) {
        if (primes[i] == 1) {
            array[primesCount] = i;
            primesCount++;
        }
    }
    return array;
}

int main() {
    int n = 3;
    int Dn = 2;
    int cnt = 0;
    int n1, Dn1, i, exponent;
    int *primesArray = sieve(100);

    while (cnt != 500) {
        n++;
        n1 = n;

        if (n1 % 2 == 0) {
            n1 /= 2;
        }

        Dn1 = 1;

        for (i = 0; i < 100; i++) {
            if (primesArray[i] * primesArray[i] > n1) {
                Dn1 *= 2;
                break;
            }

            exponent = 1;

            while (n1 % primesArray[i] == 0) {
                exponent++;
                n1 /= primesArray[i];
            }

            if (exponent > 1) {
                Dn1 *= exponent;
            }

            if (n1 == 1) {
                break;
            }
        }

        cnt = Dn * Dn1;
        Dn = Dn1;
    }

    printf("%d\n", n * (n - 1) / 2);
    free(primesArray); // Libera a memória alocada para o array de primos

    return 0;
}
