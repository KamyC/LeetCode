# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        def generateOneRow(lastRow):
            thisRow = [1, 1]
            index = 1
            for i, val in enumerate(lastRow[1:]):
                temp = val + lastRow[i]
                thisRow.insert(index, temp)
                index += 1
            return thisRow

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        if rowIndex == 2:
            return [1, 2, 1]

        inputRow = [1, 2, 1]
        for i in range(rowIndex - 2):
            inputRow = generateOneRow(inputRow)
        return inputRow