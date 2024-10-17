#get the count from input
user_input = input("Enter a list of numbers (e.g., [1, 2, 3]): ")

try:
    number_list = list(map(int, user_input.split(','))) # Split by commas and convert to integers
    number_list = [-1, 3, -1, 8, 5,4,20,10,37,22]  
    element=3
    number_list.sort()  # Sort the list in place
    print(number_list)
    print(f"Count of numbers: {len(number_list)}")  # Get the count of numbers
    if len(number_list)<=4:
        print(0)
    # else: 
    #     i=0
    #     number_length= len(number_list)
    #     cur=number_length-element
    #     print(f"cur:{cur}")
    #     output = float('inf') 
    #     print(f"output:{output}")
    #     for i in range(4): # loop number_length-element times
    #         amp=number_list[cur+i-1]-number_list[i]
    #         print(amp)  
    #         output=amp if amp<output else output
    else:
        number_length= len(number_list)
        cur=number_length-element
        output = min(
        number_list[cur + i - 1] - number_list[i]
        for i in range(4)
        )
        print(f"output:{output}")

except ValueError:
    print("That is not a valid number!")    
