class tuple:

    def __init__(self) -> None:
        self.t = (19,42,21)
        self.show()
    
    def show(self):
        a,b,c = self.t
        print(f'The {len(self.t)} numbers are: {a}, {b}, {c}')

def main():
    test = tuple()

main()