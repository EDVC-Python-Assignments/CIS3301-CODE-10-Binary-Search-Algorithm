import random
#You can use the function below to test your binary search algorithm implementation.
def get_random_list_of_items():
    list_length = random.randint(10,20)
    new_list = []
    for i in range(1,list_length):
        new_list.append(random.randint(100,500))
    return new_list

#Implement a binary search algorithm below