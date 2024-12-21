import json
import os
from collections import defaultdict

def get_json_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".json")]

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def count_refusal_sentiments(data):
    sentiment_counts = defaultdict(list)
    if "layer_candidates" in data:
        for candidate in data["layer_candidates"]:
            sentiment = candidate["refusal_sentiment"]
            number = candidate["number"]
            sentiment_counts[sentiment].append(number)
    return sentiment_counts

def main():
    directory = "out"
    json_files = get_json_files(directory)
    
    for json_file in json_files:
        file_path = os.path.join(directory, json_file)
        data = load_json(file_path)
        sentiment_counts = count_refusal_sentiments(data)
        
        if sentiment_counts:
            print(f"File: {json_file}")
            for sentiment, numbers in sentiment_counts.items():
                print(f"{sentiment}: {numbers}")
            print()

if __name__ == "__main__":
    main()
