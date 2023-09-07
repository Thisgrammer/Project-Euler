#include<stdint.h>

int main() {
    int sumF = 0;
    int a = 1, b = 2, k = 4000000;
    while (a < k || b < k) {
        if (a % 2 == 0) {
            sumF += a;
        } 
        int temp = a;
        a = b;
        b = temp + b;
    }

    printf("%d", sumF);

    return 0;
}
