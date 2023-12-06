def linearSearch(inp, x):
  return inp.index(x) + 1

if __name__ == "__main__":
  inp = list(map(int, input().split()))
  x = int(input("Enter the search number : "))
  print(f"Found at index : {linearSearch(inp, x)}")
