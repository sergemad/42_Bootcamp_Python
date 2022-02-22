
class cookbook:
    
    def __init__(self) -> None:
        self.book = {
            "sandwish":{
                "ingredients" : ["ham", "bread", "cheese","tomatoes"],
                "type_meal" : "lunch",
                "prep_time" : 10,
            },
            "cake":{
                "ingredients" : ["flour", "sugar", "eggs"],
                "type_meal" : "dessert",
                "prep_time" : 60,
            },
            "salad":{
                "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
                "type_meal" : "lunch",
                "prep_time" : 15,
            }
        }
        self.menu()


    def menu(self):

        print(f"Please select an option by typing the corresponding number:",
        "1: Add a recipe",
        "2: Delete a recipe",
        "3: Print a recipe",
        "4: Print the cookbook",
        "5: Quit",sep="\n")
        condition = True
        while condition == True:
            value = input()
            if value == "1":
                self.add_recipe()
                print("The action is done, please type another corresponding number of the menu (1 to 5).\nTo exit, enter 5.")

                
            elif value == "2":
                self.delete_recipe()
                print("The action is done, please type another corresponding number of the menu (1 to 5).\nTo exit, enter 5.")


            elif value == "3":
                self.show_recipe()
                print("The action is done, please type another corresponding number of the menu (1 to 5).\nTo exit, enter 5.")

            elif value == "4":
                self.show_book()
                print("The action is done, please type another corresponding number of the menu (1 to 5).\nTo exit, enter 5.")


            elif value == "5":
                condition = False
                print("Cookbook closed")
            
            else:
                print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")


    def add_recipe(self):
        print('What is the name of the recipe:')
        name = input()
        print('What are the ingredients (separate ingredient with only a ,) :')
        ing = input()
        print('What is the type of meal of the recipe:')
        meal = input()
        print('What is the preparation time of the recipe:')
        time = input()
        dict_recipe = {
            "ingredients" : ing.split(","),
            "type_meal" : meal,
            "prep_time" : time
        }
        self.book[name] = dict_recipe
        print("Recipe added.")


    def delete_recipe(self):
        print("Please enter the recipe's name to delete it:")
        condition = True
        while condition == True:
            recipe = input()
            for r in self.book:
                if r == recipe:
                    del self.book[r]
                    print(f"No {r} recipe anymore")
                    condition = False
                    break

            if condition == True:
                    print("This recipe does not exist. Choose another one.")


    def show_recipe(self):
        print("Please enter the recipe's name to get its details:")
        condition = True
        while condition == True:
            recipe = input()
            for r in self.book:
                if r == recipe:
                    print(f"recipe for {r}:")
                    ing,meal,time = self.book[r]["ingredients"],self.book[r]["type_meal"],self.book[r]["prep_time"]
                    print(f"Ingredients list: {ing}",
                    f"To be eaten for {meal}.",
                    f"Takes {time} minutes of cooking.", sep="\n")
                    condition = False
                    break

            if condition == True:
                    print("This recipe does not exist. Choose another one.")

    def show_book(self):
        print("Cookbook list:")
        for r in self.book:
            print(r)



def main():
    test = cookbook()

main()
