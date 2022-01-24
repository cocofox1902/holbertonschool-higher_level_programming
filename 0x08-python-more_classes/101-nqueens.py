#!/usr/bin/python3
"""module to calcule nqueens"""
import sys


def queenInTheWay(queenPlace, queenToPlace):
    """ Function to know if a queenToPlace is in the way

        Args:
            queenPlace(list): queenPlace placed so far
            queenToPlace(tuple): queenToPlace to check

        Returns:
            True or false
    """

    for (x, y) in queenPlace:
        if y == queenToPlace[1]:
            return(False)
        if abs((y - queenToPlace[1]) / (x - queenToPlace[0])) == 1:
            return(False)
    return(True)


def placeQueen(n, queenPlace, sol):
    """ Function to place a second queen

        Args:
            n(int): how many queen to place
            queenPlace(list): number of queen place
            sol(list): queen localisation
    """

    if len(queenPlace) == n:
        sol.append([list(q) for q in queenPlace])
        return()

    for y in range(n):
        queenToPlace = (len(queenPlace), y)
        if queenInTheWay(queenPlace, queenToPlace):
            queenPlace.append(queenToPlace)
            placeQueen(n, queenPlace, sol)
            queenPlace.pop()


def goodPositon():
    """ Function to know if you can place your queen

        Returns:
            valide or not
    """

    if len(sys.argv) != 2:
        print('Usage: nqueenPlace N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n <= 3:
        print('N must be at least 4')
        sys.exit(1)
    return(n)


def main():
    """ Function main

        Return:
            the localisation of where you can put your piece
    """

    n = goodPositon()
    queenPlace = []
    sol = []
    placeQueen(n, queenPlace, sol)
    print("\n".join(str(s) for s in sol))


if __name__ == '__main__':
    main()
