from flask import Flask, render_template, request, jsonify
import os
import json
from src.data.data_loader import load_recipes, load_ingredients
from src.models.recipe_generator import RecipeGenerator
from src.models.ingredient_processor import IngredientProcessor
from src.nlp.spacy_processor import load_model, analyze_recipe_query

# Initialize Flask app
app = Flask(__name__)

# Load data and models
print("Loading data and models...")
current_dir = os.path.dirname(os.path.abspath(__file__))
recipes_path = os.path.join(current_dir, 'data', 'recipes.json')
ingredients_path = os.path.join(current_dir, 'data', 'ingredients.csv')

# Check if data files exist, if not refresh data
if not os.path.exists(recipes_path) or not os.path.exists(ingredients_path):
    print("Data files not found. Refreshing data...")
    from refresh_data import refresh_all_data
    refresh_all_data()

# Load recipes and ingredients
recipes = load_recipes(recipes_path)
ingredients_df = load_ingredients(ingredients_path)

# Add more Italian recipes directly to the recipes list
additional_italian_recipes = [
    {
        "name": "Spaghetti Carbonara",
        "tags": ["italian", "pasta", "dinner", "quick"],
        "ingredients": [
            "spaghetti",
            "eggs",
            "pancetta",
            "parmesan cheese",
            "black pepper",
            "salt"
        ],
        "instructions": "1. Cook spaghetti according to package instructions.\n2. In a bowl, whisk eggs with grated parmesan cheese.\n3. Fry pancetta until crispy.\n4. Drain pasta and immediately toss with egg mixture and pancetta.\n5. The heat from the pasta will cook the eggs into a creamy sauce.\n6. Season with black pepper and serve immediately.",
        "difficulty": "medium",
        "prep_time": "20 minutes"
    },
    {
        "name": "Lasagna alla Bolognese",
        "tags": ["italian", "pasta", "dinner", "baking", "beef"],
        "ingredients": [
            "lasagna noodles",
            "ground beef",
            "onion",
            "garlic",
            "carrot",
            "celery",
            "tomato sauce",
            "tomato paste",
            "ricotta cheese",
            "mozzarella cheese",
            "parmesan cheese",
            "eggs",
            "olive oil",
            "basil",
            "oregano",
            "salt",
            "pepper"
        ],
        "instructions": "1. Preheat oven to 375°F.\n2. Cook lasagna noodles according to package.\n3. Make Bolognese sauce: sauté onion, garlic, carrot and celery until soft.\n4. Add ground beef and cook until browned.\n5. Add tomato sauce, tomato paste, herbs, salt and pepper.\n6. Simmer for 30 minutes.\n7. Mix ricotta with egg and parmesan.\n8. In a baking dish, layer: sauce, noodles, ricotta mixture, mozzarella.\n9. Repeat layers, ending with sauce and mozzarella on top.\n10. Cover with foil and bake for 25 minutes.\n11. Remove foil and bake another 25 minutes until bubbly and golden.",
        "difficulty": "hard",
        "prep_time": "1 hour 30 minutes"
    },
    {
        "name": "Fettuccine Alfredo",
        "tags": ["italian", "dinner", "pasta", "creamy", "vegetarian"],
        "ingredients": [
            "fettuccine pasta",
            "butter",
            "heavy cream",
            "parmesan cheese",
            "garlic",
            "black pepper",
            "salt",
            "parsley"
        ],
        "instructions": "1. Cook fettuccine according to package instructions.\n2. In a large skillet, melt butter over medium heat.\n3. Add minced garlic and cook for 1 minute.\n4. Pour in heavy cream and bring to a simmer.\n5. Reduce heat and stir in grated parmesan cheese until melted and sauce is smooth.\n6. Season with salt and pepper.\n7. Drain pasta and add to the sauce, tossing to coat evenly.\n8. Garnish with chopped parsley before serving.",
        "difficulty": "easy",
        "prep_time": "20 minutes"
    }
]

# Add new recipes if they don't already exist
existing_names = [r['name'].lower() for r in recipes]
for recipe in additional_italian_recipes:
    if recipe['name'].lower() not in existing_names:
        recipes.append(recipe)
        print(f"Added recipe: {recipe['name']}")

