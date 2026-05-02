def delete_file(mistake_number):
    import os
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data')
    file_path = os.path.join(data_dir, f'mistake{mistake_number}.json')
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Mistake {mistake_number} has been deleted.")
    else:
        print(f"Mistake {mistake_number} does not exist.")