#include<stdlib.h>
#include<string.h>

int main() {
    int largest = 0;
    const int MAX_NUM = 999;
    const int MIN_NUM = 100;

    for (int n = MAX_NUM; n >= MIN_NUM; n--) {
        for (int m = MAX_NUM; m >= MIN_NUM; m--) {
            int palindrome = n * m;
            if (palindrome <= largest) {
                break;
            }
            char str_palindrome[100];
            sprintf(str_palindrome, "%d", palindrome);
            int len = strlen(str_palindrome);
            int is_palindrome = 1;
            for (int i = 0; i < len / 2; i++) {
                if (str_palindrome[i] != str_palindrome[len - 1 - i]) {
                    is_palindrome = 0;
                    break;
                }
            }
            if (palindrome > largest && is_palindrome) {
                largest = palindrome;
            }
        }
    }

    printf("%d", largest);
    return 0;
}