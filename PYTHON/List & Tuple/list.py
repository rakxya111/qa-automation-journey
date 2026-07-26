# str = ['apple' , 1,2,3,4,5,'ball','2.5','000']
# print(str)

# str1 = list(('apple','banana',1,2,3,4,5,'1.3',1.2))
# print(str1)

# str1[0] = 'happy jii'
# print(str1)

# str[0:3] = ['ball','cat','dog']
# print(str)



# print(str * 3)



# # NO COPY METHOD 
# str = ['apple' , 1,2,3,4,5,'ball','2.5','000']
# str2 = str
# str2[0] = 'ball'
# print(str,str2)

# # COPY METHOD
# str = ['apple' , 1,2,3,4,5,'ball','2.5','000']
# str2 = str.copy()
# str2[0] = 'ball'
# print(str,str2)


# Append Method
# a = ['banna','ball','fruit']
# b = 'catty'
# a.append(b)
# print(a)

# Extend Method
# a = ['banna','ball','fruit']
# b = ['donkey','monkey','motty','hatty']
# a.extend(b)
# print(a)

# # Insert Method
# a = ['banna','ball','fruit']
# c = ['hall','book','lion']
# a.insert(0,c)
# print(a)

# # Remove - with name
# a = ['banna','ball','fruit']
# a.remove('banna')
# print(a)

# # Popped - with index
# b = ['banna','ball','fruit']
# b.pop(1)
# print(b)

# # Clear Method
# a = ['banna','ball','fruit']
# a.clear()
# print(a)

# # Index Method
# a = ['banna','ball','fruit']
# n = a.index('banna')
# print(n)

# Count
# a = ['banna','ball','fruit','banna','banna','banna']
# print(a.count('banna'))

# # sort 
# a = [-1,0,5,3,4,2,-100]
# a.sort()
# print(a)

# # reverse
# a = ['banna','ball','fruit']
# a.reverse()
# print(a)

# # finding - min , max
# a = [-1,0,5,3,4,2,-100]
# print(min(a))
# print(max(a))

# Set
# a = [-1,0,5,3,4,2,-100]
# b = [3,4,2,-100]
# s1 = set(a)
# s2 = set(b)
# u = s1.intersection(s2)
# print(list(u))

# # Nested 
# a = [-1,0,5,3,4,2,-100]
# b = [900,a,[2,3,5]]
# print(b)


# # range to list
# number = list(range(1,10,1))
# print(number)

# List Comphrehension
# square = [i ** 2 for i in range(1,11)]
# print(square)

# List Comphrehension
# expression for item in iterable if condition
# square = [i ** 2 for i in range(1,11) if i%2 == 0]
# print(square)

