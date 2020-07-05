# a= 10
# b = 'abc'
# c = 1,2
# d = [1,2]
# e = {"a":1,"b":'str'}
# f = 2.13
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# a = 10
# b = 20
# print('test %d' %a)
#
# print('tes %d %d' %(a,b))
#
# # f字符串
# print(f'test {a}')
# print(f'test{a}--{b}')

# a = 10
# b = 20
# c = a+b if a<b else a/b
# print(c)

# a = 1 or 2
# b = 1 or 0
# c = 0 or 0
# d = 0 or 1
# print(a,'--',b,'--',c,'--',d)

# test = 'abcsdfseeaafsa'
# new_test = test.replace('a','M',2)
# print(new_test)
# new_test1 = test.replace('a','M')
# print(new_test1)
# new_test2 = test.replace('a','M',10)
# print(new_test2)
# list1 = test.split('a')
# print(list1)
# list2 = test.split('a',2)
# print(list2)

# list1 = ['aaa','bbb']
# str3 = '-'.join(list1)
# print(str3)

# str1 = '     test and test2     '
# print(str1.strip())
# str2 = str1.capitalize()
# print(str1.upper())
# print(str1.lower())

str1 = 'abcddf'
# str2 = str1.ljust(10,'-')
# print(str2)
# str3 = str1.rjust(10,'*')
# print(str3)
# str4 = str1.center(10,'&')
# print(str4)
# str5 = str1.ljust(3,'-')
# print(str5)
# print(str1.startswith('a'))
print(str1.endswith('b'))
print(str1.startswith('b',1,5))