# Stack Works on LIFO(Last IN first OUT) / FILO (FIrst In Last Out )MEthodolgy
# Stack can be implemented using LIST and Module methods 
# Stack Mainly has push(), pop(), peek() / top(), isEmpty() 
# Push() --> Add the Element to stack using append() method

# This is List method

stack = []

def push():
    element = input("Enter the Element")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is EMpty")
    else:
        e = stack.pop()          
        print("Removed element:", e)
        print(stack)
     
while True:
    print("Select the operation 1. Push 2. Pop 3. Quit")
    choice = int(input())
    if choice == 1:
        push()  
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter correct operation")