
src = [300, 2, 12, 44, 1, 2, 4, 10, 7, 1, 78, 123, 125, 55]

result = [src[n] for n in range(1, len(src)) if src[n] > src[n-1]]
print(result)
