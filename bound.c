#include <stdio.h>
#include <unistd.h>

int main() {
    while(1) {
        sleep(0.5);
        printf("foo\n");
    }
    return 0;
}
