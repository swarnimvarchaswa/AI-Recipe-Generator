import unittest
from src.models.ingredient_processor import IngredientProcessor

class TestIngredientProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = IngredientProcessor()

    def test_process_ingredients(self):
        input_ingredients = ["2 cups of flour", "1 cup of sugar", "1/2 cup of butter"]
        expected_output = ["flour", "sugar", "butter"]
        processed_ingredients = self.processor.process_ingredients(input_ingredients)
        self.assertEqual(processed_ingredients, expected_output)

    def test_process_empty_list(self):
        input_ingredients = []
        expected_output = []
        processed_ingredients = self.processor.process_ingredients(input_ingredients)
        self.assertEqual(processed_ingredients, expected_output)

    def test_process_invalid_ingredients(self):
        input_ingredients = ["123", "!!!", "flour"]
        expected_output = ["flour"]
        processed_ingredients = self.processor.process_ingredients(input_ingredients)
        self.assertEqual(processed_ingredients, expected_output)

if __name__ == '__main__':
    unittest.main()