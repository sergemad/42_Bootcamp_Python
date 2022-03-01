from datetime import datetime
from recipe import Recipe

class Book:

    def __init__(self,name: str) -> None:
        self.name = name
        self.creation = datetime.now()
        self.last_update = datetime.now()
        cake = Recipe(
            "cake",
            4,
            60,
            ["flour", "sugar", "eggs"],
            "",
            "dessert"
        )
        sandwish = Recipe(
            "sandwish",
            2,
            10,
            ["ham", "bread", "cheese","tomatoes"],
            "",
            "lunch"
        )
        salad = Recipe(
            "salad",
            3,
            20,
            ["avocado", "arugula", "tomatoes", "spinach"],
            "",
            "starter"
        )
        self.recipes_list = {
            "starter" : [salad],
            "lunch" : [sandwish],
            "dessert" : [cake]
        }
    
    def get_recipe_by_name(self, name: str) -> Recipe:
        """Print a recipe with the name `name` and return the instance"""
        for meal in self.recipes_list:
            for recpt in self.recipes_list[meal]:
                if recpt.name == name:
                    print(recpt.name)
                    return recpt
        
        print(f"No recipe with the name {name}")
        return None

        

    def get_recipes_by_types(self, recipe_type: str) -> list[str]:
        """Get all recipe names for a given recipe_type """ 
        for meal in self.recipes_list:
            if meal == recipe_type:
                list_recp : list[str] = []
                for recp in self.recipes_list[meal]:
                    list_recp.append(recp.name)

                return list_recp
        
        print ("The recipe type is not good, it must be between starter, lunch and dessert")
        return None

    def add_recipe(self, recipe: Recipe) -> None:
        """Add a recipe to the book and update last_update""" 
        for meal in self.recipes_list:
            if meal == recipe.recipe_type:
                self.recipes_list[meal].append(recipe)
