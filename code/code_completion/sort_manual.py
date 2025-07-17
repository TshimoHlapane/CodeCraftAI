# Manual Implementation (Mike)
def sort_dicts_by_key_manual(dict_list, sort_key):
    """
    Manually sorts a list of dictionaries by a specific key.
    :param dict_list: List[Dict]
    :param sort_key: str
    :return: List[Dict]
    """
    # Create a new list to avoid mutating the original
    sorted_list = list(dict_list)
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            a = sorted_list[j].get(sort_key, None)
            b = sorted_list[j+1].get(sort_key, None)
            if a is not None and b is not None and a > b:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

# Example usage
if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    print("Manual:", sort_dicts_by_key_manual(data, "age"))