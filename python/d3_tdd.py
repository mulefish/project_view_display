from d3_reportmaker import PathToLeaf, Parent, getMaxDepth, step2_makeGenerations, findNewPoint, findOpposetAngle
from letters import getLetterFromNumber
import unittest

# Set up
step1 = []
step1.append(PathToLeaf("src|index.js"))
step1.append(PathToLeaf("src|App.test.js"))
step1.append(PathToLeaf("src|routes.js"))
step1.append(PathToLeaf("src|setupTests.js"))
step1.append(PathToLeaf("src|App.js"))
step1.append(PathToLeaf("src|pages|Home|layout.js"))
step1.append(PathToLeaf("src|pages|Home|index.js"))
step1.append(PathToLeaf("src|pages|Diagram|memory.js"))
step1.append(PathToLeaf("src|pages|Diagram|Diagram.js"))
step1.append(PathToLeaf("src|pages|FauxForce|layout.js"))
step1.append(PathToLeaf("src|pages|FauxForce|logic.js"))
step1.append(PathToLeaf("src|pages|FauxForce|Controls.js"))
step1.append(PathToLeaf("src|pages|FauxForce|index.js"))
step1.append(PathToLeaf("src|pages|FauxForce|ReadJson.js"))
step1.append(PathToLeaf("src|pages|ABCDocuments|layout.js"))
step1.append(PathToLeaf("src|pages|ABCDocuments|index.js"))
step1.append(PathToLeaf("src|pages|ABCDocuments|redux|types.js"))
step1.append(PathToLeaf("src|pages|ABCDocuments|redux|actions.js"))
step1.append(PathToLeaf("src|pages|ABCDocuments|redux|index.js"))
step1.append(PathToLeaf("src|pages|ABCDocuments|redux|reducers.js"))
step1.append(PathToLeaf("src|pages|ABCDocuments|redux|thunks.js"))
step1.append(PathToLeaf("src|pages|SecondPass|layout.js"))
step1.append(PathToLeaf("src|pages|SecondPass|logic.js"))
step1.append(PathToLeaf("src|pages|SecondPass|Controls.js"))
step1.append(PathToLeaf("src|pages|SecondPass|memory.js"))
step1.append(PathToLeaf("src|pages|SecondPass|index.js"))
step1.append(PathToLeaf("src|pages|ForceDirectedGraph|layout.js"))
step1.append(PathToLeaf("src|pages|ForceDirectedGraph|logic.js"))
step1.append(PathToLeaf("src|pages|ForceDirectedGraph|Controls.js"))
step1.append(PathToLeaf("src|pages|ForceDirectedGraph|index.js"))
step1.append(PathToLeaf("src|redux|index.js"))
step1.append(PathToLeaf("src|redux|reducers.js"))


class Version2TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_getMaxDepthFromListOfPathToLeafObjs(self):
        ary = []
        ary.append(PathToLeaf("1|1|1|1|1|1"))
        ary.append(PathToLeaf("1|1|1|1|1|1|1|1|1|1"))
        ary.append(PathToLeaf("1|1|1|1"))
        expected = 10
        actual = getMaxDepth(ary)
        self.assertEqual(expected, actual, 'max len() not correct')

    def test_makeParentObject_alsoCheckNoDupes(self):
        p = Parent("one", 1)
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

    def test_findNewPoint(self):

        angles = [0, 10, 45, 90, 180, 270, 350, 359, 360, 361, 1, 721]
        expected = [
            {'y': 0.0, 'x': 100.0, 'a': 0},
            {'y': 17.0, 'x': 98.0, 'a': 10},
            {'y': 71.0, 'x': 71.0, 'a': 45},
            {'y': 100.0, 'x': 0.0, 'a': 90},
            {'y': 0.0, 'x': -100.0, 'a': 180},
            {'y': -100.0, 'x': -0.0, 'a': 270},
            {'y': -17.0, 'x': 98.0, 'a': 350},
            {'y': -2.0, 'x': 100.0, 'a': 359},
            {'y': -0.0, 'x': 100.0, 'a': 360},
            {'y': 2.0, 'x': 100.0, 'a': 361},
            {'y': 2.0, 'x': 100.0, 'a': 1},
            {'y': 2.0, 'x': 100.0, 'a': 721},
        ]
        actual = []
        for angle in angles:
            xy = findNewPoint(0, 0, angle, 100)
            xy["a"] = angle
            actual.append(xy)

        self.assertEqual(expected, actual,
                         'FAILBOT!\n{} \nvs \n{}'.format(expected, actual))

    def test_findOpposetAngle(self):
        angles = [0, 45, 90, 180, 270, 360, 10, 370]
        expected = [
            {'in': 0, 'out': 180},
            {'in': 45, 'out': 225},
            {'in': 90, 'out': 270},
            {'in': 180, 'out': 0},
            {'in': 270, 'out': 90},
            {'in': 360, 'out': 180},
            {'in': 10, 'out': 190},
            {'in': 370, 'out': 190}
        ]
        actual = []
        for angle in angles:
            opposet = findOpposetAngle(angle)
            a = {}
            a["out"] = opposet
            a["in"] = angle
            actual.append(a)

        self.assertEqual(actual, expected,
                         'FAILBOT!\n{} \nvs \n{}'.format(expected, actual))


if __name__ == "__main__":
    unittest.main()
