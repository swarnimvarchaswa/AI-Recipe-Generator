import os
import json
import pandas as pd

def load_recipes(file_path):
    """Load recipes from a JSON file."""
    try:
        if not os.path.exists(file_path):
            print(f"Warning: Recipe file {file_path} not found. Creating a sample file.")
            # Create an expanded recipe database with 30+ recipes
            sample_recipes = [
                # BREAKFAST RECIPES
                {
                    "name": "Classic Pancakes",
                    "ingredients": ["flour", "milk", "eggs", "sugar", "baking powder", "salt", "butter", "vanilla extract"],
                    "instructions": "1. Mix dry ingredients in a bowl.\n2. In another bowl, whisk milk, eggs, melted butter, and vanilla.\n3. Combine wet and dry ingredients.\n4. Cook spoonfuls of batter on a hot griddle until bubbles form, then flip.\n5. Serve with maple syrup.",
                    "tags": ["breakfast", "sweet", "american", "family-friendly"],
                    "difficulty": "easy",
                    "prep_time": "20 minutes"
                },
                {
                    "name": "Avocado Toast",
                    "ingredients": ["bread", "avocado", "lemon juice", "salt", "red pepper flakes", "eggs"],
                    "instructions": "1. Toast bread slices.\n2. Mash avocado with lemon juice and salt.\n3. Spread on toast and sprinkle with red pepper flakes.\n4. Optional: top with a fried or poached egg.",
                    "tags": ["breakfast", "healthy", "vegetarian", "quick"],
                    "difficulty": "easy",
                    "prep_time": "10 minutes"
                },
                {
                    "name": "Classic Omelette",
                    "ingredients": ["eggs", "milk", "cheese", "butter", "salt", "pepper"],
                    "instructions": "1. Beat eggs with milk, salt, and pepper.\n2. Melt butter in a pan.\n3. Pour in egg mixture and cook until set.\n4. Sprinkle cheese on top and fold.\n5. Cook until cheese melts.",
                    "tags": ["breakfast", "quick", "high-protein", "vegetarian"],
                    "difficulty": "easy",
                    "prep_time": "10 minutes"
                },
                {
                    "name": "Overnight Oats",
                    "ingredients": ["rolled oats", "milk", "yogurt", "chia seeds", "honey", "berries", "nuts"],
                    "instructions": "1. Mix oats, milk, yogurt, chia seeds, and honey.\n2. Refrigerate overnight in a jar.\n3. Top with fresh berries and nuts before serving.",
                    "tags": ["breakfast", "healthy", "vegetarian", "no-cook", "make-ahead"],
                    "difficulty": "easy",
                    "prep_time": "5 minutes + overnight"
                },
                {
                    "name": "Breakfast Burrito",
                    "ingredients": ["eggs", "tortillas", "cheese", "bacon", "salsa", "avocado", "bell pepper", "onion"],
                    "instructions": "1. Cook bacon until crispy.\n2. Sauté bell pepper and onion until soft.\n3. Scramble eggs with vegetables.\n4. Warm tortillas.\n5. Fill tortillas with egg mixture, cheese, salsa, and avocado slices.\n6. Roll up and serve.",
                    "tags": ["breakfast", "mexican", "high-protein", "savory"],
                    "difficulty": "medium",
                    "prep_time": "25 minutes"
                },

                # ITALIAN CUISINE
                {
                    "name": "Classic Margherita Pizza",
                    "ingredients": ["pizza dough", "tomato sauce", "fresh mozzarella", "basil", "olive oil", "salt"],
                    "instructions": "1. Preheat oven to 475°F.\n2. Roll out pizza dough.\n3. Spread tomato sauce and top with sliced fresh mozzarella.\n4. Bake for 10-12 minutes until crust is golden.\n5. Top with fresh basil leaves and drizzle with olive oil.",
                    "tags": ["italian", "dinner", "vegetarian", "baking"],
                    "difficulty": "medium",
                    "prep_time": "25 minutes"
                },
                {
                    "name": "Spaghetti Carbonara",
                    "ingredients": ["spaghetti", "eggs", "bacon", "parmesan cheese", "black pepper", "salt"],
                    "instructions": "1. Cook spaghetti according to package instructions.\n2. Fry bacon until crispy.\n3. Beat eggs with grated parmesan.\n4. Mix hot pasta with bacon, then quickly stir in egg mixture.\n5. Season with black pepper and salt.",
                    "tags": ["italian", "dinner", "pasta", "quick"],
                    "difficulty": "medium",
                    "prep_time": "20 minutes"
                },
                {
                    "name": "Fettuccine Alfredo",
                    "ingredients": ["fettuccine pasta", "butter", "heavy cream", "parmesan cheese", "garlic", "parsley", "black pepper"],
                    "instructions": "1. Cook pasta according to package instructions.\n2. In a pan, melt butter and sauté garlic.\n3. Add cream and bring to a simmer.\n4. Stir in parmesan cheese until melted.\n5. Toss with pasta and season with pepper.\n6. Garnish with parsley.",
                    "tags": ["italian", "dinner", "pasta", "creamy", "vegetarian"],
                    "difficulty": "medium",
                    "prep_time": "20 minutes"
                },
                {
                    "name": "Classic Lasagna",
                    "ingredients": ["lasagna noodles", "ground beef", "onion", "garlic", "tomato sauce", "ricotta cheese", "mozzarella cheese", "parmesan cheese", "eggs", "parsley", "basil"],
                    "instructions": "1. Brown beef with onion and garlic.\n2. Add tomato sauce and simmer.\n3. Mix ricotta, egg, and parsley.\n4. Layer sauce, noodles, ricotta mix, and mozzarella in baking dish.\n5. Repeat layers and top with parmesan.\n6. Bake at 375°F for 45 minutes.",
                    "tags": ["italian", "dinner", "baked", "family-friendly"],
                    "difficulty": "medium",
                    "prep_time": "1 hour 15 minutes"
                },
                {
                    "name": "Mushroom Risotto",
                    "ingredients": ["arborio rice", "mushrooms", "onion", "garlic", "white wine", "vegetable broth", "parmesan cheese", "butter", "olive oil", "thyme"],
                    "instructions": "1. Sauté mushrooms until golden and set aside.\n2. Cook onion and garlic in butter and oil.\n3. Add rice and toast for 2 minutes.\n4. Add wine and stir until absorbed.\n5. Add hot broth gradually, stirring constantly.\n6. When rice is creamy, stir in mushrooms, parmesan, and thyme.",
                    "tags": ["italian", "dinner", "vegetarian", "rice dish"],
                    "difficulty": "hard",
                    "prep_time": "45 minutes"
                },

                # MEXICAN CUISINE
                {
                    "name": "Chicken Fajitas",
                    "ingredients": ["chicken breast", "bell peppers", "onion", "lime", "cumin", "paprika", "chili powder", "tortillas", "sour cream", "guacamole", "salsa"],
                    "instructions": "1. Slice chicken and vegetables into strips.\n2. Season chicken with spices and lime juice.\n3. Cook chicken in a hot skillet until done.\n4. Sauté vegetables until tender-crisp.\n5. Serve with warm tortillas and toppings.",
                    "tags": ["mexican", "dinner", "high-protein", "quick"],
                    "difficulty": "easy",
                    "prep_time": "30 minutes"
                },
                {
                    "name": "Guacamole",
                    "ingredients": ["avocado", "lime juice", "red onion", "tomato", "cilantro", "jalapeño", "salt", "garlic"],
                    "instructions": "1. Mash avocados in a bowl.\n2. Mix in lime juice, finely diced onion, tomato, cilantro, and jalapeño.\n3. Add minced garlic and salt to taste.\n4. Let sit for 15 minutes before serving.",
                    "tags": ["mexican", "appetizer", "dip", "vegetarian", "vegan"],
                    "difficulty": "easy",
                    "prep_time": "15 minutes"
                },
                {
                    "name": "Beef Enchiladas",
                    "ingredients": ["ground beef", "onion", "garlic", "enchilada sauce", "tortillas", "cheese", "black olives", "green onions"],
                    "instructions": "1. Brown beef, onion, and garlic.\n2. Mix in some enchilada sauce.\n3. Fill tortillas with beef mixture, roll up, and place in baking dish.\n4. Pour remaining sauce over enchiladas and top with cheese.\n5. Bake at 350°F for 20 minutes.\n6. Garnish with olives and green onions.",
                    "tags": ["mexican", "dinner", "baked", "family-friendly"],
                    "difficulty": "medium",
                    "prep_time": "45 minutes"
                },
                {
                    "name": "Chicken Quesadillas",
                    "ingredients": ["tortillas", "chicken", "cheese", "bell pepper", "onion", "sour cream", "salsa", "avocado"],
                    "instructions": "1. Cook diced chicken with vegetables and spices.\n2. Place mixture on half of a tortilla and sprinkle with cheese.\n3. Fold tortilla and cook in a skillet until golden on both sides.\n4. Cut into wedges and serve with sour cream, salsa, and avocado.",
                    "tags": ["mexican", "lunch", "dinner", "quick", "family-friendly"],
                    "difficulty": "easy",
                    "prep_time": "25 minutes"
                },

                # ASIAN CUISINE
                {
                    "name": "Vegetable Stir Fry",
                    "ingredients": ["broccoli", "carrot", "bell pepper", "onion", "garlic", "ginger", "soy sauce", "sesame oil", "rice"],
                    "instructions": "1. Cook rice according to package instructions.\n2. Heat oil in a wok or large pan.\n3. Add garlic and ginger, stir for 30 seconds.\n4. Add vegetables and stir fry for 5-7 minutes.\n5. Add soy sauce and continue cooking for 2 minutes.\n6. Serve over rice.",
                    "tags": ["asian", "chinese", "dinner", "vegetarian", "vegan", "healthy"],
                    "difficulty": "easy",
                    "prep_time": "25 minutes"
                },
                {
                    "name": "Chicken Fried Rice",
                    "ingredients": ["rice", "chicken", "eggs", "peas", "carrots", "onion", "garlic", "soy sauce", "sesame oil"],
                    "instructions": "1. Cook rice and let it cool.\n2. Scramble eggs in a pan and set aside.\n3. Stir-fry chicken until cooked.\n4. Add vegetables and cook until tender.\n5. Mix in rice, soy sauce, and scrambled eggs.\n6. Drizzle with sesame oil before serving.",
                    "tags": ["asian", "chinese", "dinner", "leftover-friendly"],
                    "difficulty": "medium",
                    "prep_time": "30 minutes"
                },
                {
                    "name": "Beef and Broccoli",
                    "ingredients": ["beef strips", "broccoli", "garlic", "ginger", "soy sauce", "oyster sauce", "cornstarch", "rice"],
                    "instructions": "1. Marinate beef in soy sauce, garlic, and ginger.\n2. Mix cornstarch with water to create a slurry.\n3. Stir-fry beef until browned and set aside.\n4. Steam broccoli until bright green.\n5. Stir-fry everything together with sauce and slurry until thickened.\n6. Serve over rice.",
                    "tags": ["asian", "chinese", "dinner", "high-protein"],
                    "difficulty": "medium",
                    "prep_time": "35 minutes"
                },
                {
                    "name": "Pad Thai",
                    "ingredients": ["rice noodles", "chicken", "shrimp", "tofu", "eggs", "bean sprouts", "green onions", "peanuts", "lime", "fish sauce", "tamarind paste", "sugar", "garlic"],
                    "instructions": "1. Soak rice noodles in hot water until soft.\n2. Mix fish sauce, tamarind paste, and sugar to make sauce.\n3. Stir-fry garlic, chicken, shrimp, and tofu.\n4. Push to one side and scramble eggs in the same pan.\n5. Add noodles and sauce mixture.\n6. Toss in bean sprouts and green onions.\n7. Serve with lime and crushed peanuts.",
                    "tags": ["asian", "thai", "dinner", "spicy"],
                    "difficulty": "hard",
                    "prep_time": "40 minutes"
                },

                # DESSERTS
                {
                    "name": "Chocolate Chip Cookies",
                    "ingredients": ["flour", "butter", "sugar", "brown sugar", "eggs", "vanilla extract", "baking soda", "salt", "chocolate chips"],
                    "instructions": "1. Preheat oven to 350°F.\n2. Cream together butter and sugars.\n3. Beat in eggs and vanilla.\n4. Mix in flour, baking soda, and salt.\n5. Stir in chocolate chips.\n6. Drop spoonfuls onto baking sheets.\n7. Bake for 10-12 minutes.",
                    "tags": ["dessert", "baking", "cookies", "chocolate", "sweet"],
                    "difficulty": "easy",
                    "prep_time": "30 minutes"
                },
                {
                    "name": "Chocolate Brownie",
                    "ingredients": ["butter", "sugar", "eggs", "vanilla extract", "flour", "cocoa powder", "salt", "chocolate chips"],
                    "instructions": "1. Preheat oven to 350°F and grease a baking pan.\n2. Melt butter, then stir in sugar, eggs, and vanilla.\n3. Mix in dry ingredients until just combined.\n4. Fold in chocolate chips.\n5. Pour into pan and bake for 25-30 minutes.\n6. Cool before cutting into squares.",
                    "tags": ["dessert", "baking", "chocolate", "sweet"],
                    "difficulty": "easy",
                    "prep_time": "40 minutes"
                },
                {
                    "name": "Apple Pie",
                    "ingredients": ["pie crust", "apples", "sugar", "cinnamon", "nutmeg", "lemon juice", "butter", "flour", "salt"],
                    "instructions": "1. Preheat oven to 425°F.\n2. Peel and slice apples, toss with sugar, cinnamon, nutmeg, lemon juice, and flour.\n3. Line pie dish with bottom crust.\n4. Fill with apple mixture and dot with butter.\n5. Cover with top crust, seal edges, and cut vents.\n6. Bake for 45-50 minutes until golden brown.",
                    "tags": ["dessert", "baking", "pie", "fruit", "american"],
                    "difficulty": "medium",
                    "prep_time": "1 hour"
                },
                {
                    "name": "Tiramisu",
                    "ingredients": ["ladyfingers", "espresso", "mascarpone cheese", "eggs", "sugar", "cocoa powder", "rum"],
                    "instructions": "1. Mix espresso with rum in a shallow dish.\n2. Beat egg yolks with sugar until creamy.\n3. Fold in mascarpone cheese.\n4. In another bowl, beat egg whites until stiff peaks form and fold into mascarpone mixture.\n5. Dip ladyfingers in espresso mixture and layer in dish.\n6. Spread half the mascarpone mixture on top.\n7. Repeat layers and dust with cocoa powder.\n8. Refrigerate for at least 4 hours.",
                    "tags": ["dessert", "italian", "no-bake", "chocolate", "coffee"],
                    "difficulty": "medium",
                    "prep_time": "30 minutes + 4 hours chilling"
                },
                {
                    "name": "Chocolate Mousse",
                    "ingredients": ["chocolate", "eggs", "sugar", "heavy cream", "butter", "vanilla extract", "salt"],
                    "instructions": "1. Melt chocolate and butter together.\n2. Beat egg yolks with sugar until pale.\n3. Fold chocolate mixture into egg mixture.\n4. Whip cream until soft peaks form.\n5. Fold whipped cream into chocolate mixture.\n6. Chill for at least 2 hours.\n7. Serve with additional whipped cream if desired.",
                    "tags": ["dessert", "chocolate", "french", "creamy", "make-ahead"],
                    "difficulty": "medium",
                    "prep_time": "25 minutes + 2 hours chilling"
                },

                # SOUPS AND STEWS
                {
                    "name": "Classic Chicken Soup",
                    "ingredients": ["chicken", "carrots", "celery", "onion", "garlic", "chicken broth", "noodles", "parsley", "bay leaf", "salt", "pepper"],
                    "instructions": "1. Cook chicken in broth until done, then remove and shred.\n2. Add vegetables and simmer until tender.\n3. Return chicken to pot and add noodles.\n4. Cook until noodles are tender.\n5. Season with salt and pepper.\n6. Garnish with fresh parsley.",
                    "tags": ["soup", "comfort food", "american", "dinner", "healthy"],
                    "difficulty": "medium",
                    "prep_time": "1 hour"
                },
                {
                    "name": "Tomato Soup",
                    "ingredients": ["tomatoes", "onion", "garlic", "vegetable broth", "basil", "cream", "butter", "sugar", "salt", "pepper"],
                    "instructions": "1. Sauté onions and garlic in butter.\n2. Add diced tomatoes and cook for 5 minutes.\n3. Pour in vegetable broth and simmer for 15 minutes.\n4. Blend until smooth.\n5. Stir in cream, sugar, salt, and pepper.\n6. Garnish with fresh basil.",
                    "tags": ["soup", "vegetarian", "comfort food", "lunch", "dinner"],
                    "difficulty": "easy",
                    "prep_time": "30 minutes"
                },
                {
                    "name": "Beef Stew",
                    "ingredients": ["beef chuck", "potatoes", "carrots", "onion", "celery", "garlic", "beef broth", "tomato paste", "flour", "bay leaf", "thyme", "red wine"],
                    "instructions": "1. Toss beef cubes in seasoned flour.\n2. Brown beef in a pot.\n3. Add onions, garlic, and celery, cook until soft.\n4. Pour in wine and broth, add bay leaf and thyme.\n5. Simmer for 1.5 hours.\n6. Add potatoes and carrots, cook for another 45 minutes.\n7. Season to taste.",
                    "tags": ["stew", "dinner", "comfort food", "winter"],
                    "difficulty": "medium",
                    "prep_time": "3 hours"
                },
                {
                    "name": "Minestrone Soup",
                    "ingredients": ["onion", "carrot", "celery", "zucchini", "tomatoes", "beans", "pasta", "vegetable broth", "parmesan cheese", "parsley", "olive oil", "garlic"],
                    "instructions": "1. Sauté onions, carrots, celery, and garlic in olive oil.\n2. Add tomatoes and broth, bring to a simmer.\n3. Add zucchini and beans, cook for 10 minutes.\n4. Add pasta and cook until tender.\n5. Serve with parmesan cheese and parsley.",
                    "tags": ["soup", "italian", "vegetarian", "healthy", "dinner"],
                    "difficulty": "easy",
                    "prep_time": "45 minutes"
                },

                # SALADS
                {
                    "name": "Caesar Salad",
                    "ingredients": ["romaine lettuce", "parmesan cheese", "croutons", "eggs", "garlic", "lemon juice", "olive oil", "dijon mustard", "worcestershire sauce", "anchovy paste", "salt", "pepper"],
                    "instructions": "1. Make dressing by whisking egg yolk, garlic, lemon juice, mustard, anchovy paste, and worcestershire sauce.\n2. Slowly add olive oil while whisking.\n3. Toss lettuce with dressing.\n4. Add croutons and shaved parmesan cheese.",
                    "tags": ["salad", "appetizer", "lunch", "vegetarian"],
                    "difficulty": "easy",
                    "prep_time": "20 minutes"
                },
                {
                    "name": "Greek Salad",
                    "ingredients": ["cucumber", "tomato", "red onion", "bell pepper", "kalamata olives", "feta cheese", "olive oil", "lemon juice", "oregano", "salt"],
                    "instructions": "1. Chop vegetables into chunks.\n2. Combine in a bowl with olives.\n3. Whisk together olive oil, lemon juice, oregano, and salt.\n4. Pour dressing over salad and toss gently.\n5. Top with crumbled feta cheese.",
                    "tags": ["salad", "greek", "mediterranean", "vegetarian", "healthy", "lunch"],
                    "difficulty": "easy",
                    "prep_time": "15 minutes"
                },
                {
                    "name": "Cobb Salad",
                    "ingredients": ["lettuce", "chicken", "bacon", "eggs", "avocado", "tomato", "blue cheese", "red wine vinegar", "dijon mustard", "olive oil", "salt", "pepper"],
                    "instructions": "1. Arrange lettuce on a platter.\n2. Arrange rows of chicken, bacon, eggs, avocado, tomato, and blue cheese.\n3. Mix vinegar, mustard, oil, salt, and pepper for dressing.\n4. Drizzle dressing over salad before serving.",
                    "tags": ["salad", "american", "lunch", "dinner", "high-protein"],
                    "difficulty": "easy",
                    "prep_time": "30 minutes"
                },

                # OTHER POPULAR DISHES
                {
                    "name": "Classic Burger",
                    "ingredients": ["ground beef", "salt", "pepper", "hamburger buns", "lettuce", "tomato", "onion", "pickles", "cheese", "ketchup", "mustard", "mayonnaise"],
                    "instructions": "1. Season beef with salt and pepper, form into patties.\n2. Grill or pan-fry patties to desired doneness.\n3. Toast buns lightly.\n4. Assemble burgers with your choice of toppings and condiments.",
                    "tags": ["american", "dinner", "lunch", "grilled", "sandwich"],
                    "difficulty": "easy",
                    "prep_time": "25 minutes"
                },
                {
                    "name": "Roast Chicken",
                    "ingredients": ["whole chicken", "butter", "garlic", "lemon", "rosemary", "thyme", "salt", "pepper", "olive oil"],
                    "instructions": "1. Preheat oven to 425°F.\n2. Mix softened butter with herbs, garlic, lemon zest, salt, and pepper.\n3. Rub mixture under and over chicken skin.\n4. Place lemon halves in cavity.\n5. Roast for 1 hour 15 minutes or until done.\n6. Let rest before carving.",
                    "tags": ["dinner", "roasted", "high-protein", "family-friendly"],
                    "difficulty": "medium",
                    "prep_time": "1 hour 30 minutes"
                },
                {
                    "name": "Hummus",
                    "ingredients": ["chickpeas", "tahini", "lemon juice", "garlic", "olive oil", "cumin", "salt", "paprika"],
                    "instructions": "1. Drain and rinse chickpeas.\n2. Blend chickpeas, tahini, lemon juice, garlic, and cumin in a food processor.\n3. While blending, drizzle in olive oil until smooth.\n4. Add salt to taste.\n5. Serve with a sprinkle of paprika and a drizzle of olive oil.",
                    "tags": ["mediterranean", "appetizer", "vegetarian", "vegan", "dip"],
                    "difficulty": "easy",
                    "prep_time": "10 minutes"
                },
                {
                    "name": "Sushi Rolls",
                    "ingredients": ["sushi rice", "nori sheets", "cucumber", "avocado", "crab meat", "rice vinegar", "sugar", "salt", "soy sauce", "wasabi", "pickled ginger"],
                    "instructions": "1. Cook rice and season with vinegar, sugar, and salt.\n2. Place nori on bamboo mat, spread rice on top.\n3. Add fillings in a line.\n4. Roll tightly using the mat.\n5. Cut into bite-sized pieces.\n6. Serve with soy sauce, wasabi, and pickled ginger.",
                    "tags": ["japanese", "asian", "seafood", "dinner"],
                    "difficulty": "hard",
                    "prep_time": "1 hour"
                },
                {
                    "name": "Chicken Curry",
                    "ingredients": ["chicken", "onion", "garlic", "ginger", "curry powder", "coconut milk", "tomatoes", "cilantro", "rice", "salt"],
                    "instructions": "1. Sauté onion, garlic, and ginger until soft.\n2. Add chicken and cook until browned.\n3. Stir in curry powder and cook for 1 minute.\n4. Add tomatoes and coconut milk, simmer for 20 minutes.\n5. Season with salt.\n6. Garnish with cilantro and serve with rice.",
                    "tags": ["indian", "asian", "dinner", "spicy"],
                    "difficulty": "medium",
                    "prep_time": "40 minutes"
                },
                {
                    "name": "Mac and Cheese",
                    "ingredients": ["macaroni", "butter", "flour", "milk", "cheddar cheese", "parmesan cheese", "breadcrumbs", "salt", "pepper", "nutmeg"],
                    "instructions": "1. Cook macaroni according to package instructions.\n2. In a saucepan, melt butter and stir in flour to make a roux.\n3. Gradually add milk, stirring until thickened.\n4. Add cheese and stir until melted.\n5. Mix in cooked macaroni.\n6. Top with breadcrumbs and more cheese.\n7. Bake at 350°F for 20-25 minutes until golden.",
                    "tags": ["american", "dinner", "comfort food", "vegetarian", "pasta", "baked", "family-friendly"],
                    "difficulty": "medium",
                    "prep_time": "45 minutes"
                }
            ]

            # New Italian recipes to add to your collection
            italian_recipes = [
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
                    "name": "Chicken Parmigiana",
                    "tags": ["italian", "dinner", "chicken", "baking"],
                    "ingredients": [
                        "chicken breasts",
                        "breadcrumbs",
                        "parmesan cheese",
                        "mozzarella cheese",
                        "eggs",
                        "tomato sauce",
                        "basil",
                        "olive oil",
                        "salt",
                        "pepper"
                    ],
                    "instructions": "1. Preheat oven to 425°F.\n2. Pound chicken breasts to even thickness.\n3. Dip chicken in beaten eggs, then coat with mixture of breadcrumbs and parmesan.\n4. Heat olive oil in a skillet and brown chicken on both sides.\n5. Place chicken in a baking dish, top with tomato sauce and mozzarella.\n6. Bake for 15-20 minutes until cheese is bubbly and chicken cooked through.\n7. Garnish with fresh basil.",
                    "difficulty": "medium",
                    "prep_time": "40 minutes"
                },
                {
                    "name": "Risotto ai Funghi",
                    "tags": ["italian", "dinner", "vegetarian", "rice"],
                    "ingredients": [
                        "arborio rice",
                        "mushrooms",
                        "onion",
                        "garlic",
                        "white wine",
                        "vegetable broth",
                        "parmesan cheese",
                        "butter",
                        "olive oil",
                        "parsley",
                        "salt",
                        "pepper"
                    ],
                    "instructions": "1. Heat broth in a saucepan and keep warm.\n2. Sauté chopped onion and garlic in olive oil until translucent.\n3. Add sliced mushrooms and cook until soft.\n4. Add rice and stir for 2 minutes until translucent around edges.\n5. Pour in wine and stir until absorbed.\n6. Add warm broth one ladle at a time, stirring frequently.\n7. Continue adding broth until rice is creamy and al dente (about 18-20 minutes).\n8. Remove from heat, stir in butter and parmesan.\n9. Season with salt and pepper and garnish with parsley.",
                    "difficulty": "hard",
                    "prep_time": "35 minutes"
                },
                {
                    "name": "Tiramisu",
                    "tags": ["italian", "dessert", "no-bake", "coffee"],
                    "ingredients": [
                        "mascarpone cheese",
                        "eggs",
                        "sugar",
                        "espresso coffee",
                        "ladyfinger biscuits",
                        "cocoa powder",
                        "vanilla extract"
                    ],
                    "instructions": "1. Separate eggs. Beat yolks with sugar until pale and fluffy.\n2. Add mascarpone and vanilla, mix until smooth.\n3. In another bowl, beat egg whites until stiff peaks form.\n4. Gently fold egg whites into mascarpone mixture.\n5. Dip ladyfingers quickly in coffee and arrange in serving dish.\n6. Spread half the mascarpone mixture over the ladyfingers.\n7. Add another layer of coffee-dipped ladyfingers.\n8. Top with remaining mascarpone mixture.\n9. Dust with cocoa powder and refrigerate for at least 4 hours.",
                    "difficulty": "medium",
                    "prep_time": "30 minutes plus 4 hours chilling"
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
                }
            ]

            sample_recipes.extend(italian_recipes)

            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(sample_recipes, f, indent=4)
            return sample_recipes
        
        with open(file_path, 'r') as f:
            recipes = json.load(f)
        return recipes
    except Exception as e:
        print(f"Error loading recipes: {e}")
        return []

