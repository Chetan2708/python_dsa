def fun(x):
    stack=[]
    st = ""

    for i in range(len(x)):
        stack.append(x[i])
    for i in range(len(stack)):
        st+=(stack.pop())
    print(st)

x = input()
fun(x)



