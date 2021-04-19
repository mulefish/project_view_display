import fnmatch
import os
import json
from letters import getLetterFromNumber
import math
pattern = "*.js"
rootPath = "../src/"
ignore = ["", ".."]


class PathToLeaf:
    def __init__(self, dir):
        self.dir = dir
        self.ary = dir.split("|")

    def show(self):
        r = "{}".format(self.dir)
        return r


newParentCount = 0


class Node:

    def __init__(self, base, depth):
        global newParentCount

        self.base = base
        self.children = {}
        self.letter = getLetterFromNumber(newParentCount)
        newParentCount += 1
        self.depth = depth
        self.x = None
        self.y = None
        self.degree = None

    def addKid(self, name):
        # kid = "{}_{}".format(incomingKid, 1 + self.depth)
        # if kid not in self.children:
        #     self.children.append(kid)
        if name not in self.children:
            kid = Node(name, self.depth + 1)
            self.children[name] = kid

    def show(self):
        return {
            self.base: self.children,
            'x': self.x,
            'y': self.y
        }

    def setDegree(self, degree):
        self.degree

    def setXY(self, x, y):
        self.x = x
        self.y = y


def getMaxDepth(ary_of_objs):
    most = 0
    for x in ary_of_objs:
        if len(x.ary) > most:
            most = len(x.ary)
    return most


def step1_gatherData():
    step1 = []
    i = 0
    for root, dirs, files in os.walk(rootPath):
        # root = root.replace(os.sep, "|")
        i += 1
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            x = x.replace(os.sep, "|")
            x = x.replace("||", "|")
            # print(x)
            step1.append(PathToLeaf(x))
    return step1


def step2_makeGenerations(deepest, results_from_step1):
    generations = []
    for j in range(1, deepest):
        map = {}
        for n in results_from_step1:
            if j < len(n.ary):
                a = n.ary[j - 1]
                b = n.ary[j]
                if a not in ignore:
                    if a not in map:
                        p = Node(a, j)
                        map[a] = p
                    map[a].addKid(b)
        if len(map) > 0:  # needed to avoid empty 'generations' due to where the path original started from
            generations.append(map)
    return generations


def step3_emit_raw_graph(generations, step1):
    n = 0
    for i in range(len(generations)):
        stack = generations[i]
        for k in stack:
            parent = stack[k]
            for nodeTo in parent.children:
                fromTo = {
                    'a': parent.base,
                    'id': parent.letter,
                    'd': parent.depth,
                    'b': nodeTo
                }
                # print("{} {} {} ".format(n, i, fromTo))
                n += 1
    # m = 0
    # for node in step1:
    #     print("{} {}".format(m, node.show()))
    #     m += 1


# def step3_getEachUniqueNode(generations):
#     count = 0
#     for i in range(len(generations)):
#         stack = generations[i]
#         for k in stack:
#             p = stack[k]
#             count += 1
#             count += len(p.children)
#             print("{}  {}   {} ".format(count, p.base, p.children))


def step3_makeGraph(generations):
    # set the very first one to be somewhere ( I choose to use nice positive numbers 'cause I am lazy )
    # Where doesn't really matter -
    # coord space will all be ratioized later on.
    n = 0
    generations[0]["src"].setXY(1000, 1000)
    generations[0]["src"].setDegree(0)

    for sibling in generations:
        for k in sibling:
            parent = sibling[k]
            degreesOfSweep = 360 / len(parent.children)
            d = 0
            for name in parent.children:
                #     print("{} and {} ".format(parent.base, kid))
                print("{}    {}    parent {}".format(n, name, parent.x))
                # xy = findNewPoint(parent.x, parent.y, d, 100)
                # parent.children[name].setXY(xy["x"], xy["y"])
                # parent.children[name].setDegree(d)
                n += 1
                d += degreesOfSweep


def findNewPoint(x, y, angle, distance):
    x = round(math.cos(angle * math.pi / 180) * distance + x)
    y = round(math.sin(angle * math.pi / 180) * distance + y)
    xy = {
        "x": x,
        "y": y
    }
    return xy


def findOpposetAngle(angle):
    oppositeAngle = (angle + 180) % 360
    return oppositeAngle


if __name__ == "__main__":
    step1 = step1_gatherData()
    deepest = getMaxDepth(step1)
    generations = step2_makeGenerations(deepest, step1)
    # step3_emit_raw_graph(generations, step1)
    # step3_getEachUniqueNode(generations)
    step3_makeGraph(generations)
