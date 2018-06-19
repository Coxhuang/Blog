from django.test import TestCase

list = [6,5,4,3,2,1,1]
dict = {}
for i,v in enumerate(reversed(list)):
    print(i,v)
    dict[i] = v

print(dict)




