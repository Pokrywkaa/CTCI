def permutations(s):
    return permutations_helper('', s)

def permutations_helper(partial, letters_left):
    if len(letters_left)==0:
        return [partial]
    permutations = []
    for i, letter in enumerate(letters_left):
        next_letters_left = letters_left[:i] + letters_left[(i+1):]
        permutations += permutations_helper(partial+letter, next_letters_left)
    return permutations

print(permutations('abc'))

import unittest

class Test(unittest.TestCase):
    def test_permutation(self):
        self.assertCountEqual(permutations('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertCountEqual(permutations('ab'), ['ab', 'ba'])
        
if __name__ == '__main__':
    unittest.main()