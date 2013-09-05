nums = range(100)

numbers = [x for x in nums]
print('numbers:\n',numbers)

cubes = [x*x*x for x in nums]
print('cubes:\n', cubes)

cubesmod2 = [x*x*x for x in nums if x*x*x % 2 == 0]
print('cubes even:\n', cubesmod2)

cubesmod2dict = {x:x*x*x for x in nums if x*x*x % 2 == 0}
print('cubes even dictionary:\n', cubesmod2dict)