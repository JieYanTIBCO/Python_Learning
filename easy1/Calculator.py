def calculator(a,op,b):
    match op:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            if b!=0: 
                return a/b
            else:
                return "ERROR:Can not divid 0!"
        case _:
            return "ERROR:Invalidate operator!"

print("This is a calculator!")

a=float(input("please input the first number:"))
op=input("please input the operator:")
b=float(input("please input the second number:"))

total= calculator(a,op,b)

if isinstance(total,(int,float)):
    print(f"The result is:{total}")
else:
    print(total)