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
- 🖥️ Web Interface: Modern, responsive design for easy browsing

## Technologies Used
- Python 3.6+
- spaCy: For natural language processing
- pandas: For ingredient data management
- JSON: For recipe storage and retrieval
- Flask: For web interface
- Tailwind CSS: For modern UI design
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

## Running the Application

### Web Interface (Recommended)
Launch the web application:
```bash
python app.py
```
Then open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

### Command-Line Interface
Run the traditional command-line application:
```bash
python main.py
```

## Using the Web Interface
The web interface provides a user-friendly way to search and discover recipes:

1. **Home Page**: View statistics about the recipe collection and use the search bar
2. **Recipe Search**: Enter ingredients, cuisine types, or meal preferences
3. **Recipe Details**: View ingredients, instructions, and difficulty levels
4. **Alternative Recipes**: Discover similar recipes you might enjoy

### Example Web Searches
- Type "italian" to see Italian recipes
- Search "dessert with chocolate" for sweet treats
- Enter "quick breakfast" for morning meal ideas
- Try "vegetarian dinner" for meat-free evening recipes

## Quick Start Guide (Command Line)
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

#### Web Interface Not Loading
**Problem**: Cannot access the web interface
**Solution**:
- Ensure Flask is properly installed (`pip install flask`)
- Check for any error messages in the terminal
- Make sure port 5000 is not being used by another application
- Try restarting the application with `python app.py`

## Project Structure
- `app.py`: Web interface using Flask
- `main.py`: Command-line interface
- `templates/`: HTML templates for web interface
- `static/`: CSS and JavaScript files for web styling
- `src/`: Core application logic
- `data/`: Recipe and ingredient data

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements
Designed and developed by Swarnim Varchaswa

## Example Output (Command Line)
```
🍳 AI Recipe Generator 🍳
--------------------------
✅ Loaded 36 recipes
Recipe collection includes:
  • 5 dessert recipes
  • 7 Italian dishes
  • 14 vegetarian options
  • 6 Asian dishes
  • 5 Mexican recipes
  • 5 breakfast options

Analyzing your request...> dessert with chocolate
Looking for recipes with: chocolate
Meal type: dessert

🍽️ Chocolate Chip Cookies
...
```