import heapq
from collections import deque

# Define the maze as a 2D list
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and goal positions
start = (0, 0)
goal = (4, 4)

# Depth-First Search (DFS) implementation
def dfs(maze, start, goal):
    stack = [start]
    visited = set()
    came_from = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            break
        
        if current in visited:
            continue

        visited.add(current)

        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and neighbor not in visited:
                stack.append(neighbor)
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

# Breadth-First Search (BFS) implementation
def bfs(maze, start, goal):
    queue = deque([start])
    visited = set()
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break
        
        if current in visited:
            continue

        visited.add(current)

        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and neighbor not in visited:
                queue.append(neighbor)
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

# Uniform Cost Search (UCS) implementation
def ucs(maze, start, goal):
    pq = [(0, start)]
    visited = {start: 0}
    came_from = {start: None}

    while pq:
        current_cost, current = heapq.heappop(pq)

        if current == goal:
            break

        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                new_cost = current_cost + 1
                if neighbor not in visited or new_cost < visited[neighbor]:
                    visited[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
                    came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

# A* Search implementation
def a_star(maze, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = [(heuristic(start, goal), 0, start)]
    visited = {start: 0}
    came_from = {start: None}

    while pq:
        _, current_cost, current = heapq.heappop(pq)

        if current == goal:
            break

        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                new_cost = current_cost + 1
                if neighbor not in visited or new_cost < visited[neighbor]:
                    visited[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(pq, (priority, new_cost, neighbor))
                    came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

# Best-First Search implementation
def best_first_search(maze, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = [(heuristic(start, goal), start)]
    visited = set()
    came_from = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        if current in visited:
            continue

        visited.add(current)

        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

# Path reconstruction function
def reconstruct_path(came_from, start, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    return path[::-1]

# Display the maze and path
def display_maze(maze, path=None):
    maze_copy = [row[:] for row in maze]
    if path:
        for x, y in path:
            maze_copy[x][y] = 2  

    for row in maze_copy:
        print(" ".join(str(cell) for cell in row))
    print()

# Main function to execute the search
def main():
    algorithms = {
        'DFS': dfs,
        'BFS': bfs,
        'UCS': ucs,
        'A*': a_star,
        'Best-First': best_first_search
    }

    print("Available algorithms:")
    for name in algorithms:
        print(f"- {name}")
    
    choice = input("Select a search algorithm: ").strip()

    if choice in algorithms:
        path = algorithms[choice](maze, start, goal)
        if path:
            print("Path found:")
            display_maze(maze, path)
        else:
            print("No path found.")
    else:
        print("Invalid choice!")

    if input("Would you like to solve another maze? (y/n): ").strip().lower() == 'y':
        main()

if __name__ == "__main__":
    main()
