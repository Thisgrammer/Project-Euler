#include<stdio.h>
#include<math.h>

int main() {
    int sum_of_squares = 0;
    int sum = 0;
    int k = 100;
    for (int i = 1; i <= k; i++) {
        sum_of_squares +=  pow(i, 2);
        sum += i;
    }
    int square_of_sum = pow(sum, 2);
    int result = square_of_sum - sum_of_squares;
    printf("%d", result);
    return 0;
}