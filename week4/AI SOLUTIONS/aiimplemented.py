def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

data = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 90}
]

sorted_data = sort_dicts_by_key(data, "score")
print(sorted_data)


# manually inputing the data without copilot 
def sort_dicts_by_key(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data
data = [
    {"name": "alice", "score": 88},
    {"name": "bob", "score": 72},
    {"name": "charlie", "score": 90}
]