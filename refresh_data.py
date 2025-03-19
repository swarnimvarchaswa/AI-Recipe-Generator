import os
import shutil
import json
from src.data.data_loader import load_recipes, load_ingredients

def print_colorful(text, color_code, end="\n"):
    """Print text in color."""
    print(f"\033[{color_code}m{text}\033[0m", end=end)

def refresh_all_data():
    """Force refresh all data files by deleting them and regenerating."""
    print_colorful("🔄 Refreshing all data files...", "1;36")
    
    # Get data directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')
    
    # Create data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    # Delete and recreate recipes.json
    recipes_path = os.path.join(data_dir, 'recipes.json')
    if os.path.exists(recipes_path):
        print_colorful(f"🗑️  Deleting existing recipes file: {recipes_path}", "33")
        os.remove(recipes_path)
    
    # Delete and recreate ingredients.csv
    ingredients_path = os.path.join(data_dir, 'ingredients.csv')
    if os.path.exists(ingredients_path):
        print_colorful(f"🗑️  Deleting existing ingredients file: {ingredients_path}", "33")
        os.remove(ingredients_path)
    
    # Reload data
    print_colorful("🍳 Regenerating recipe data...", "36")
    recipes = load_recipes(recipes_path)
    print_colorful(f"✅ Generated {len(recipes)} recipes", "1;32")
    
    print_colorful("🥕 Regenerating ingredient data...", "36")
    ingredients = load_ingredients(ingredients_path)
    print_colorful(f"✅ Generated {len(ingredients)} ingredients", "1;32")
    
    print_colorful("\n✨ Data refresh complete! All recipe data has been regenerated.", "1;32")
    
    print("Adding additional Italian recipes to the collection...")
    from src.data.data_loader import italian_recipes
    
    # Add the Italian recipes to the recipes list if they don't exist already
    existing_names = [recipe['name'] for recipe in recipes]
    for recipe in italian_recipes:
        if recipe['name'] not in existing_names:
            recipes.append(recipe)
    
    # Save the updated recipes
    with open(recipes_path, 'w') as f:
        json.dump(recipes, f, indent=2)
    
    print(f"✅ Now have {len(recipes)} recipes including additional Italian dishes")
    
    # Count recipe types
    desserts = sum(1 for r in recipes if any("dessert" in tag.lower() for tag in r.get('tags', [])))
    italian = sum(1 for r in recipes if any("italian" in tag.lower() for tag in r.get('tags', [])))
    breakfast = sum(1 for r in recipes if any("breakfast" in tag.lower() for tag in r.get('tags', [])))
    mexican = sum(1 for r in recipes if any("mexican" in tag.lower() for tag in r.get('tags', [])))
    asian = sum(1 for r in recipes if any(tag.lower() in ["asian", "chinese", "japanese", "thai"] for tag in r.get('tags', [])))
    vegetarian = sum(1 for r in recipes if any("vegetarian" in tag.lower() for tag in r.get('tags', [])))
    
    print_colorful("\n📊 Recipe collection statistics:", "1;36")
    print_colorful(f"  • {desserts} dessert recipes", "36")
    print_colorful(f"  • {italian} Italian dishes", "36")
    print_colorful(f"  • {breakfast} breakfast options", "36")
    print_colorful(f"  • {mexican} Mexican recipes", "36")
    print_colorful(f"  • {asian} Asian dishes", "36")
    print_colorful(f"  • {vegetarian} vegetarian options", "36")

    print_colorful("\n🔍 Testing key recipe search terms...", "1;35")
    test_queries = ["dessert", "italian", "breakfast", "chocolate", "eggs, bacon"]
    
    for query in test_queries:
        matching = []
        # FIX: Changed toLowerCase() to lower()
        query_terms = [term.strip().lower() for term in query.split(",")]
        
        for recipe in recipes:
            recipe_text = " ".join([ing.lower() for ing in recipe.get("ingredients", [])])
            recipe_text += " " + " ".join([tag.lower() for tag in recipe.get('tags', [])])
            
            if any(term in recipe_text for term in query_terms):
                matching.append(recipe["name"])
        
        print_colorful(f"Query '{query}' matches {len(matching)} recipes", "33")
        if matching:
            examples = ", ".join(matching[:3])
            if len(matching) > 3:
                examples += f", and {len(matching) - 3} more"
            print_colorful(f"  Examples: {examples}", "37")

if __name__ == "__main__":
    refresh_all_data()