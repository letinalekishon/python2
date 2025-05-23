sets = {12,12,12,12,34,12,12,12,12}
print(type(sets))
print(sets)


set={5,6,7,8}
x={1,2,3,4,5,6,7}

z=x-set
print(z)

z= x.difference(set)
print(z)

z= x.union(set)
print(z)


z= x.symmetric_difference(set)
print(z)


z= x.intersection(set)
print(z)