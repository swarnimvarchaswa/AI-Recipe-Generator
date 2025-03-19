class RecipeGenerator:
    def __init__(self, recipes=None):
        self.recipes = recipes or []

    def load_recipes(self, recipes):
        """Load recipes from a list of recipe dictionaries."""
        self.recipes = recipes
    
    def generate_recipe(self, query_analysis):
        """Generate a recipe based on query analysis."""
        # Get search terms
        search_terms = []
        
        # Add ingredients to search terms
        if "ingredients" in query_analysis and query_analysis["ingredients"]:
            search_terms.extend([i.lower() for i in query_analysis["ingredients"]])
        
        # Add meal types to search terms
        if "meal_types" in query_analysis and query_analysis["meal_types"]:
            search_terms.extend([m.lower() for m in query_analysis["meal_types"]])
        
        # Add cuisines to search terms
        if "cuisines" in query_analysis and query_analysis["cuisines"]:
            search_terms.extend([c.lower() for c in query_analysis["cuisines"]])
            
        # Also check original text for common terms
        if "original_text" in query_analysis:
            text = query_analysis["original_text"].lower()
            # Check for common meal types in the text
            for term in ["dessert", "breakfast", "dinner", "lunch", "italian", "chocolate", "mexican"]:
                if term in text and term not in search_terms:
                    search_terms.append(term)
        
        # If no search terms, return error
        if not search_terms:
            return "Please provide some ingredients or a type of dish."
        
        # Very simple matching - check if ANY search term appears in recipe ingredients or tags
        matches = []
        for recipe in self.recipes:
            # Get recipe text to search in (ingredients + tags)
            recipe_text = " ".join([ing.lower() for ing in recipe.get("ingredients", [])])
            recipe_text += " " + " ".join([tag.lower() for tag in recipe.get("tags", [])])
            
            # Check if ANY search term appears in recipe text
            for term in search_terms:
                if term in recipe_text:
                    matches.append(recipe)
                    break  # One match is enough
        
        # If no matches, return error
        if not matches:
            return f"No matching recipes found for: {', '.join(search_terms)}"
        
        # Return the first match
        return matches[0]
    
    def get_recipe_suggestions(self, query_analysis, limit=3):
        """Get multiple recipe suggestions."""
        # Get search terms
        search_terms = []
        
        # Add ingredients to search terms
        if "ingredients" in query_analysis and query_analysis["ingredients"]:
            search_terms.extend([i.lower() for i in query_analysis["ingredients"]])
        
        # Add meal types to search terms
        if "meal_types" in query_analysis and query_analysis["meal_types"]:
            search_terms.extend([m.lower() for m in query_analysis["meal_types"]])
        
        # Add cuisines to search terms
        if "cuisines" in query_analysis and query_analysis["cuisines"]:
            search_terms.extend([c.lower() for c in query_analysis["cuisines"]])
            
        # Also check original text for common terms
        if "original_text" in query_analysis:
            text = query_analysis["original_text"].lower()
            # Check for common meal types in the text
            for term in ["dessert", "breakfast", "dinner", "lunch", "italian", "chocolate", "mexican"]:
                if term in text and term not in search_terms:
                    search_terms.append(term)
        
        # If no search terms, return empty list
        if not search_terms:
            return []
        
        # Very simple matching - check if ANY search term appears in recipe ingredients or tags
        matches = []
        for recipe in self.recipes:
            # Get recipe text to search in (ingredients + tags)
            recipe_text = " ".join([ing.lower() for ing in recipe.get("ingredients", [])])
            recipe_text += " " + " ".join([tag.lower() for tag in recipe.get("tags", [])])
            
            # Check if ANY search term appears in recipe text
            for term in search_terms:
                if term in recipe_text:
                    matches.append(recipe)
                    break  # One match is enough
        
        # Return up to 'limit' matches
        return matches[:limit]