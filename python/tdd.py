from version2 import Node, Parent, getMaxDepth, readFS_makeDotGraph

import unittest


class Version2TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_getMaxDepthFromListOfNodeObjs(self):
        ary = []
        ary.append(Node("a", "1|1|1|1|1|1"))
        ary.append(Node("a", "1|1|1|1|1|1|1|1|1|1"))
        ary.append(Node("a", "1|1|1|1"))
        expected = 10
        actual = getMaxDepth(ary)
        self.assertEqual(expected, actual, 'max len() not correct')

    def test_makeParentObject(self):
        p = Parent("one")
        p.addKid("two")
        p.addKid("three")
        p.addKid("four")
        expected = {"one": ["two", "three", "four"]}
        self.assertEqual(expected, p.show(), 'parent object is not perfect')


if __name__ == "__main__":
    unittest.main()
