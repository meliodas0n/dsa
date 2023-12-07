def binarSearch(inp, x, l, r):
  if r >= l:
    m = (r + l) // 2
    if inp[m] == x:
      return m
    elif inp[m] < x:
      return binarSearch(inp, x, l, m - 1)
    else:
      return binarSearch(inp, x, m + 1, r)
  else:
    return -1



if __name__ == "__main__":
    inp = list(map(int, input().split()))
    x = int(input("Enter number to be search : "))
    print(f"Found {x} at : {binarSearch(inp, x, 0, len(inp) - 1) + 1} ")
