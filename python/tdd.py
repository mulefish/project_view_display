from version2 import Node, Parent, getMaxDepth, step2_makeGenerations
from letters import getLetterFromNumber
import unittest

# Set up
step1 = []
step1.append(Node("A", "src|index.js"))
step1.append(Node("A", "src|App.test.js"))
step1.append(Node("A", "src|routes.js"))
step1.append(Node("A", "src|setupTests.js"))
step1.append(Node("A", "src|App.js"))
step1.append(Node("D", "src|pages|Home|layout.js"))
step1.append(Node("D", "src|pages|Home|index.js"))
step1.append(Node("E", "src|pages|Diagram|memory.js"))
step1.append(Node("E", "src|pages|Diagram|Diagram.js"))
step1.append(Node("F", "src|pages|FauxForce|layout.js"))
step1.append(Node("F", "src|pages|FauxForce|logic.js"))
step1.append(Node("F", "src|pages|FauxForce|Controls.js"))
step1.append(Node("F", "src|pages|FauxForce|index.js"))
step1.append(Node("F", "src|pages|FauxForce|ReadJson.js"))
step1.append(Node("H", "src|pages|ABCDocuments|layout.js"))
step1.append(Node("H", "src|pages|ABCDocuments|index.js"))
step1.append(Node("I", "src|pages|ABCDocuments|redux|types.js"))
step1.append(Node("I", "src|pages|ABCDocuments|redux|actions.js"))
step1.append(Node("I", "src|pages|ABCDocuments|redux|index.js"))
step1.append(Node("I", "src|pages|ABCDocuments|redux|reducers.js"))
step1.append(Node("I", "src|pages|ABCDocuments|redux|thunks.js"))
step1.append(Node("G", "src|pages|SecondPass|layout.js"))
step1.append(Node("G", "src|pages|SecondPass|logic.js"))
step1.append(Node("G", "src|pages|SecondPass|Controls.js"))
step1.append(Node("G", "src|pages|SecondPass|memory.js"))
step1.append(Node("G", "src|pages|SecondPass|index.js"))
step1.append(Node("L", "src|pages|ForceDirectedGraph|layout.js"))
step1.append(Node("L", "src|pages|ForceDirectedGraph|logic.js"))
step1.append(Node("L", "src|pages|ForceDirectedGraph|Controls.js"))
step1.append(Node("L", "src|pages|ForceDirectedGraph|index.js"))
step1.append(Node("N", "src|redux|index.js"))
step1.append(Node("N", "src|redux|reducers.js"))


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

    def test_makeParentObject_alsoCheckNoDupes(self):
        p = Parent("one")
        p.addKid("two")
        p.addKid("three")
        p.addKid("four")
        p.addKid("four")
        p.addKid("four")
        p.addKid("four")
        expected = {"one": ["two", "three", "four"]}
        self.assertEqual(expected, p.show(), 'parent object is not perfect')

    def test_number2letter(self):
        expected = ["A", "B", "C"]
        actual = []
        actual.append(getLetterFromNumber(0))
        actual.append(getLetterFromNumber(1))
        actual.append(getLetterFromNumber(2))
        self.assertEqual(expected, actual, '123 is supposed to be ABC')

    def test_makeGeenerations1(self):
        # Notice! Duped keys! And that will be OK
        expected = ["src", "redux", "pages", "ABCDocuments", "SecondPass",
                    "Diagram", "FauxForce", "ForceDirectedGraph", "Home", "redux"]

        expected.sort()
        actual = []
        deepest = 6
        generations = step2_makeGenerations(deepest, step1)
        for g in generations:
            for k in g:
                actual.append(k)
        actual.sort()
        self.assertEqual(expected, actual,
                         'Something afoot with step2_makeGenerations func')

    def test_makeGenerations_srcIsCorrect(self):
        expected = ['App.test.js', 'index.js',  'routes.js',
                    'setupTests.js', 'App.js', 'pages', 'redux']
        expected.sort()
        deepest = 6
        generations = step2_makeGenerations(deepest, step1)

        parent = generations[0]["src"]
        actual = parent.children
        actual.sort()

        self.assertEqual(expected, actual,
                         'FAILBOT!\n{} \nvs \n{}'.format(expected, actual))


if __name__ == "__main__":
    unittest.main()
