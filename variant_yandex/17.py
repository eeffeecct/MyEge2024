f=open('17.txt').read()
n=[int(x) for x in f]
res = []
for x,y,z,w,t,g in zip(n,n[1:],n[2:],n[3:],n[4:],n[5:]):
    if z + w > t + g and z + w > x + y:
        if t + g > 0 and x + y > 0:
            res.append(z * w)
print(len(res), min(res))