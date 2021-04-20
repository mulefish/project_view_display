import fnmatch
import os
import json
from letters import getLetterFromNumber
import math
pattern = "*.js"
rootPath = "../src/"


class Node:
    def __init__(self, name, depth):
        self.name = name
        self.kids = []
        self.depth = depth

    def addChild(self, kid):
        if kid not in self.kids:
            k = {"name": kid}
            self.kids.append(k)

    def show(self):
        return {
            'name': self.name, 'kids': self.kids
        }


NILL = "NILL"
ignore = [NILL]


def getUniques(ary, depth):
    nodes = {}
    for item in ary:
        if item not in nodes:
            if item != NILL:
                nodes[item] = Node(item, depth)
    return nodes


def step1_gatherData():
    found = []
    most = 0
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            x = x.replace(os.sep, "|")
            x = x.replace("||", "|")
            x = x.replace("..|", "")
            ary = x.split("|")
            found.append(ary)
            if len(ary) > most:
                most += 1
    for j in range(len(found)):
        n = most - len(found[j])
        for i in range(n):
            found[j].append(NILL)

    # for ary in found:
    #     print(ary)

    rotated = zip(*reversed(found))
    generations = []
    # assumption: the 0th 'generation' has only one member called 'src'
    seen = {}
    for i in range(1, len(rotated)):
        j = i - 1
        rowA = rotated[j]
        parents = getUniques(rowA, j)

        rowB = rotated[i]

        for k in range(len(rowB)):
            a = rowA[k]
            b = rowB[k]
            if b != NILL:

                compoundname = "{}_{}_{}".format(j, a, b)
                if compoundname not in seen:
                    seen[compoundname] = ""
                    parents[a].addChild(b)
        generations.append(parents)
        # for k in parents:
        #     n = parents[k]
        #     print("{}    {}".format(k, n.show()))

    m = 0
    for parents in generations:
        for k in parents:
            p = parents[k]
            print("{}   {} {}".format(m, p.depth, p.name))
            m += 1

    m = 0
    for i in range(len(generations)):
        parents = generations[i]
        for k in parents:
            n = parents[k]
            padding = pad(i)
            for kidmap in n.kids:
                kidname = kidmap["name"]
                print("{} {} {}    {}\t\t\t\t\t{}".format(
                    m, padding, i, n.name, kidname))
                m += 1


def pad(n):
    padding = ""
    for i in range(n):
        padding += "---"
    return padding


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
