def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multyply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
operation={"+":add,"-":subtract,"*":multyply,"/":division}
def calculator():
    num1=int(input("Enter first number:"))
    for symbol in operation:
        print(symbol)
    x= True
    while x :
        operand=input("pick operation ")
        clculation_function=operation[operand]
        num2=int(input("Enter next number:"))
        answer=clculation_function(num1,num2)
        print(f"{num1} {operand} {num2} = {answer}")
        continu=input("if want to calculate with answer type 'y' for new calculation type 'n'")
        if continu=='y':
            num1=answer
        else:
            x=False
            calculator()
calculator()            

                
