
def towers_of_hanoi(tower1, tower2, tower3, n=None):
    if n is None:
        n = len(tower1.discs)
    if n==0:
        return
    towers_of_hanoi(tower1, tower3, tower2, n-1)
    disc = tower1.discs.pop()
    tower3.discs.append(disc)
    towers_of_hanoi(tower2, tower1, tower3, n-1)
    
    
    
class Tower(object):
    def __init__(self, name, discs=None):
        self.name = name
        if discs:
            self.discs = discs
        else:
            self.discs = []

    
import unittest

class Test(unittest.TestCase):
  def test_towers_of_hanoi(self):
    tower1 = Tower("Tower1", ["6", "5", "4", "3", "2", "1"])
    tower2 = Tower("Tower2")
    tower3 = Tower("Tower3")
    towers_of_hanoi(tower1, tower2, tower3)
    self.assertEqual(tower1.discs, [])
    self.assertEqual(tower2.discs, [])
    self.assertEqual(tower3.discs, ["6", "5", "4", "3", "2", "1"])

if __name__ == "__main__":
  unittest.main()