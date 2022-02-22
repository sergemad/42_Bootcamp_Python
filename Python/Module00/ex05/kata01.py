class language:

    def __init__(self) -> None:
        self.l = {
            'Python': 'Guido Van Rossum',
            'Ruby': 'Yukihiro Matsumoto',
            'PHP': 'Rasmus Lerdof'
        }
        self.show()
    
    def show(self):
        print(f'Python was created by {self.l["Python"]}\n'+
              f'Ruby was created by {self.l["Ruby"]}\n'+
              f'PHP was created by {self.l["PHP"]}')

def main():
    test = language()

main()