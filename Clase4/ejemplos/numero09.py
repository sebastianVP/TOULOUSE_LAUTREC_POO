import collections

d1= collections.OrderedDict()
d1['B']=61
d1['A']=60
d1['C']=55
d1['D']=50
d1['B']=61


for k,v in d1.items():
    print(k,v)