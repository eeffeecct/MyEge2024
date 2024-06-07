text = open('6.txt').readline()

k = 0
data = set()
try:
    for i in range(len(text) - 1):
        if text[i] == 'X' and text[i + 1] == 'Y' and text[i + 2] == 'Z':
            k += 3
            text = text[3:]
        else:
            data.add(k)
            k = 0
except IndexError:
    print(max(data))
