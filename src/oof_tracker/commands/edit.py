import json
from pathlib import Path
def edit_mistakes():
    data_dir = Path(__file__).resolve().parents[3] / 'data'
    files = [f for f in data_dir.iterdir() if f.suffix == '.json']
    
    if not files:
        print("No mistakes found.")
        return
    
    for file in files:
        print(f"Mistake: {file.stem}")
    
    mistake_number = input("Enter the mistake number you want to edit (e.g., 1 for mistake1.json): ")
    file_path = data_dir / f'mistake{mistake_number}.json'
    
    if not file_path.exists():
        print(f"Mistake {mistake_number} does not exist.")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Assuming each file contains a list with one mistake
    if isinstance(data, list) and data:
        mistake = data[0]
    else:
        mistake = data  # In case it's directly a dict
    
    print("Current details of the mistake:")
    for key, value in mistake.items():
        print(f"{key.capitalize()}: {value}")
    
    print("\nEnter new details (leave blank to keep current value):")
    for key in mistake.keys():
        new_value = input(f"{key.capitalize()} [{mistake[key]}]: ")
        if new_value.strip():
            mistake[key] = new_value.strip()
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(mistake, f, indent=4)
    
    print(f"Mistake {mistake_number} has been updated.")

if __name__ == "__main__":
    edit_mistakes()
    