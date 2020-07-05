# Python 基础知识

## 1.数据类型

1.1 数字
 - 整型 int
 - 浮点型 float

1.2 字符串 String

- 格式化输出  
```python
a = 10
b = 20
print('test %d' %(a))

print('tes %d %d' %(a,b))

# f字符串
print(f'test {a}')
print(f'test{a}--{b}')

# *
a= '1'
print(a*10) # 重复10次a
 
```

1.3 布尔 Boolean

True,False

1.4 列表

[1,2]
1.5 元组

(1,2)  也可以不带()

1.6 字典

2. 检查变量类型

type()  返回变量对应数据类型
```python
a= 10
b = 'abc'
c = 1,2
d = [1,2]
e = {"a":1,"b":'str'}
f = 2.13

print(type(a))  # <class 'int'>
print(type(b)) # <class 'str'>
print(type(c)) # <class 'tuple'>
print(type(d)) # <class 'list'>
print(type(e)) # <class 'dict'>
print(type(f)) # <class 'float'>
```

3. 类型转换

3.1 字符串转数字

int(str)

float(str)

3.2 字符串转数字

str(int)

3.3 转列表

list()

3.4 转字典

eval(str)

3.5 转元组

tuple()


## 2. 运算符

2.1 算术运算符

 `+ - * /`

2.2 逻辑运算符

` or 或 and 与`

```python

a = 1 and 2
b = 1 and 0
c = 0 and 0
d = 0 and 1
print(a,'--',b,'--',c,'--',d) # 2 -- 0 -- 0 -- 0

a = 1 or 2
b = 1 or 0
c = 0 or 0
d = 0 or 1
print(a,'--',b,'--',c,'--',d) # 1 -- 1 -- 0 -- 1
```

3.3 比较运算符

`> < >= <=`

3.4 赋值运算符

`=`

3.5 运算符优先级

() > 算术运算符 > 比较运算符 > 逻辑运算符 > 赋值运算符

3.6 三目运算符

语法： True时执行 if 条件 else  False时执行

```python
a = 10
b = 20
c = a+b if a<b else a/b
print(c) # 30
```

## 3.条件分支
1. 分支结构
if..else

if..elif..else
2. 循环结构

2.1 while 循环
```python
while 条件：
    循环体
```

2.2 for 循环
```python
for item in 迭代器：
    循环体

```
3. 循环中断

break  跳出循环，循环结束

continue 跳出本次循环，循环继续

4. for..else 与 while..else

循环正常结束后执行else中代码，循环体中使用break关键字跳出循环不会执行else中代码，continue则会执行

## 4. 字符串操作
1. 字符串查找

begin,end为指定索引位置，如果有传则在字符串指定begin，end位置查找指定子串str

1.1 find(str,begin,end)
- 查找字符串中子串，如果有则返回子串在字符串中开始索引，如果不存在则返回-1
- 如果字符串中包含多个子串，则返回第一个

1.2 index(str,begin,end)
- 查找字符串中子串，如果有则返回子串在字符串中开始索引，如果不存在则报错
- 如果字符串中包含多个子串，则返回第一个

1.3 count(str,begin,end)

- 返回子串在字符串中出现的次数,如果没找到则返回0

1.4 rfind(str,begin,end)
- 同 find方法，rfind从右开始查找

1.5 rindex(str,begin,end)
- 同 find方法，rfind从右开始查找

2. 字符串修改
- 字符串不可变，字符串修改不能修改原字符串

2.1 replace(str,newstr,num)
- 三个参数，待替换字符，替换字符，替换数量
- 替换数量超过字符次数时替换所有，效果童不传替换数量
- 有返回值，返回值为替换后的新字符串
```python
test = 'abcsdfseeaafsa'
new_test = test.replace('a','M',2)
print(new_test) # MbcsdfseeMafsa
new_test1 = test.replace('a','M')
print(new_test1) # MbcsdfseeMMfsM
new_test2 = test.replace('a','M',10)
print(new_test2) # MbcsdfseeMMfsM

```
2.2 split(str,num)
- 参数： 分隔符str,分割次数num
- 返回值为列表
```python
test = 'abcsdfseeaafsa'
list1 = test.split('a')
print(list1) # ['', 'bcsdfsee', '', 'fs', '']
list2 = test.split('a',2)
print(list2) # ['', 'bcsdfsee', 'afsa']
```
2.3 join()

- 使用连接符拼接列表

```python
list1 = ['aaa','bbb']
str3 = '-'.join(list1)
print(str3) #$ aaa-bbb

```
2.4 capitalize()

- 将字符串首字母大写
```python
str1 = 'test and test2'
str2 = str1.capitalize()
print(str2) # Test and test2
```
2.5 title()

- 将字符串中每个单词首字母大写
```python
str1 = 'test and test2'
print(str1.title()) # Test And Test2
```

2.6 upper()
- 所有字符大写
```python
str1 = 'test and test2'
print(str1.upper()) # TEST AND TEST2
```
2.7 lower() 
- 所有字符小写
```python
str1 = 'test And test2'
print(str1.lower())  # test and test2
```
2.8 strip()
- 删除首尾空格
```python

str1 = '     test and test2     '
print(str1.strip()) # test and test2
```
2.9 ljust() 与 rjust() 与 center()
- ljust(num,separator)  左对齐，指定字符串长度，不足在右侧填空指定分隔符
- rjust(num,separator)  右对齐，指定字符串长度，不足在左侧填空指定分隔符
- center(num,separator) 居中对齐，左右填充，不是绝对居中
- 指定num小于字符串长度时，不做任何操作
```python
str1 = 'abcddf'
str2 = str1.ljust(10,'-')
print(str2) # abcddf----
str3 = str1.rjust(10,'*')
print(str3) # ****abcddf
str4 = str1.center(10,'&')
print(str4) # &&abcddf&&
str5 = str1.ljust(3,'-')
print(str5)  # abcddf
```

3. 判断是否包含

3.1 startswith(str,begin,end) 与 endswith(str)
- 判断字符串是否以str开头或结尾
```python
str1 = 'abcddf'
print(str1.startswith('a')) # True
print(str1.startswith('a',10,20)) # False
print(str1.startswith('b',1,5)) # True
print(str1.endswith('b')) # False
```




