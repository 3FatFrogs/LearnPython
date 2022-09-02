
import math

print('Hello World!!')


pippoList = []
for x in range(10):
    pippoList.append(round(x*math.sin(x),3))

print(pippoList)
print(pippoList.sort())



def pippo(*arguments):
    s1 = "==="
    s2 = s1 + "=============================================="
    
    if len(arguments)>0:
        temp = " " + arguments[0]  + " ";
        s3 = "{}{}{}".format(s1,temp,s2[0:len(s2)-len(temp)])
    else:
        s3 = "{}{}".format(s1,s2)
    
    print('\n' + s3)


pippo()
a = 8
b = 3.3

word = 'Python'
print(a, type(a))
print(b, type(b))
print(word, type(word))

print(word[0])     # character in position 0
print(word[5])     # character in position 5
print(word[0:2])   # characters from position 0 (included) to 2 (excluded)
print(word[2:5])   # characters from position 2 (included) to 5 (excluded)

for x in word:
    print(x)




pippo("List")
squares = [1, 4, 9, 16, 25]
squares.append(36)
print(squares, type(squares))







pippo("Loops")
r = range(0, 20, 2)
print(10 in r)
print(11 in r)
#for x in range(1,5,0.2):
#    print(x, end=',')


for num in range(15,18):
    if num%2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


for num in range(15,18):
    if num%2 == 0:
        print("Found an even number", num)
        break
    print("Found a number", num)


x = int(input("Please enter an integer: "))
if x < 0:
    print("Negative number")
elif x==0:
    print("Zeor")
else:
    print("Positive number")



pippo("for else")
#For..Else
for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))



pippo("Lambda Expressions")
def make_incrementor(n=1):
    return lambda x: x+n

f = make_incrementor(10)
print(f(6))
print(f(2))
print(f(1))
print(f(9))


pairs = [(1, 'one'), ("2", 'two'), (3, 'three'), (4, 'four')] #list of tuple
print(type(pairs))
print(pairs)
for x,y in pairs:
    print("{}-{}".format(x,y))

pairs2 = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')] #list of
for x,y in pairs2:
    print("{}-{}".format(x,y))

pairs.sort();
print(pairs)