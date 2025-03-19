import unittest
from src.models.recipe_generator import RecipeGenerator

class TestRecipeGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = RecipeGenerator()

    def test_generate_recipe_with_valid_ingredients(self):
        ingredients = ["chicken", "rice", "broccoli"]
        recipe = self.generator.generate_recipe(ingredients)
        self.assertIsInstance(recipe, str)
        self.assertIn("chicken", recipe)
        self.assertIn("rice", recipe)
        self.assertIn("broccoli", recipe)

    def test_generate_recipe_with_no_ingredients(self):
        ingredients = []
        recipe = self.generator.generate_recipe(ingredients)
        self.assertEqual(recipe, "No ingredients provided.")

    def test_generate_recipe_with_invalid_ingredients(self):
        ingredients = ["unknown_ingredient"]
        recipe = self.generator.generate_recipe(ingredients)
        self.assertEqual(recipe, "No valid recipe found for the provided ingredients.")

if __name__ == '__main__':
    unittest.main()