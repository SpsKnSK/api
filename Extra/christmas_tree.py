from random import randint, choice
from termcolor import colored

# global variables eeeck
treeWidth = 11
green, darkGrey, yellow, red = "green", "dark_grey", "yellow", "red"


def CreateTopDecoration(treeWidth: int) -> str:
    return colored("^".rjust(treeWidth), red)


def CreateRowWithDecorations(branchLenght: int) -> str:
    row = list(" " * (branchLenght * 2 - 1))
    for _ in range(randint(1, 5)):
        decoration = (
            choice(["%", "@", "#", "*", "&"]) if randint(1, 2) % 2 == 0 else " "
        )
        randomColumn = randint(0, branchLenght * 2 - 2)
        row[randomColumn] = (
            decoration if row[randomColumn] == " " else row[randomColumn]
        )
    return colored("".join(row), yellow)


def CreateLeftBranch(treeWidth: int, branchLength: int) -> str:
    return colored("/".rjust(treeWidth - branchLength), green)


def CreateRightBranch() -> str:
    return colored("\\", green)


def CreateBottom(treeWidth: int) -> str:
    return colored("-" * treeWidth * 2, green)


def CreateTrunkRow(treeWidth: int, columnCount:int = 5, layerCount:int=3) -> str:
    return "\n".join([colored(("|" * columnCount).rjust(treeWidth + 2), darkGrey) for _ in range(layerCount)])


def Main()->None:
    print(CreateTopDecoration(treeWidth))
    for i in range(1, treeWidth):
        print(CreateLeftBranch(treeWidth, i) + CreateRowWithDecorations(i) + CreateRightBranch())
    print(CreateBottom(treeWidth))
    print(CreateTrunkRow(treeWidth))

Main()
