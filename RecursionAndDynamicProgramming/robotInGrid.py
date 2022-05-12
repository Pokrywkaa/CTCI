def path(maze):
    if not maze:
        return None
    path=[]
    if is_path(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None
        

def is_path(maze, row, col, path):
    if row < 0 or col < 0 or not maze[row][col]:
        return False
    
    isAtOrigin = row == 0 and col == 0
    
    if (isAtOrigin or is_path(maze, row, col-1, path) 
                        or is_path(maze, row-1, col, path)):
        path.append((row, col))
        return True
    return False

print(path([[1,1,1], [0,1,0], [0,1,1]]))