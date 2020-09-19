def list_concatenator(data):
    # Takes a list and makes a comma-separated string with 'and' before the
    #  last item.
    list_string = ''
    
    if data:
        for item in data[:-1]:
            list_string = list_string + item + ', '
    
        list_string += f'and {data[-1]}'

        return list_string

# Testing a normal list.
numbers = [str(value) for value in range(1, 11)]
number_string = list_concatenator(numbers)
print(number_string)

# Testing an empty list.
empty_list = []
empty_string = list_concatenator(empty_list)
print(empty_string)