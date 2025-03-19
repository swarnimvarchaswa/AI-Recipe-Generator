def log_message(message):
    print(f"[LOG] {message}")

def validate_ingredients(ingredients):
    if not isinstance(ingredients, list):
        raise ValueError("Ingredients should be provided as a list.")
    if not all(isinstance(ingredient, str) for ingredient in ingredients):
        raise ValueError("All ingredients must be strings.")
    return True

def format_recipe_output(recipe):
    if not isinstance(recipe, dict):
        raise ValueError("Recipe should be a dictionary.")
    return f"Recipe: {recipe.get('title', 'Untitled')}\nIngredients: {', '.join(recipe.get('ingredients', []))}\nInstructions: {recipe.get('instructions', 'No instructions provided.')}"