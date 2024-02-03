a = [5, 4, 9, -1, 0]

for i in range(len(a)):
  for j in range(len(a)):
    if a[i] <= a[j]:
      a[i], a[j] = a[j], a[i]

print(a)
