def weird_algorithm():
  n = int(input())
  while True:
    print(n, end=" ")
    if n == 1: break
    if n % 2 == 0: n = int(n / 2)
    else: n = int(3 * n + 1)
  print()

def main():
  print("On a Second thought, I am back to python instead")

if __name__ == "__main__":
  weird_algorithm()