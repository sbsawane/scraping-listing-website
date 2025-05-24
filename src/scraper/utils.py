def format_data(raw_data):
    # Function to clean and format the scraped property data
    formatted_data = []
    for item in raw_data:
        formatted_item = {
            'title': item.get('title', '').strip(),
            'price': item.get('price', '').strip(),
            'location': item.get('location', '').strip(),
            'description': item.get('description', '').strip(),
        }
        formatted_data.append(formatted_item)
    return formatted_data

def save_to_csv(data, filename):
    import csv
    keys = data[0].keys() if data else []
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)