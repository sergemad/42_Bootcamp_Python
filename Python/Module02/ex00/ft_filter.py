def ft_filter(function_to_apply,list_of_inputs: list)-> list:
    r : list = []
    for i in range(0,len(list_of_inputs)):
        if function_to_apply(list_of_inputs[i]):
            r.append(list_of_inputs[i])
    
    return r