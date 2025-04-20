import random

# Initialize stack with 5 random numbers
stack = [random.randint(1, 100) for i in range(5)]
print("Initial stack:", stack)


print("\nStack Menu:")
print("1. Push")
print("2. Pop")
print("3. Display")

choice = input("Enter your choice: ")
    
if choice == '1':
        item = input("Enter the item to push: ")
        stack.append(int(item))
        print(f"{item} pushed to stack.")
elif choice == '2':
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            item = stack.pop()
            print(f"{item} popped from stack.")
elif choice == '3':
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Stack elements are:")
            for item in reversed(stack):
                print(item)
else:
        print("Invalid choice. Please try again.")

#OUTPUT:
# Initial stack: [3, 78, 82, 59, 76]

# Stack Menu:
# 1. Push
# 2. Pop
# 3. Display
# Enter your choice: 2
# 76 popped from stack.  
