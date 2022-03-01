def ft_map(function_to_apply,list_of_inputs: list)-> list:
    for i in range(0,len(list_of_inputs)):
        list_of_inputs[i] = function_to_apply(list_of_inputs[i])
    
    return list_of_inputs