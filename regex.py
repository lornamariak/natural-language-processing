"""Test name-matching regular expression."""
import re

import pytest

'''
Gerund matching using Regex
'''

# *** ADD YOUR PATTERN BELOW *** #
pattern = r'([a-zA-Z]*[aeiou]+)([a-z]+|)(ing)\b'
#raise NotImplementedError("Add your pattern to the test file.")
# *** ADD YOUR PATTERN ABOVE *** #


test_cases = [
    ("showering", True),
    ("eating", True),
    ("using", True),
    ("praying", True),
    ("scathing", True),
    ("bring", False),
    ("sing", False),
    ("cling", False),
    ("seemingly", False),
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_name_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.fullmatch(pattern, string) is not None) == matches


##############################################################################################
'''
Name matching using Regex
'''

# *** ADD YOUR PATTERN BELOW *** #
pattern = r'(^[A-Z][a-z]*(\.)?) ([a-zA-Z]+[\.,-]*( )*)*([A-Z]+[a-z]*( )*)\w+[\.]*'
#raise NotImplementedError("Add your pattern to the test file.")
# *** ADD YOUR PATTERN ABOVE *** #


test_cases = [
    ("Quan Hongchan", True),
    ("Philip Seymour Hoffman", True),
    ("Dr. Nicki Washington", True),
    ("Joseph Gordon-Levitt", True),
    ("Ken Griffey, Jr.", True),
    ("John von Neumann", True),
    ("Cher", False),
    ("not a name", False),
    ("happy feet", False),
    ("The end", False),
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_name_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""