from src.nlp.spacy_processor import load_model, process_text, extract_ingredients, analyze_recipe_query

class IngredientProcessor:
    def __init__(self):
        self.nlp = load_model()
        self.common_units = ["cup", "tablespoon", "teaspoon", "ounce", "pound", "gram", 
                            "kilogram", "ml", "liter", "pinch", "dash", "bunch", "slice"]
        
        self.ingredient_substitutes = {
            "butter": ["margarine", "olive oil", "coconut oil"],
            "milk": ["almond milk", "soy milk", "oat milk", "coconut milk"],
            "flour": ["almond flour", "coconut flour", "gluten-free flour"],
            "sugar": ["honey", "maple syrup", "stevia", "agave nectar"],
            "egg": ["flax egg", "chia egg", "applesauce"]
        }

    def process_ingredients(self, ingredient_list):
        """Process a list of ingredients by cleaning and standardizing them."""
        if not ingredient_list:
            return []
            
        # Clean ingredients - remove empty entries, strip whitespace, convert to lowercase
        cleaned_ingredients = []
        for ingredient in ingredient_list:
            if ingredient:
                # Remove quantities and units
                cleaned = self._clean_ingredient(ingredient)
                cleaned_ingredients.append(cleaned)
                
        return cleaned_ingredients
    
    def _clean_ingredient(self, ingredient_text):
        """Clean a single ingredient text by removing quantities and normalizing."""
        text = ingredient_text.strip().lower()
        
        # Remove quantities (numbers followed by units)
        doc = self.nlp(text)
        
        # Extract just the food item by removing quantities and units
        ingredient_parts = []
        skip_next = False
        
        for i, token in enumerate(doc):
            if skip_next:
                skip_next = False
                continue
                
            # Skip numbers
            if token.like_num:
                if i < len(doc) - 1 and doc[i+1].text in self.common_units:
                    skip_next = True
                continue
                
            # Skip common units
            if token.text in self.common_units:
                continue
                
            ingredient_parts.append(token.text)
        
        cleaned = " ".join(ingredient_parts).strip()
        return cleaned
    
    def extract_from_text(self, text):
        """Extract ingredients from free-form text."""
        return extract_ingredients(text, self.nlp)
    
    def analyze_query(self, text):
        """Analyze a user query to extract ingredients and preferences."""
        return analyze_recipe_query(text, self.nlp)
    
    def suggest_substitutes(self, ingredient):
        """Suggest substitutes for a given ingredient."""
        ingredient = ingredient.lower().strip()
        
        # Check for direct matches
        if ingredient in self.ingredient_substitutes:
            return self.ingredient_substitutes[ingredient]
        
        # Check for partial matches
        for key in self.ingredient_substitutes:
            if key in ingredient or ingredient in key:
                return self.ingredient_substitutes[key]
        
        return []