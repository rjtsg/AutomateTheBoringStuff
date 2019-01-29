tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(TableData):
    colWidths = [0] * len(TableData)
    for i in range(len(TableData)):
        big = 0
        for j in range(len(TableData[i])):
            if len(TableData[i][j]) > big:
                big = len(TableData[i][j])
        colWidths[i] = big
    
    for k in range(len(TableData[0])):
        #i = range(len(TableData))
        print(TableData[0][k].rjust(colWidths[0],' ') + TableData[1][k].rjust(colWidths[1]+1,' ') + TableData[2][k].rjust(colWidths[2]+1,' '))
        #print(i)

printTable(tableData)
