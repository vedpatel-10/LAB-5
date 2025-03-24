import random

# Initialize queue with 5 random numbers
queue = [random.randint(1, 100) for i in range(5)]
print("Initial queue:", queue)

print("\nQueue Menu:")
print("1. Insert")
print("2. Delete")
print("3. Display")

choice = input("Enter your choice: ")
    
if choice == '1':
        item = input("Enter the item to insert: ")
        queue.append(int(item))
        print(f"{item} added to queue.")
elif choice == '2':
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            item = queue.pop(0)
            print(f"{item} removed from queue.")
elif choice == '3':
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            print("Queue elements are:")
    
            print(queue)        
else:
        print("Invalid choice. Please try again.")