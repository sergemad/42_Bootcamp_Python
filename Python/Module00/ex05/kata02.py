
class date:

    def __init__(self) -> None:
        self.t = (3,30,2019,9,25)
        self.show()
    
    def show(self):
        hour, min, year, day, month  = self.t
        print(f'{day}/{month}/{year} {hour}:{min}')

def main():
    test = date()

main()