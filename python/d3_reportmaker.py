import fnmatch
import os
import json
from letters import getLetterFromNumber
import math
pattern = "*.js"
rootPath = "../src/"
ignore = ["", ".."]


class Node:
    def __init__(self, l, dir):
        self.l = l
        self.dir = dir
        self.ary = dir.split("|")

    def show(self):
        r = "{}|{}".format(self.l, self.dir)
        return r


newParentCount = 0


class Parent:

    def __init__(self, base, depth):
        global newParentCount

        self.base = base
        self.children = []
        self.letter = getLetterFromNumber(newParentCount)
        newParentCount += 1
        self.depth = depth

    def addKid(self, kid):
        if kid not in self.children:
            self.children.append(kid)

    def show(self):
        return {
            self.base: self.children
        }


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
        l = getLetterFromNumber(i)
        i += 1
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            x = x.replace(os.sep, "|")
            x = x.replace("||", "|")
            # print(x)
            step1.append(Node(l, x))
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
                        p = Parent(a, j)
                        map[a] = p
                    map[a].addKid(b)
        generations.append(map)
    return generations


def step3_emit_raw_graph(generations):
    collections = []
    for i in range(len(generations)):
        stack = generations[i]
        for k in stack:
            parent = stack[k]
            for nodeTo in parent.children:
                fromTo = {
                    'id': parent.letter,
                    'd': parent.depth,
                    'from': parent.base,
                    'to': nodeTo
                }
                collections.append(fromTo)
    # print(json.dumps(collections))


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
    step3_emit_raw_graph(generations)
