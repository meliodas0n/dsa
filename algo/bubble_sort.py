def bubbleSort(inp):
  for i in range(len(inp)):
    for j in range(1, len(inp)):
      if inp[i] >= inp[j]:
        inp[i], inp[j] = inp[j], inp[i]
  return inp

if __name__ == "__main__":
  inp = list(map(int, input().split()))
  print(f"Bubble Sorting : {bubbleSort(inp)}")