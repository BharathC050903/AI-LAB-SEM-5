import random

def is_safe(board, row, col, n):
  """Checks if it's safe to place a queen at the given position."""
  for i in range(row):
    if board[i] == col or \
       board[i] - i == col - row or \
       board[i] + i == col + row:
      return False
  return True

def calculate_cost(board, n):
  """Calculates the number of pairs of queens attacking each other."""
  cost = 0
  for i in range(n):
    for j in range(i + 1, n):
      if board[i] == board[j] or \
         board[i] - i == board[j] - j or \
         board[i] + i == board[j] + j:
        cost += 1
  return cost


def hill_climbing(n):
  """Solves the N-Queens problem using Hill Climbing."""
  current_board = [random.randint(0, n - 1) for _ in range(n)]
  current_cost = calculate_cost(current_board, n)

  while True:
    neighbors = []
    for i in range(n):
      for j in range(n):
        if j != current_board[i]:
          neighbor_board = current_board[:]
          neighbor_board[i] = j
          neighbors.append(neighbor_board)

    best_neighbor = None
    best_neighbor_cost = float('inf')

    for neighbor in neighbors:
      neighbor_cost = calculate_cost(neighbor, n)
      if neighbor_cost < best_neighbor_cost:
        best_neighbor_cost = neighbor_cost
        best_neighbor = neighbor


    if best_neighbor is None or best_neighbor_cost >= current_cost:
      return current_board, current_cost

    print(f"Current Board: {current_board} \nCurrent Cost: {current_cost}")
    current_board = best_neighbor
    current_cost = best_neighbor_cost

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)


# Example usage for 8-Queens problem
n = 5
solution_board, solution_cost = hill_climbing(n)
print("Solution Board:")
print_board(solution_board)
print("Cost (number of attacking pairs):", solution_cost)