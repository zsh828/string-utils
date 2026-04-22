"""String utility functions."""


def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


def count_vowels(s):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def is_palindrome(s):
    """Check if a string is a palindrome (ignoring case and spaces)."""
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def capitalize_words(s):
    """Capitalize the first letter of each word."""
    return s.title()
