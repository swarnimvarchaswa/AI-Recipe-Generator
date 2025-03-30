import os
import sys
import time
from src.models.recipe_generator import RecipeGenerator
from src.models.ingredient_processor import IngredientProcessor
from src.data.data_loader import load_recipes, load_ingredients
from src.nlp.spacy_processor import analyze_recipe_query, load_model

def print_colorful(text, color_code=None):
    """Print with ANSI color codes if supported."""
    if color_code and sys.stdout.isatty():
        print(f"\033[{color_code}m{text}\033[0m")
    else:
        print(text)

def print_recipe(recipe):
    """Print a recipe in a nicely formatted way."""
    if not recipe:
        print_colorful("No recipe available.", "31")  # Red text
        return
        
    if isinstance(recipe, str):
        print_colorful(recipe, "31")  # Red text
        return
        
    print("\n" + "=" * 60)
    print_colorful(f"🍽️  {recipe.get('name', 'Unnamed Recipe')}  🍽️", "1;33")  # Bold yellow
    
    if "tags" in recipe and recipe["tags"]:
        tags = ", ".join(recipe["tags"])
        print_colorful(f"Tags: {tags}", "36")  # Cyan text

    if "difficulty" in recipe:
        print(f"Difficulty: {recipe['difficulty'].capitalize()}")
        
    if "prep_time" in recipe:
        print(f"Prep Time: {recipe['prep_time']}")
    
    print("-" * 60)
    print_colorful("📋 Ingredients:", "1;32")  # Bold green
    for ing in recipe.get('ingredients', []):
        print(f"  • {ing}")
    
    print("-" * 60)
    print_colorful("👨‍🍳 Instructions:", "1;34")  # Bold blue
    print(recipe.get('instructions', 'No instructions available.'))
    print("=" * 60 + "\n")

def print_recipe_stats(recipes):
    """Print statistics about loaded recipes."""
    if not recipes:
        print_colorful("No recipes loaded! Please check your data files.", "31")
        return
        
    print_colorful(f"✅ Loaded {len(recipes)} recipes", "1;32")
    
    # Count recipe types
    desserts = sum(1 for r in recipes if any("dessert" in tag.lower() for tag in r.get('tags', [])))
    italian = sum(1 for r in recipes if any("italian" in tag.lower() for tag in r.get('tags', [])))
    breakfast = sum(1 for r in recipes if any("breakfast" in tag.lower() for tag in r.get('tags', [])))
    mexican = sum(1 for r in recipes if any("mexican" in tag.lower() for tag in r.get('tags', [])))
    asian = sum(1 for r in recipes if any(tag.lower() in ["asian", "chinese", "japanese", "thai"] for tag in r.get('tags', [])))
    vegetarian = sum(1 for r in recipes if any("vegetarian" in tag.lower() for tag in r.get('tags', [])))
    
    print_colorful("Recipe collection includes:", "1;36")
    print_colorful(f"  • {desserts} dessert recipes", "36")
    print_colorful(f"  • {italian} Italian dishes", "36")
    print_colorful(f"  • {breakfast} breakfast options", "36")
    print_colorful(f"  • {mexican} Mexican recipes", "36")
    print_colorful(f"  • {asian} Asian dishes", "36")
    print_colorful(f"  • {vegetarian} vegetarian options", "36")
    print()

def main():
    """Main function for the AI Recipe Generator."""
    # Load recipes and ingredients
    current_dir = os.path.dirname(os.path.abspath(__file__))
    recipes_path = os.path.join(current_dir, 'data', 'recipes.json')
    ingredients_path = os.path.join(current_dir, 'data', 'ingredients.csv')
    
    print_colorful("Loading data and models...", "36")  # Cyan text
    recipes = load_recipes(recipes_path)
    ingredients_df = load_ingredients(ingredients_path)
    
    # Initialize processors
    nlp = load_model()
    ingredient_processor = IngredientProcessor()
    recipe_generator = RecipeGenerator()
    recipe_generator.load_recipes(recipes)
    
    # NEW: Print recipe stats at startup
    print_recipe_stats(recipes)
    
    # Interactive mode
    print_colorful("\n🍳 Welcome to the AI Recipe Generator! 🍳", "1;35")  # Bold magenta
    print("Enter ingredients or ask for a specific dish (or type 'exit' to quit).")
    print("Examples:")
    print("  - chicken, rice, bell pepper")
    print("  - vegetarian dinner with pasta")
    print("  - dessert with chocolate")
    
    while True:
        print()
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print_colorful("Thank you for using the AI Recipe Generator! Goodbye! 👋", "1;35")
            break
        
        if not user_input.strip():
            continue
            
        # Process user query
        print_colorful("Analyzing your request...", "36")
        
        # Use NLP to extract ingredients and preferences
        query_analysis = analyze_recipe_query(user_input, nlp)
        
        # Debug info
        print(f"DEBUG: Query analysis: {query_analysis}")
        print(f"DEBUG: Total recipes loaded: {len(recipe_generator.recipes)}")

        # If comma-separated list, treat as direct ingredients list
        if "," in user_input:
            direct_ingredients = [ing.strip() for ing in user_input.split(',')]
            if direct_ingredients:
                query_analysis["ingredients"] = direct_ingredients

        # Process the extracted ingredients for display
        processed_ingredients = ingredient_processor.process_ingredients(query_analysis["ingredients"])

        if not processed_ingredients and not query_analysis["cuisines"] and not query_analysis["meal_types"]:
            print_colorful("I couldn't identify any ingredients or meal types. Please try again with more specific information.", "31")
            continue

        # Show what we're looking for
        if processed_ingredients:
            print(f"Looking for recipes with: {', '.join(processed_ingredients)}")

        if query_analysis["cuisines"]:
            print(f"Cuisine type: {', '.join(query_analysis['cuisines'])}")
            
        if query_analysis["meal_types"]:
            print(f"Meal type: {', '.join(query_analysis['meal_types'])}")

        # Generate recipe
        generated_recipe = recipe_generator.generate_recipe(query_analysis)
        
        # Print the generated recipe
        print_recipe(generated_recipe)
        
        # Additional features
        if isinstance(generated_recipe, dict):
            # Suggest alternatives
            print_colorful("Would you like to see alternative recipes? (y/n)", "1;33")
            alt_response = input("> ").lower()
            if alt_response == 'y':
                # THIS IS THE FIX - pass query_analysis instead of processed_ingredients
                alternatives = recipe_generator.get_recipe_suggestions(query_analysis, limit=2)
                # Remove the already shown recipe
                alternatives = [r for r in alternatives if r.get('name') != generated_recipe.get('name')]
                
                if alternatives:
                    for alt in alternatives:
                        print_recipe(alt)
                else:
                    print_colorful("No alternative recipes found.", "31")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_colorful("\nThank you for using the AI Recipe Generator! Goodbye! 👋", "1;35")
    except Exception as e:
        print_colorful(f"An error occurred: {e}", "31")

