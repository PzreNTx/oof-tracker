import time
import json
import os
import re

def no_skip(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("You are required to fill in this field!")

def add_mistake():
    print("Please enter the mistake details:")
    time.sleep(2)
    
    # Collect the data
    date.pattern = r'^\d{4}-\d{2}-\d{2}$'
    while True:
        date = input("When the mistake occurred (YYYY-MM-DD): ")
        if re.match(date.pattern, date):
            break
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    subject = no_skip("Subject of the mistake: ")
    topic = no_skip("Topic of the mistake: ")
    mistake_type = no_skip("Type of the mistake: ")
    description = input("Describe the mistake (optional): ")
    correct_answer = input("What is the correct answer? (optional): ")
    root_cause = no_skip("What is the root cause of the mistake?: ")
    fix_strategy = no_skip("What is your strategy to fix this mistake?: ")

    while True:
        confidence_level = input("On a scale of 1-10, how confident are you that your fix strategy will work? ")
        if confidence_level.isdigit() and 1 <= int(confidence_level) <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    
    # Create the mistake dictionary
    mistake = {
        "date": date,
        "subject": subject,
        "topic": topic,
        "mistake_type": mistake_type,
        "description": description,
        "correct_answer": correct_answer,
        "root_cause": root_cause,
        "fix_strategy": fix_strategy,
        "confidence_level": int(confidence_level) if confidence_level.isdigit() else confidence_level
    }
    
    # Find the next available mistake number
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data')
    existing_files = os.listdir(data_dir)
    mistake_numbers = []
    for file in existing_files:
        match = re.match(r'mistake(\d+)\.json', file)
        if match:
            mistake_numbers.append(int(match.group(1)))
    
    next_number = max(mistake_numbers) + 1 if mistake_numbers else 1
    
    # Save to file
    filename = f'mistake{next_number}.json'
    filepath = os.path.join(data_dir, filename)
    with open(filepath, 'w') as f:
        json.dump([mistake], f, indent=4)
    
    print(f"Mistake saved to {filename}")

if __name__ == "__main__":
    add_mistake()
