from collections import Counter

def permutations(s):
    result = []
    map = Counter(s)
    printPerms(map, '', len(s), result)
    return result

def printPerms(map, prefix, remaining, result):
    if remaining == 0:
        return result.append(prefix)
    for i in map.keys():
        count = map.get(i)
        if count > 0:
            map[i] = count - 1
            printPerms(map, prefix+i, remaining-1, result)
            map[i] = count
            
            
print(permutations('abb'))

import unittest

class Test(unittest.TestCase):
    def test_permutations(self):
        self.assertCountEqual(permutations('abb'), ['abb', 'bab', 'bba'])
if __name__ == '__main__':
    unittest.main()