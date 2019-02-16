# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        def generateOneRow(lastRow):
            thisRow = [1, 1]
            index = 1
            for i, val in enumerate(lastRow[1:]):
                temp = val + lastRow[i]
                thisRow.insert(index, temp)
                index += 1
            return thisRow

        if numRows == 0:
            return []

        final = [[1]]
        if numRows == 1:
            return final

        inputRow = [1, 1]
        final.append(inputRow)
        if numRows == 2:
            return final

        for i in range(numRows - 2):
            final.append(generateOneRow(inputRow))
            inputRow = generateOneRow(inputRow)
        return final