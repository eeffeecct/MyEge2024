text = open('5.txt').readline()
data = ''
my_dict = {}


for i in range(len(text) - 1):
    if text[i] == 'A':
        data += text[i + 1]
        data = data.replace('A', '', 1)


for letter in data:
    if letter in my_dict:
        my_dict[letter] += 1
    else:
        my_dict[letter] = 1

most_frequent_letter = max(my_dict, key=my_dict.get)
print(most_frequent_letter, my_dict[most_frequent_letter])

# L1567

