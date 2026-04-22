"""Tests for string_utils module."""
import pytest
from string_utils import reverse_string, count_vowels, is_palindrome, capitalize_words


class TestReverseString:
    def test_basic_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_palindrome(self):
        assert reverse_string("radar") == "radar"

    def test_empty_string(self):
        assert reverse_string("") == ""


class TestCountVowels:
    def test_hello(self):
        assert count_vowels("hello") == 2

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("radar") is True

    def test_with_spaces(self):
        assert is_palindrome("race car") is True

    def test_with_case(self):
        assert is_palindrome("RaceCar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_complex_palindrome(self):
        assert is_palindrome("A man a plan a canal Panama") is True


class TestCapitalizeWords:
    def test_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_lowercase(self):
        assert capitalize_words("python is awesome") == "Python Is Awesome"
