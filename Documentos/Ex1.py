fileopen = open("data.txt")
n= 0 
lst = []
p = 0

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

for line in fileopen:
        n += 1
        x = line.strip().split(",")
        if isfloat(x[-1]) == True:
            t = float(x[-1])
            lst.append(t)

for i in range(len(lst)):
    p = p + lst[i]

med = p/len(lst)
print(med)
print(max(lst))
print(min(lst))


