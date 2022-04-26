class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rowLength = len(obstacleGrid[0])
        row = rowLength * [0]
        noWay = False

        
        for i in range(len(obstacleGrid) - 1, -1, -1):
            newRow = rowLength * [0]
            for j in range(rowLength - 1, -1, -1):
                if j + 1 == rowLength:
                    if i == len(obstacleGrid) - 1:
                        newRow[j] = 1
                    if row[j] > 0:
                        newRow[j] = 1 - obstacleGrid[i][j]

                    #newRow[j] = 0
                    continue;
                
                if obstacleGrid[i][j] is not 1:
                    if obstacleGrid[i][j + 1] is not 1:
                        newRow[j] = newRow[j + 1] + row[j]
                    else:
                        newRow[j] = row[j]
                else:
                    newRow[j] = 0
                
            noWay = noWay or all(path == 0 for path in newRow)
            row = newRow
        
        ## in case the end has an obstacle, or there is a full row of obstacles
        ## there is no way for the robot to reach the end

        if obstacleGrid[len(obstacleGrid) - 1][rowLength - 1] == 1:
            noWay = True
        if noWay:
            return 0
        
        return row[0]
    

