tupal = (12,34,53,12,33) # tupal are immutiable mens if we can try to change it we can not change it
print(tupal)

tup1 = (1,4,5,6)
l1 = list(tup1)
l1[3] =4
tup1 = tuple(l1)
print(tup1)