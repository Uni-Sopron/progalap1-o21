li = [5, 4, 2]
print(li)
#li.append('nulla')
li.append(0)
print(li)
#l2 = li.copy()
#l2 = list(li)
#l2 = li[:]
l2 = li
li.extend(l2)
li += [1, 2, 3]
#li.clear()
print('li =', li)
li.insert(-3, 0)
li.remove(4)
print('l2 =', l2)
print('2 is in list?', 2 in li)
print('6 is in list?', 6 in li)
li.sort()
li.reverse()
print(li)
print(sorted(li))
print(li)
