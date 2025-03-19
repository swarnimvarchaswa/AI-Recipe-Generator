# AI Recipe Generator 🍳

## Overview
The AI Recipe Generator is an intelligent application that helps you discover recipes based on ingredients you have, cuisine preferences, or meal types. It uses natural language processing to understand your requests and matches them with a database of over 30 diverse recipes.

## Features
- 🧠 Smart Matching: Ask for recipes in natural language
- 🍕 Diverse Recipes: 30+ recipes across Italian, Mexican, Asian, American cuisines
- 🥗 Multiple Meal Types: Breakfast, lunch, dinner, desserts
- 🌱 Dietary Options: Vegetarian, vegan recipes available
- ✨ Recipe Alternatives: Get suggestions for alternative recipes
- 📊 Statistics: View recipe collection statistics

## Technologies Used
- Python 3.6+
- spaCy: For natural language processing
- pandas: For ingredient data management
- JSON: For recipe storage and retrieval
- ColorPrint: For colorful terminal output

## Getting Started

### Prerequisites
- Python 3.6+
- pip package manager

### Setup and Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-recipe-generator.git
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Initialize the recipe database (required for first-time setup):
```bash
python refresh_data.py
```

### Starting the Application
Run the main application:
```bash
python main.py
```

## Quick Start Guide
1. After running the application, you'll see statistics about available recipes
2. Type your recipe request at the prompt (">")
3. Try simple queries first: "italian" or "breakfast"
4. For more specific searches, try: "dessert with chocolate" or "eggs, bacon"
5. Type "exit" to quit the application

## Managing Recipe Data

### Refreshing Recipe Data
To refresh recipe data:
```bash
python refresh_data.py
```

This will:
- Delete existing recipe and ingredient files
- Regenerate them with the complete dataset of 30+ recipes
- Display statistics about the available recipes
- Test key search terms to ensure functionality

### When to Refresh Data
- First time setup: Always refresh data when setting up the project
- After code changes: If you've modified the recipe generation logic
- Troubleshooting: If searches aren't returning expected results
- Data corruption: If you see errors about missing or invalid recipe data

## Example Queries
- **Cuisine**: "Italian pasta", "Mexican dinner"
- **Meal Type**: "quick breakfast", "healthy lunch"
- **Ingredients**: "chicken and rice", "vegetarian with tofu"
- **Combined**: "spicy Asian dinner", "quick Italian breakfast"

## Troubleshooting

### Common Issues

#### No Matching Recipes Found
**Problem**: The search isn't returning any recipes
**Solution**:
- Run `python refresh_data.py` to ensure all recipes are available
- Use simpler search terms
- Check the recipe stats to verify recipes exist for your search term

#### Error Loading Data
**Problem**: Application shows errors about missing or corrupt data files
**Solution**:
- Run `python refresh_data.py` to recreate all data files
- Check file permissions in your data directory
- Ensure your Python environment has write access to the data folder

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Example Output
```markdown
🍳 AI Recipe Generator 🍳
--------------------------
✅ Loaded 36 recipes
Recipe collection includes:
  • 5 dessert recipes
  • 7 Italian dishes







Analyzing your request...> dessert with chocolate  • 14 vegetarian options  • 6 Asian dishes  • 5 Mexican recipes  • 5 breakfast optionsLooking for recipes with: chocolate
Meal type: dessert

🍽️ Chocolate Chip Cookies
...
```#   A I - R e c i p e - G e n e r a t o r  
 