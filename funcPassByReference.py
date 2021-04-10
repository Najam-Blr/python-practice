def function_pass_by_value(in_list):
    print('function_pass_by_value says Input List: ', in_list, id(in_list))

    # Reassigning a local value, [pass by value example]
    in_list.append(5)
    print('function_pass_by_value says changed List: ', in_list, id(in_list))

source_list_2 = ['A', 'B', 'C']
print('Before passing by value to function, source_list: ', source_list_2, id(source_list_2))
# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_value(source_list_2)
print('After passing by value to function, source_list: ', source_list_2, id(source_list_2))
