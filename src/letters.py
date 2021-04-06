
import math

gaint_list = []


def getLetterFromNumber(n):
    if n < len(gaint_list):
        return gaint_list[n]
    else:
        return "_" + n


if __name__ == "__main__":
    # https://www.programmersought.com/article/75954623406/

    def cycle_letter(arr, level):
        tempArr = []
        letterArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        arrNum = len(arr)
        if(level == 0 or arrNum == 0):
            return letterArr
        for index in range(arrNum):
            for letter in letterArr:
                tempArr.append(arr[index]+letter)
        return tempArr

    # arr: Number of Excel column names to be generated
    def reduce_excel_col_name(num):
        tempVal = 1
        level = 1
        while(tempVal):
            tempVal = num/(math.pow(26, level))
            if(tempVal > 1):
                level += 1
            else:
                break

        excelArr = []
        tempArr = []
        for index in range(level):
            tempArr = cycle_letter(tempArr, index)
            for numIndex in range(len(tempArr)):
                if(len(excelArr) < num):
                    excelArr.append(tempArr[numIndex])
                else:
                    return excelArr

    print(reduce_excel_col_name(1000))
