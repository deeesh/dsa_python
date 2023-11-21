import re

def simple_matcher(pattern , text):

    # Escape Special Patterns in Python
    pattern = re.escape(pattern)

    # Replace '*' with '.*' for 0 or more ocurrence
    pattern = pattern.replace(r'\*', '.*')

    # Replace '?' with '.' for a single character
    pattern = pattern.replace(r'\?', '.')

    # Add '^' at the beginning '$' at the end to match the whole string
    pattern = f'^{pattern}$'

    # Use re.match to check if the text matches the pattern
    match = re.match(pattern, text)

    return bool(match)

pattern = r'ab*c'
text = 'ac'
result = simple_matcher(pattern, text)
print(result)
