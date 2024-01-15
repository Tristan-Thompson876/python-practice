
x = "my_Globalx"

def test():
    global x
    x = "new_x"
    y = "my_loacly"
    print(y)

def outer():
    m = "outer"
    def inner():
        m = "inner"
        print(m)

    inner()
    print(m)
outer()

print(x)
print(x[0:4])
print(x[0:])
print(x[0:-1])
print(x[0:-1:-1])
print(x[0:-1:2] + " before")
print(x[-1:2:-2] + " this")
print(x[::-1])
print(x[::-3])

#list comprehension review
#nums = [0,1,2,3,4,5,6,7,8,9,10]

#add 10 to each number in list
#my_L = [n + 10 for n in nums]
#print(my_L)

#Lamda and map review
nums = [0,1,2,3,4,5,6,7,8,9,10]
my_L = list(map(lambda n: n*n, nums))
print(my_L)