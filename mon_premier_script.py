"""message = "C'est mon premier script !!!"
print(message)
je_change_de_type = 1
print(type(je_change_de_type))
je_change_de_type = "coucou"
print(type(je_change_de_type))
"""

def count_names_letters(names_list):
    """
    Count names with more than seven letters
    """
    count = 0
    for name in names_list:
        if len(name) > 7:
            count += 1
            print("Name with more than seven letters: " + name)
        else:
            print("Name with seven letters or less: " + name)
    return count

""" Test unitaire """
import unittest

class TestNamesMethod(unittest.TestCase):
    def test_count_names_with_more_than_seven_letters(self):
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        count = count_names_letters(names_list)
        self.assertEqual(count, 4)

if __name__ == '__main__':
    unittest.main()
