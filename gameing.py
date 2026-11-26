import random


def create_board(size: int) -> list[list[str]]:
    return [["." for _ in range(size)] for _ in range(size)]


def print_board(board: list[list[str]], px: int, py: int) -> None:
    for y, row in enumerate(board):
        cells = []
        for x, cell in enumerate(row):
            if x == px and y == py:
                cells.append("P")
            else:
                cells.append(cell)
        print(" ".join(cells))
    print()


def play_game(size: int = 5, max_moves: int = 10) -> None:
    board = create_board(size)
    px, py = 0, 0

    # Place treasure away from the starting position (0, 0)
    while True:
        tx = random.randrange(size)
        ty = random.randrange(size)
        if (tx, ty) != (0, 0):
            break

    moves_left = max_moves
    directions = {
        "w": (0, -1),  # up
        "s": (0, 1),   # down
        "a": (-1, 0),  # left
        "d": (1, 0),   # right
    }

    print(f"Find the treasure in {max_moves} moves! Move with w/a/s/d, or q to quit.")

    while moves_left > 0:
        print(f"Moves left: {moves_left} | Position: ({px}, {py})")
        print_board(board, px, py)

        cmd = input("Move (w/a/s/d/q): ").strip().lower()
        if cmd == "q":
            print("Game quit.")
            return

        if cmd not in directions:
            print("Invalid input. Use w, a, s, d, or q.\n")
            continue

        dx, dy = directions[cmd]
        nx, ny = px + dx, py + dy

        if not (0 <= nx < size and 0 <= ny < size):
            print("Hit the wall! Try another direction.\n")
            continue

        board[py][px] = "*"  # mark visited tile
        px, py = nx, ny
        moves_left -= 1

        if (px, py) == (tx, ty):
            print(f"You found the treasure at ({tx}, {ty}) with {moves_left} moves left!")
            return

        dist = abs(tx - px) + abs(ty - py)
        print(f"Hint: Manhattan distance to treasure is {dist}.\n")

    print(f"Out of moves! The treasure was at ({tx}, {ty}).")


if __name__ == "__main__":
    play_game()