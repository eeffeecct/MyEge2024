s = open('probnik4/24.txt').readline()
s = s.replace('O', 'N').replace('P', 'N')

while 'NN' in s: s = s.replace('NN', 'N N')
print(max(len(c) for c in s.split()))