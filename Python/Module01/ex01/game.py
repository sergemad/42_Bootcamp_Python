class GotCharacter:

    def __init__(self, first_name: str, is_alive: str) -> None:
        self.firs_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
     # To formate the docstring
    '''A class representing the Stark family. Or when bad things happen to good people.'''
    def __init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.firs_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self) -> None:
        print(f"The house words is {self.house_words}")
    
    def die(self):
        self.is_alive = False
    