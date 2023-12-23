#include <stdio.h>
#include <math.h>

int is_prime(int n) {
    int i;
    
    if (n == 1) {
        return 0;
    } else if (n < 4) {
        return 1;
    } else if (n % 2 == 0) {
        return 0;
    } else if (n < 9) {
        return 1;
    } else if (n % 3 == 0) {
        return 0;
    } else {
        int r = floor(sqrt(n));
        int f = 5;
        while (f <= r) {
            if (n % f == 0) {
                return 0;
            }
            if (n % (f+2) == 0) {
                return 0;
            }
            f += 6;
        }
    }

    return 1;
}

int main() {
    int n = 10001;
    int count = 1;
    int current_num = 1;

    while (count < n) {
        if (is_prime(current_num)) {
            count++;
            if (count == n) {
                printf("The %dth prime is %d", n, current_num);
            }
        }
        current_num++;
    }

    return 0;
}
