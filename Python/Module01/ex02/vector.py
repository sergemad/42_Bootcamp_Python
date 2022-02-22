class Vector:

    def __init__(self, values = None) -> None:
        if isinstance(values,type(None)):
            self.values : list[list[float]] = [[]]
        
        elif isinstance(values,list):
            if isinstance(values[0],list):
                self.values = values
                self.shape = (len(self.values),len(self.values[0]))
                
            else:
                print("ERROR : You have to make a list of list")
            
        else:
            print("ERROR : You have to make a list of list")

        

        

