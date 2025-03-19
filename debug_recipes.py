import os
import json
from src.data.data_loader import load_recipes

def main():
    """Debug tool to check if recipes are loading correctly."""
    print("Debugging Recipe Loader")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    recipes_path = os.path.join(current_dir, 'data', 'recipes.json')
    
    print(f"Looking for recipes at: {recipes_path}")
    
    if not os.path.exists(recipes_path):
        print(f"WARNING: Recipe file not found at {recipes_path}")
        print("Will create a new file when loading recipes")
    
    recipes = load_recipes(recipes_path)
    
    print(f"Loaded {len(recipes)} recipes")
    
    # Print recipe names and tags to verify data
    print("\nRecipe names and tags:")
    for i, recipe in enumerate(recipes[:5]):  # Print first 5 recipes
        print(f"{i+1}. {recipe.get('name')} - Tags: {recipe.get('tags')}")
    
    # Check for dessert recipes with chocolate
    print("\nLooking for dessert recipes with chocolate:")
    dessert_recipes = [r for r in recipes if 'dessert' in ' '.join(r.get('tags', [])).lower()]
    chocolate_desserts = [r for r in dessert_recipes if any('chocolate' in ing.lower() for ing in r.get('ingredients', []))]
    
    print(f"Found {len(dessert_recipes)} dessert recipes")
    print(f"Found {len(chocolate_desserts)} chocolate dessert recipes")
    
    if chocolate_desserts:
        print("Example chocolate dessert:")
        print(f"Name: {chocolate_desserts[0].get('name')}")
        print(f"Tags: {chocolate_desserts[0].get('tags')}")
        print(f"Ingredients: {chocolate_desserts[0].get('ingredients')}")

if __name__ == "__main__":
    main()