def ft_reduce(function_to_apply,list_of_inputs):
    if isinstance(list_of_inputs,list):
        r = list_of_inputs[0]
        for i in range(1,len(list_of_inputs)):
            r = function_to_apply(r,list_of_inputs[i])
        
        return r
    
    else:
        print("ERROR : Bad parameter")