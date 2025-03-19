import spacy
from spacy.matcher import Matcher

def load_model(model_name='en_core_web_sm'):
    try:
        nlp = spacy.load(model_name)
        return nlp
    except OSError:
        print(f"Model {model_name} not found. Downloading...")
        # Download the model
        spacy.cli.download(model_name)
        nlp = spacy.load(model_name)
        return nlp

def process_text(text, nlp=None):
    if nlp is None:
        nlp = load_model()
    
    doc = nlp(text)
    processed_data = {
        'tokens': [token.text for token in doc],
        'entities': [(ent.text, ent.label_) for ent in doc.ents],
        'pos_tags': [(token.text, token.pos_) for token in doc]
    }
    return processed_data

def extract_ingredients(text, nlp=None):
    """Extract potential ingredients from user input text with improved accuracy."""
    if nlp is None:
        nlp = load_model()
        
    doc = nlp(text.lower())
    
    # Define patterns for ingredients
    matcher = Matcher(nlp.vocab)
    
    # Pattern for standalone nouns that might be ingredients
    matcher.add("INGREDIENT", [[{"POS": "NOUN"}]])
    
    # Pattern for adjective + noun (e.g., "fresh tomatoes")
    matcher.add("ADJ_INGREDIENT", [[{"POS": "ADJ"}, {"POS": "NOUN"}]])
    
    # Find matches
    matches = matcher(doc)
    
    ingredients = []
    for match_id, start, end in matches:
        span = doc[start:end]
        # Filter out common non-ingredient nouns
        if span.text not in ["recipe", "dish", "food", "meal", "cook", "time", "minutes"]:
            ingredients.append(span.text)
            
    # Remove duplicates while preserving order
    seen = set()
    ingredients = [ing for ing in ingredients if not (ing in seen or seen.add(ing))]
    
    return ingredients

def analyze_recipe_query(text, nlp=None):
    """Ultra simple query analyzer that just looks for keywords."""
    text = text.lower()
    result = {
        "ingredients": [],
        "meal_types": [],
        "cuisines": [],
        "dietary_preferences": [],
        "original_text": text
    }
    
    # List of known cuisines
    cuisines = ["italian", "french", "mexican", "chinese", "japanese", "indian", "thai", 
                "mediterranean", "greek", "american", "spanish"]
    
    # List of known meal types
    meal_types = ["breakfast", "lunch", "dinner", "dessert", "appetizer", "snack"]
    
    # List of common dietary preferences
    diet_prefs = ["vegetarian", "vegan", "gluten-free", "dairy-free", "low-carb"]
    
    # Common ingredients to explicitly check for
    common_ingredients = [
        "chicken", "beef", "pork", "fish", "egg", "eggs", "cheese", "chocolate", "pasta", 
        "rice", "potato", "tomato", "garlic", "onion", "carrot", "bacon"
    ]
    
    # Check for cuisines
    for cuisine in cuisines:
        if cuisine in text:
            result["cuisines"].append(cuisine)
    
    # Check for meal types
    for meal in meal_types:
        if meal in text:
            result["meal_types"].append(meal)
    
    # Check for dietary preferences
    for diet in diet_prefs:
        if diet in text:
            result["dietary_preferences"].append(diet)
    
    # Check for common ingredients
    for ingredient in common_ingredients:
        if ingredient in text:
            result["ingredients"].append(ingredient)
    
    # If user entered a comma-separated list, treat each item as an ingredient
    if "," in text:
        items = [item.strip() for item in text.split(",")]
        for item in items:
            if item and item not in result["ingredients"]:
                result["ingredients"].append(item)
    
    return result