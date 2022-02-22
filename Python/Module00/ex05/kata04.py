class module:

    def __init__(self) -> None:
        self.t = (0,4,132.42222,10000,12345.67)
        self.show()
    
    def show(self):
        mod,ex,a,b,c = self.t
        print(f'module_0{mod}, ex_0{ex} : {round(a,2)}, '+ '{:.2e}'.format(b)+', {:.2e}'.format(c))

def main():
    test = module()

main()