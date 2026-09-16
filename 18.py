t = (1, 2, 3, 4, 5, 6, 7, 8)

print("Tuple:", t)
print("Count:", t.count(4))
print("Index:", t.index(5))

l = list(t)

l.remove(4)
print("After remove:", l)

l.pop()
print("After pop:", l)

l.sort()
print("After sort:", l)

l.reverse()
print("After reverse:", l)

l.append(10)
print("After append:", l)

l.extend([11, 12, 13])
print("After extend:", l)

print("Sum:", sum(l))
print("Max:", max(l))
print("Min:", min(l))
print("Length:", len(l))