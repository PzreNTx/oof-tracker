import os
import json

def list_mistakes():
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data')
    files = [f for f in os.listdir(data_dir) if f.endswith('.json')]
    
    if not files:
        print("No mistakes found.")
        return
    
    # Stops running if there are no more mistakes to list.
    for file in files:
        filepath = os.path.join(data_dir, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Assuming each file contains a list with one mistake
        if isinstance(data, list) and data:
            mistake = data[0]
        else:
            mistake = data  # In case it's directly a dict
        
        date = mistake.get("date", "")
        subject = mistake.get("subject", "")
        topic = mistake.get("topic", "")
        mistake_type = mistake.get("mistake_type", "")
        description = mistake.get("description", "No description provided.")
        correct_answer = mistake.get("correct_answer", "No correct answer provided.")
        root_cause = mistake.get("root_cause", "")
        fix_strategy = mistake.get("fix_strategy", "")
        confidence_level = mistake.get("confidence_level", "")
        print(f"Mistake: {file}")
        print(f"Date: {date}")
        print(f"Subject: {subject}")
        print(f"Topic: {topic}")
        print(f"Type: {mistake_type}")
        print(f"Description: {description}")
        print(f"Correct Answer: {correct_answer}")
        print(f"Root Cause: {root_cause}")
        print(f"Fix Strategy: {fix_strategy}")
        print(f"Confidence Level: {confidence_level}")
        print("-" * 40)

if __name__ == "__main__":
    list_mistakes()