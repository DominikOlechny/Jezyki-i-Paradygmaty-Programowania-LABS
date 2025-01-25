from typing import List, Any, Optional


def analyze_data(data: List[Any]):
    # Filtracja wartości numerycznych
    numeric_values = list(filter(lambda x: isinstance(x, (int, float)), data))
    max_numeric = max(numeric_values) if numeric_values else None

    # Filtracja napisów
    string_values = list(filter(lambda x: isinstance(x, str), data))
    longest_string = max(string_values, key=len) if string_values else None

    # Filtracja krotek
    tuple_values = list(filter(lambda x: isinstance(x, tuple), data))
    longest_tuple = max(tuple_values, key=len) if tuple_values else None

    return max_numeric, longest_string, longest_tuple


# Przykładowe użycie
data = [
    42, "scankcan", (1, 2, 3), 3.14, "cahskajshchjscakchjksajkh", (1,), (1, 2, 3, 4),
    {"sad": "zcxzxc"}, [1, 2, 3], -100, "czxhczxjk", (1, 2)
]

result = analyze_data(data)
print("Największa liczba:", result[0])
print("Najdłuższy napis:", result[1])
print("Krotka o największej liczbie elementów:", result[2])
