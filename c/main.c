#include <stdio.h>

int main() {
  volatile int a = 10, b = 20, c = 30;

  for (int i = 0; i < 10; i++) {
    c *= a + b;
  }

  int guess;
  printf("Guess Number: "); fflush(stdout);
  scanf("%d", &guess);

  int ans = a * b + 1 * c;
  if (ans == guess) {
    printf("Winner!\n");
  } else {
    printf("Nope\n");
  }
  
  return 0;
}
