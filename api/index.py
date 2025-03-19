from flask import Flask, render_template, request, jsonify
import os
import json
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load data directly
def load_recipes():
    # Sample recipes
    sample_recipes = [
        {
            "name": "Margherita Pizza",
            "tags": ["italian", "pizza", "dinner", "vegetarian"],
            "ingredients": [
                "pizza dough",
                "tomato sauce",
                "fresh mozzarella",
                "fresh basil",
                "olive oil",
                "salt"
            ],
            "instructions": "1. Preheat oven to 475°F (245°C).\n2. Roll out pizza dough on a floured surface.\n3. Spread tomato sauce evenly over the dough.\n4. Tear mozzarella into pieces and distribute over sauce.\n5. Bake for 10-12 minutes until crust is golden.\n6. Remove from oven, top with fresh basil leaves and a drizzle of olive oil.\n7. Season with salt to taste.",
            "difficulty": "medium",
            "prep_time": "30 minutes"
        },
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
            "name": "Chocolate Chip Cookies",
            "tags": ["dessert", "cookies", "chocolate", "baking"],
            "ingredients": [
                "butter",
                "white sugar",
                "brown sugar",
                "eggs",
                "vanilla extract",
                "flour",
                "baking soda",
                "salt",
                "chocolate chips"
            ],
            "instructions": "1. Preheat oven to 350°F (175°C).\n2. Cream together butter and sugars until light and fluffy.\n3. Beat in eggs one at a time, then stir in vanilla.\n4. Combine flour, baking soda, and salt; gradually stir into the creamed mixture.\n5. Fold in chocolate chips.\n6. Drop by rounded tablespoons onto ungreased cookie sheets.\n7. Bake for 10-12 minutes until edges are lightly golden.",
            "difficulty": "easy",
            "prep_time": "25 minutes"
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
    return sample_recipes

# Load recipes
recipes = load_recipes()

# Simple recipe search
def search_recipes(query, recipes):
    query = query.lower()
    results = []
    
    # Search by name or tag
    for recipe in recipes:
        if query in recipe['name'].lower():
            results.append(recipe)
            continue
            
        # Search by tag
        for tag in recipe.get('tags', []):
            if query in tag.lower():
                results.append(recipe)
                break
                
    return results

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
    
    # Exact name match
    exact_recipe = next((r for r in recipes if r['name'].lower() == query.lower()), None)
    if exact_recipe:
        return render_template(
            'results.html',
            query=query,
            search_info={'ingredients': [], 'cuisines': [], 'meal_types': []},
            recipe=exact_recipe,
            error_message=None,
            alternatives=[]
        )
    
    # Search recipes
    matching_recipes = search_recipes(query, recipes)
    
    if matching_recipes:
        main_recipe = matching_recipes[0]
        alternatives = matching_recipes[1:5] if len(matching_recipes) > 1 else []
        
        # Get cuisine or meal type from query
        cuisines = []
        meal_types = []
        
        if "italian" in query.lower():
            cuisines = ["Italian"]
        elif "mexican" in query.lower():
            cuisines = ["Mexican"]
        elif "asian" in query.lower():
            cuisines = ["Asian"]
            
        if "breakfast" in query.lower():
            meal_types = ["Breakfast"]
        elif "lunch" in query.lower():
            meal_types = ["Lunch"]
        elif "dinner" in query.lower():
            meal_types = ["Dinner"]
        elif "dessert" in query.lower():
            meal_types = ["Dessert"]
            
        search_info = {
            'ingredients': [],
            'cuisines': cuisines,
            'meal_types': meal_types
        }
        
        return render_template(
            'results.html',
            query=query,
            search_info=search_info,
            recipe=main_recipe,
            error_message=None,
            alternatives=alternatives
        )
    else:
        # No recipes found
        return render_template(
            'results.html',
            query=query,
            search_info={'ingredients': [], 'cuisines': [], 'meal_types': []},
            recipe=None,
            error_message="No matching recipes found. Try another search term.",
            alternatives=[]
        )

# For Vercel serverless deployment
app.template_folder = os.path.abspath("templates")
app.static_folder = os.path.abspath("static")