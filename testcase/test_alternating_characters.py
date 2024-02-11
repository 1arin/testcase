from case.alternating_characters import alternatingCharacters
import unittest

def alternatingCharacters(s):
    count = i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            count += 1
        i += 1
    return count

# Test cases
test_cases = [
    ("abcdef", 0),
    ("aaaaa", 4),
    ("ababab", 0),
    ("xxxxx", 4),
    ("aabbaabb", 4)
]

# Test the function with each test case
for input_string, expected_output in test_cases:
    result = alternatingCharacters(input_string)
    assert result == expected_output, f"Test case failed: input='{input_string}', expected={expected_output}, got={result}"

