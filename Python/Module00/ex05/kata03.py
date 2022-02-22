class phrase:

    def __init__(self) -> None:
        self.phrase = "The right format"
        self.show()
    
    def show(self):
        print(f'------------------------{self.phrase}%')

def main():
    test = phrase()


main()