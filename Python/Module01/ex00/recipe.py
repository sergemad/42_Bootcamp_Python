class Recipe:

    def __init__(self,name: str, lvl: int, time: int, ing: list[str], desc: str, type: str) -> None:
        # initialisation of all variable an error message if the parameter are not right
        if isinstance(name,str):
            self.name = name
        
        else:
            print("ERROR : name input must be a string")
            quit()

        if isinstance(lvl, int):
            if int(lvl) > 0 & int(lvl) <6:
                self.cooking_lvl = lvl
            
            else:
                print("ERROR : The level input must be between 1 and 5")
                quit()
        
        else:
            print("ERROR : the level input must be an intenger between 1 and 5")
            quit()
        
        if isinstance(time,int):
            self.cooking_ime = time
        
        else:
            print("ERROR : time input must be an intenger")
            quit()
        
        if isinstance(ing,list):
            self.ingredients = ing
        
        else:
            print("ERROR : ingredients input must be a list")
            quit()
        
        if isinstance(desc, str):
            self.description = desc
        
        else:
            print("ERROR : description input must be a string")
            quit()
        
        if isinstance(type,str):
            if type == "lunch" or type == "starter" or type == "dessert":
                self.recipe_type = type
            
            else:
                print("ERROR : type of meal input must be a string between starter, lunch and dessert")
                quit()
        
        else:
            print("ERROR : type of meal input must be a string")
            quit()
    
    def __exit__(self) -> None:
        print("recipe __exit__")

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        txt = f"{self.name} is a {self.recipe_type} meal. The ingredients are {self.ingredients} and it takes {self.cooking_ime} min of preparation"
        return txt