def load_ingredients(file_path):
    """Load ingredients from a CSV file."""
    try:
        if not os.path.exists(file_path):
            print(f"Warning: Ingredients file {file_path} not found. Creating a sample file.")
            # Create a comprehensive ingredients file with categories
            sample_data = {
                "name": [
                    # Proteins
                    "chicken", "beef", "pork", "turkey", "eggs", "tofu", "shrimp", "fish", "lamb", "chickpeas",
                    # Dairy
                    "milk", "cheese", "butter", "yogurt", "cream", "sour cream", "ricotta", "parmesan", "mozzarella", "feta",
                    # Vegetables
                    "tomato", "onion", "garlic", "bell pepper", "carrot", "broccoli", "spinach", "lettuce", "potato", 
                    "zucchini", "cucumber", "mushrooms", "corn", "peas", "kale", "sweet potato", "celery", "avocado",
                    # Fruits
                    "apple", "banana", "orange", "lemon", "lime", "berries", "grapes", "melon", "pineapple", "mango",
                    # Grains & Starches
                    "rice", "pasta", "flour", "bread", "oats", "quinoa", "couscous", "tortillas", "noodles", "barley",
                    # Herbs & Spices
                    "basil", "oregano", "thyme", "rosemary", "cilantro", "mint", "parsley", "cinnamon", "cumin", 
                    "paprika", "turmeric", "ginger", "salt", "pepper", "nutmeg", "curry powder", "bay leaf", "chili powder",
                    # Condiments & Sauces
                    "olive oil", "soy sauce", "vinegar", "mayonnaise", "ketchup", "mustard", "honey", "maple syrup", 
                    "hot sauce", "salsa", "tomato sauce", "tahini", "peanut butter", "coconut milk"
                ],
                "category": [
                    # Proteins
                    "protein", "protein", "protein", "protein", "protein", "protein", "protein", "protein", "protein", "protein",
                    # Dairy
                    "dairy", "dairy", "dairy", "dairy", "dairy", "dairy", "dairy", "dairy", "dairy", "dairy",
                    # Vegetables
                    "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", 
                    "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", "vegetable", 
                    "vegetable", "vegetable",
                    # Fruits
                    "fruit", "fruit", "fruit", "fruit", "fruit", "fruit", "fruit", "fruit", "fruit", "fruit",
                    # Grains & Starches
                    "grain", "grain", "grain", "grain", "grain", "grain", "grain", "grain", "grain", "grain",
                    # Herbs & Spices
                    "herb", "herb", "herb", "herb", "herb", "herb", "herb", "spice", "spice", "spice", "spice", 
                    "spice", "spice", "spice", "spice", "spice", "herb", "spice",
                    # Condiments & Sauces
                    "oil", "sauce", "condiment", "condiment", "condiment", "condiment", "sweetener", "sweetener", 
                    "sauce", "sauce", "sauce", "sauce", "spread", "sauce"
                ]
            }
            df = pd.DataFrame(sample_data)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            df.to_csv(file_path, index=False)
            return df
        
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading ingredients: {e}")
        return pd.DataFrame()