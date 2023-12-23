#include<stdio.h>
#include<math.h>

int main() {
    long long smallest = 0;
    int k = 20;

    for (int i = 2; i < k+1; i++) {
        // check if the i is prime
        int c = 0;
        for (int n = 2; n < k+1; n++) {
            if (i % n == 0) {
                c += 1;
            }
        }
        
        // if i is divisible only by itself, that is, if he is prime 
        if (c == 1) {
            int p = 1;
            while (1) {
                if (pow(i, p) > k) {
                    if (i == 2) {
                        smallest = pow(i, p-1);
                    } else {
                        smallest *= pow(i, p-1);
                    }
                    break;
                } else {
                    p += 1;
                }
            }    
        }
    }
    
    printf("%lld", smallest);
}