# Initialize models
recipe_generator = RecipeGenerator()
recipe_generator.load_recipes(recipes)
ingredient_processor = IngredientProcessor()
nlp = load_model()

print(f"✅ Loaded {len(recipes)} recipes")

# Calculate recipe stats
def get_recipe_stats():
    desserts = sum(1 for r in recipes if any("dessert" in tag.lower() for tag in r.get('tags', [])))
    italian = sum(1 for r in recipes if any("italian" in tag.lower() for tag in r.get('tags', [])))
    breakfast = sum(1 for r in recipes if any("breakfast" in tag.lower() for tag in r.get('tags', [])))
    mexican = sum(1 for r in recipes if any("mexican" in tag.lower() for tag in r.get('tags', [])))
    asian = sum(1 for r in recipes if any(tag.lower() in ["asian", "chinese", "japanese", "thai"] for tag in r.get('tags', [])))
    vegetarian = sum(1 for r in recipes if any("vegetarian" in tag.lower() for tag in r.get('tags', [])))
    
    return {
        'total': len(recipes),
        'desserts': desserts,
        'italian': italian,
        'breakfast': breakfast,
        'mexican': mexican,
        'asian': asian,
        'vegetarian': vegetarian
    }

# Routes
@app.route('/')
def index():
    """Home page with search form and recipe stats"""
    stats = get_recipe_stats()
    return render_template('index.html', stats=stats)

@app.route('/search', methods=['POST'])
def search():
    """Handle recipe search"""
    query = request.form.get('query', '')
    
    # FIX 1: EXACT NAME MATCH - For "View Full Recipe" button
    # First check for exact recipe name match
    exact_recipe = None
    for recipe in recipes:
        if recipe['name'].lower() == query.lower():
            exact_recipe = recipe
            break
    
    if exact_recipe:
        # Found exact recipe match, display it
        return render_template(
            'results.html',
            query=query,
            search_info={'ingredients': [], 'cuisines': [], 'meal_types': []},
            recipe=exact_recipe,
            error_message=None,
            alternatives=[]  # No alternatives for direct recipe lookup
        )
    
    # Regular search process
    query_analysis = analyze_recipe_query(query, nlp)
    processed_ingredients = ingredient_processor.process_ingredients(query_analysis["ingredients"])
    
    # FIX 2: CUISINE SEARCH - For showing multiple Italian recipes
    # If searching for a cuisine type (like "italian")
    if query_analysis.get('cuisines') and not query_analysis.get('ingredients') and not query_analysis.get('meal_types'):
        cuisine = query_analysis['cuisines'][0].lower()
        matching_recipes = []
        
        # Find all recipes matching this cuisine
        for recipe in recipes:
            if any(cuisine in tag.lower() for tag in recipe.get('tags', [])):
                matching_recipes.append(recipe)
        
        if matching_recipes:
            # Show first matching recipe as the main recipe
            main_recipe = matching_recipes[0]
            
            # Use the rest as alternatives
            alternatives = matching_recipes[1:7] if len(matching_recipes) > 1 else []
            
            return render_template(
                'results.html',
                query=query,
                search_info={'ingredients': [], 'cuisines': query_analysis['cuisines'], 'meal_types': []},
                recipe=main_recipe,
                error_message=None,
                alternatives=alternatives
            )
    
    # Standard recipe search
    recipe = recipe_generator.generate_recipe(query_analysis)
    
    # Generate alternatives (if recipe found)
    alternatives = []
    if isinstance(recipe, dict):
        alternatives = recipe_generator.get_recipe_suggestions(query_analysis, limit=6)
        # Remove the main recipe from alternatives
        alternatives = [r for r in alternatives if r.get('name') != recipe.get('name')]
    
    search_info = {
        'ingredients': processed_ingredients,
        'cuisines': query_analysis.get('cuisines', []),
        'meal_types': query_analysis.get('meal_types', [])
    }
    
    return render_template(
        'results.html',
        query=query,
        search_info=search_info,
        recipe=recipe if isinstance(recipe, dict) else None,
        error_message=recipe if isinstance(recipe, str) else None,
        alternatives=alternatives[:6]  # Show up to 6 alternatives
    )

if __name__ == '__main__':
    app.run(debug=True)

# random
