from collections import deque


# Function to find the solution to the Water Jug problem
def solve_water_jug_problem(capacity1, capacity2, target1, target2):
    # Create a queue for BFS
    queue = deque()

    # Create a set to store visited states
    visited = set()

    # Initialize the starting state with both jugs empty
    start_state = (0, 0)

    # Enqueue the starting state
    queue.append((start_state, []))

    # BFS algorithm
    while queue:
        state, path = queue.popleft()
        jug1, jug2 = state

        # Check if the targets are reached
        if jug1 == target1 and jug2 == target2:
            return path + [state]

        # Check if the current state has already been visited
        if state in visited:
            continue

        # Mark the current state as visited
        visited.add(state)

        # Generate all possible next states and add them to the queue
        # Fill Jug 1
        queue.append(((capacity1, jug2), path + [state]))
        # Fill Jug 2
        queue.append(((jug1, capacity2), path + [state]))
        # Empty Jug 1
        queue.append(((0, jug2), path + [state]))
        # Empty Jug 2
        queue.append(((jug1, 0), path + [state]))
        # Pour from Jug 1 to Jug 2
        pour_amount = min(jug1, capacity2 - jug2)
        queue.append(((jug1 - pour_amount, jug2 + pour_amount), path + [state]))
        # Pour from Jug 2 to Jug 1
        pour_amount = min(jug2, capacity1 - jug1)
        queue.append(((jug1 + pour_amount, jug2 - pour_amount), path + [state]))

    # If the targets cannot be reached
    return None


# Main program
def main():
    print("Water Jug Problem Solver")

    # Get the jug capacities and target volumes from the user
    capacity1 = int(input("Enter the capacity of Jug 1: "))
    capacity2 = int(input("Enter the capacity of Jug 2: "))
    target1 = int(input("Enter the target volume for Jug 1: "))
    target2 = int(input("Enter the target volume for Jug 2: "))

    # Solve the Water Jug problem
    solution = solve_water_jug_problem(capacity1, capacity2, target1, target2)

    # Display the solution
    if solution is None:
        print("No solution found.")
    else:
        print("Solution:")
        for state in solution:
            print(f"Jug 1: {state[0]}, Jug 2: {state[1]}")


# Run the program
if __name__ == "__main__":
    main()
