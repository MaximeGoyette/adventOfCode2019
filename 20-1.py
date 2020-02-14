data = '''                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P               '''.split('\n')

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def find_adjacent(grid, x, y):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= y < len(grid) and grid[ny][nx] in alphabet:
            return nx, ny

def parse_grid(grid, alphabet=''):
    walkable = set()
    poi = {}
    start_pos = None
    end_pos = None

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if grid[y][x] == '.':
                walkable.add((x, y))
            elif grid[y][x] in alphabet:
                px, py, ox, oy = find_adjacent(grid, x, y, alphabet=alphabet)
                uid = grid[y][x] + grid[py][px]
                if uid == 'AA':
                    start_pos
                if not uid in poi:
                    poi[uid] = []
                poi[uid].append((x, y))

    teleports = {}

    for uid, (pos1, pos2)  in poi.items():
        teleports[pos1] = pos2
        teleports[pos2] = 

    return walkable, teleports



walkable, teleports = parse_grid(data)