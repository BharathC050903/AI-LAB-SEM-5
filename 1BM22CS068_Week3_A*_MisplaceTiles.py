import heapq

# Function to check if the current state is the goal state
def is_goal(state, goal_state):
    return state == goal_state

# Function to get the possible moves from the current state
def get_neighbors(state):
    neighbors = []
    index = state.index(0)  # Find the blank (0)
    row, col = divmod(index, 3)

    # Define possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# Heuristic 1: Number of misplaced tiles
def misplaced_tiles(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

# Heuristic 2: Manhattan distance
def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal.index(state[i]), 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

# Function to print the state in a 3x3 format
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()  # Blank line for readability

# A* algorithm with level-wise output
def a_star_level_wise(start, goal, heuristic):
    # Priority queue to store the nodes to explore (f(n), g(n), state, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, start, []))

    visited = set()

    print("Level-wise output:")

    while priority_queue:
        f_n, g_n, current_state, path = heapq.heappop(priority_queue)

        if current_state in visited:
            continue

        visited.add(current_state)

        # Print level information
        print(f"\nLevel {g_n} (g(n) = {g_n}):")
        print(f"f(n) = {f_n}, h(n) = {heuristic(current_state, goal)}")
        print_state(current_state)

        if is_goal(current_state, goal):
            return path + [current_state]

        # Gather and print all neighbors for the current level
        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor not in visited:
                g_new = g_n + 1
                h_new = heuristic(neighbor, goal)
                f_new = g_new + h_new

                # Print the neighboring state for the next level
                print(f"    Adjacent Node (g(n) = {g_new}, h(n) = {h_new}, f(n) = {f_new}):")
                print_state(neighbor)

                # Push neighbors into the priority queue
                heapq.heappush(priority_queue, (f_new, g_new, neighbor, path + [current_state]))

    return None  # If no solution found

# Function to take 8-puzzle input from the user
def input_puzzle(prompt):
    print(prompt)
    puzzle = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (3 numbers separated by spaces): ").split()
        puzzle.extend([int(x) for x in row])
    return tuple(puzzle)

# Main code
start_state = input_puzzle("Enter the start state (use 0 for the blank space):")
goal_state = input_puzzle("Enter the goal state (use 0 for the blank space):")

# Choose heuristic
print("Select Heuristic:")
print("1. Number of Misplaced Tiles")
print("2. Manhattan Distance")
choice = input("Enter 1 or 2: ")

if choice == '1':
    heuristic = misplaced_tiles
else:
    heuristic = manhattan_distance

print("\nSolving using A* Search with level-wise output...")
a_star_solution = a_star_level_wise(start_state, goal_state, heuristic)

if a_star_solution:
    print("A* Solution found! Steps:")
    for i, step in enumerate(a_star_solution):
        print(f"Step {i + 1}:")
        print_state(step)
else:
    print("No solution found using A*.")