# Queue is a Linear Data Structure where elements are inserted from one side and removed from another side
# Queue is open at both ends
#  --|-|-|-|-|-|--
#  --|-|-|-|-|-|--
# Back Rear tail and front/head
# Queue is open at both ends
# FIFO: First IN First OUT and LILO: Last IN Last OUT
# Operations of Queue --> i) enqueue() -->using append() method --> Add elements to queue  ii) dequeue() --> using pop()--> Remove Elements from Queue  iii) isFull --> Check Wheather Queue is full or not
#  iv) isEmpty() --> check weather Queue is empty or not
# We can implement Queues using list and Modules(classes of different modules)

# Queue Implementation using list

queue = []

def enqueue():
    element = input("Enter the Element:")
    queue.append(element)
    print("Element Added ", element)


def dequeue():
    e = queue.pop()
    print("Element removed ", e)

def display():
    print(queue)
    
while True:
    print("Enter the operations to perform 1.Push 2.Pop 3.Remove")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Choose the correct input operatoin")
