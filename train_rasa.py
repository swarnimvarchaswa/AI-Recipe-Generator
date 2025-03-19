import os
import subprocess

def train_rasa():
    # Ensure we're in the correct directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    rasa_dir = os.path.join(project_dir, 'src', 'rasa')
    
    # Check if the Rasa files exist
    if not os.path.exists(os.path.join(rasa_dir, 'config.yml')):
        print("Rasa configuration files not found. Please check the setup.")
        return False
    
    try:
        # Change to the Rasa directory
        os.chdir(rasa_dir)
        
        # Train the Rasa model
        print("Training Rasa model...")
        subprocess.run(['rasa', 'train'], check=True)
        
        print("Rasa model trained successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Error training Rasa model. Make sure Rasa is installed correctly.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    train_rasa()