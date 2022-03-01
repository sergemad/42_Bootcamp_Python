class Vector:

    '''Manipulation of vector and operation on vectors'''
    def __init__(self, values = None) -> None:
        self.values : list[list] = []
        if isinstance(values,list):
            if isinstance(values[0],list):
                condition = True
                isfloat = True
                height = len(values[0])
                for v in range(0,len(values)):
                    if height != len(values[v]):
                        condition = False
                        break
                    else:
                        for f in values[v]:
                            if not(isinstance(f,float)):
                                isfloat =False
                                break
                
                if condition == True and isfloat == True:
                    self.values = values
                    self.shape = (len(self.values),len(self.values[0]))

                elif isfloat == False:
                    print("ERROR : The value of the list must be float")

                elif condition == False:
                    print("ERROR : The shape of the list is not right")
                
            else:
                print("ERROR : You have to make a list of list")
            
        elif isinstance(values, tuple):
            min, max = values[0], values[1]
            for v in range(min, max):
                self.values.append([float(v)])
            
            self.shape = (len(self.values),len(self.values[0]))
        
        elif isinstance(values, int):
            for v in range(0, values):
                self.values.append([float(v)])
            
            self.shape = (len(self.values),len(self.values[0]))


    def dot(self,v):
        return self*v

    def T(self):
        results : list[list[float]] = [[]]
        for i in range(0,self.shape[0]):
            for j in range(0,self.shape[1]):
                results[j].append(self.values[i][j])

        return results[0]

    def __mul__(self, a):
        if isinstance(a,Vector):
            r = 0
            if self.shape == a.shape and self.shape[1] == 1:
                for i in range(0,self.shape[0]):
                    r = r + self.values[i][0] * a.values[i][0]
                
                return r
            
            else:
                print("ERROR : The shape of the two vectors must be (m * 1) ")
            
        else:
            results : list[list[float]] = []
            for i in range(0,self.shape[0]):
                results.append([])
                for j in range(0,self.shape[1]):
                    results[i].append(self.values[i][j] * a)
        
            return Vector(results)
        
    def __add__(self, a):
        if isinstance(a,Vector):
            if self.shape == a.shape and self.shape[1] == 1:
                results : list[list[float]] = []
                for i in range(0,self.shape[0]):
                    results.append([])
                    for j in range(0,self.shape[1]):
                        results[i].append(self.values[i][j] + a.values[i][j])
                
                return Vector(results)
            
            else:
                print("ERROR : The shape of the two vectors must be (m * 1) ")
        
        else:
            print("ERROR : Addition is only on vectors")
        
    def __sub__(self, a):
        if isinstance(a,Vector):
            if self.shape == a.shape and self.shape[1] == 1:
                results : list[list[float]] = []
                for i in range(0,self.shape[0]):
                    results.append([])
                    for j in range(0,self.shape[1]):
                        results[i].append(self.values[i][j] - a.values[i][j])
                
                return Vector(results)
            
            else:
                print("ERROR : The shape of the two vectors must be (m * 1) ")
        
        else:
            print("ERROR : substraction is only on vectors")
        
    def __truediv__(self, a: int):
        if a != 0:
            results : list[list[float]] = []
            for i in range(0,self.shape[0]):
                results.append([])
                for j in range(0,self.shape[1]):
                    results[i].append(self.values[i][j] / a)
            
            return Vector(results)
        
        else:
            print("ERROR : division is not possible with two vectors")

    def __str__(self) -> str:
        return f"The vector in {self.values} and his shape is {self.shape}"
    
