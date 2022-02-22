from recipe import Recipe
from book import Book

def main():
    b = Book("my_book")
    r = b.get_recipe_by_name("salad")
    b.add_recipe(recipe = Recipe("test", 10, 40, ["test"], "", "lunch"))
    m = b.get_recipes_by_types("lunch")
    
    print(r,m)

main()
