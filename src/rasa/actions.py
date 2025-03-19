from rasa import Action
from rasa_sdk.events import SlotSet
from models.recipe_generator import RecipeGenerator
from models.ingredient_processor import IngredientProcessor

class ActionGenerateRecipe(Action):
    def name(self) -> str:
        return "action_generate_recipe"

    def run(self, dispatcher, tracker, domain):
        ingredients = tracker.get_slot("ingredients")
        
        if not ingredients:
            dispatcher.utter_message(text="Please provide some ingredients.")
            return []

        ingredient_processor = IngredientProcessor()
        processed_ingredients = ingredient_processor.process_ingredients(ingredients)

        recipe_generator = RecipeGenerator()
        recipe = recipe_generator.generate_recipe(processed_ingredients)

        if recipe:
            dispatcher.utter_message(text=f"Here is a recipe for you: {recipe}")
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't generate a recipe with those ingredients.")

        return [SlotSet("ingredients", None)]