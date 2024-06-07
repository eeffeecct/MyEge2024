text = open('24.txt').readline()
k = 0
data = set()
for i in range(1, len(text) - 1, 2):
    if text[i] + text[i + 1] in ('AB', 'CB'):
        k += 1
    else:
        data.add(k)
        k = 0

print(max(data))
