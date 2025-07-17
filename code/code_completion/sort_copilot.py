# AI-Suggested Implementation (GitHub Copilot)
def sort_dicts_by_key(dict_list, sort_key):
    """
    Sorts a list of dictionaries by a specific key.
    :param dict_list: List[Dict]
    :param sort_key: str
    :return: List[Dict]
    """
    return sorted(dict_list, key=lambda x: x.get(sort_key, None))

# Example usage
if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    print("AI-suggested:", sort_dicts_by_key(data, "age"))
