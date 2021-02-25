def countNewArrSide(width, height):
    if (height <= width):
        return height

    if (width < height):
        return width


def createDoubleArr(height, width):
    newDoubleArr = [0] * height
    for i in range(height):
        newDoubleArr[i] = [0] * width
    return newDoubleArr


def buildNewList(doubleArr):
    height = len(doubleArr)
    width = len(doubleArr[0])

    newArrSide = countNewArrSide(width, height)
    newArr = createDoubleArr(newArrSide, newArrSide)

    for i in range(newArrSide):
        for j in range(newArrSide):
            newArr[i][j] = doubleArr[i][j]
    return newArr


if __name__ == '__main__':
    print(buildNewList([[1, 2, 3], [4, 5]]))
