import ast

def normalize_indentation(code: str) -> str:
    tree = ast.parse(code)
    return ast.unparse(tree)


# Test

code1 = "def count_pairs(arr):\n    count = 0\n    for i in range(len(arr)):\n        for j in range(len(arr)):\n            if arr[i] < arr[j]:\n                count += 1\n    return count\n"
code2 = "def count_pairs(arr):\n count = 0\n for i in range(len(arr)):\n   for j in range(len(arr)):\n        if arr[i] < arr[j]:\n             count += 1\n return count\n"

normalized_code1 = normalize_indentation(code1)
normalized_code2 = normalize_indentation(code2)

print(normalized_code1 == normalized_code2)  # Should print True