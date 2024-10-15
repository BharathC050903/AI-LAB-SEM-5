from collections import deque

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

# Function to print the state in a 3x3 format
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()  # Blank line for readability

# DFS algorithm to solve the 8-puzzle
def dfs(start, goal):
    visited = set()
    stack = [(start, [])]

    while stack:
        current_state, path = stack.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal(current_state, goal):
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                stack.append((neighbor, path + [current_state]))

    return None  # If no solution found

# Function to take 8-puzzle input from the user
def input_puzzle(prompt):
    print(prompt)
    puzzle = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (3 numbers separated by spaces): ").split()
        puzzle.extend([int(x) for x in row])
    return tuple(puzzle)

# Function to select goal state
def select_goal_state():
    print("Select a goal state:")
    print("1. Goal State:")
    print("   0 1 2")
    print("   3 4 5")
    print("   6 7 8")
    print("2. Goal State:")
    print("   1 2 3")
    print("   4 5 6")
    print("   7 8 0")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        return (0, 1, 2, 3, 4, 5, 6, 7, 8)
    else:
        return (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Main code
start_state = input_puzzle("Enter the start state (use 0 for the blank space):")
goal_state = select_goal_state()

print("\nSolving using DFS...")
dfs_solution = dfs(start_state, goal_state)

if dfs_solution:
    print("DFS Solution found! Steps:")
    for i, step in enumerate(dfs_solution):
        print(f"Step {i + 1}:")
        print_state(step)
else:
    print("No solution found using DFS.")