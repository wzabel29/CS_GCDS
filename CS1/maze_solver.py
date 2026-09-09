# 0 = Path, 1 = Wall, 2 = Start, 3 = Exit
maze = [
    [2, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 3],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

ROWS = len(maze)
COLS = len(maze[0])

def solve_maze(r, c):
    # 1. Base Case: Check for out-of-bounds index
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return False

    # 2. Base Case: Hit the exit!
    if maze[r][c] == 3:
        print(f"Reached the exit at ({r}, {c})!")
        return True

    # 3. Base Case: Hit a wall or an already visited cell
    if maze[r][c] == 1 or maze[r][c] == 7:
        return False

    # Mark the current cell as visited (if it's not the start position)
    if maze[r][c] != 2:
        maze[r][c] = 7

    # 4. Recursive Step: Try moving in all 4 directions (Down, Right, Up, Left)
    if solve_maze(r + 1, c): # Move Down
        return True
    if solve_maze(r, c + 1): # Move Right
        return True
    if solve_maze(r - 1, c): # Move Up
        return True
    if solve_maze(r, c - 1): # Move Left
        return True

    # Backtrack: If no direction works, return False
    return False

# Run the solver starting at position (0, 0)
if solve_maze(0, 0):
    print("Path found successfully!")
else:
    print("No path found.")