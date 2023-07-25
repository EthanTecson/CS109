def life(rows, columns, generations, initialCells):
    grid = makeGrid(rows, columns)
    initialize(grid, intitialCells)

    for g in range(generations):
        newGrid = copy.deepcopy(grid)
        for r in range(rows):
            for c in range(columns):
                neighbors = neighborhood(grid, r, c)
                if grid[r][c] == ALIVE and neighbors < 2:
                    