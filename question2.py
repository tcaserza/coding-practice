def minimumDistance(numRows, numColumns, area):
    fewest_steps = walk_path(0, 0, area, numColumns, numRows, None)
    return fewest_steps

def walk_path(x, y, area, maxX, maxY, fewest_steps):
    if area[x][y] == 9:
        area[x][y] = 2
        total_steps = count_steps(area)
        if not fewest_steps or total_steps < fewest_steps:
            fewest_steps = total_steps
    area[x][y] = 2
    if x+1 < maxX and (area[x+1][y] == 1 or area[x+1][y] == 9):
        fewest_steps = walk_path(x+1, y, area, maxX, maxY, fewest_steps)
    if x-1 >= 0 and (area[x-1][y] == 1 or area[x-1][y] == 9):
        fewest_steps = walk_path(x-1, y, area, maxX, maxY, fewest_steps)
    if y+1 < maxY and (area[x][y+1] == 1 or area[x][y+1] == 9):
        fewest_steps = walk_path(x, y+1, area, maxX, maxY, fewest_steps)
    if y-1 >= 0 and (area[x][y-1] == 1 or area[x][y-1] == 9):
        fewest_steps = walk_path(x, y-1, area, maxX, maxY, fewest_steps)
    return fewest_steps


def count_steps(area):
    total_steps = 0
    got_to_end = True
    for row in area:
        total_steps += row.count(2)
        if row.count(9) > 0:
            got_to_end = False
            return None
    return total_steps - 1

print minimumDistance(5,5,[[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,9]])