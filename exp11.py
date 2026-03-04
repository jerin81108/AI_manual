import random, time

def check_win(b, p):
    # Check rows, columns, and the two diagonals
    win_configs = [
        b[0], b[1], b[2],                        # Rows
        [b[0][i] for i in range(3)],             # Cols (simplified)
        [b[i][0] for i in range(3)], [b[i][1] for i in range(3)], [b[i][2] for i in range(3)],
        [b[0][0], b[1][1], b[2][2]],             # Diag 1
        [b[0][2], b[1][1], b[2][0]]              # Diag 2
    ]
    return [p, p, p] in win_configs
def play():
    board = [[0]*3 for _ in range(3)]
    for turn in range(9): # Max 9 moves
        player = (turn % 2) + 1
        
        # Find empty spots and pick one
        empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == 0]
        r, c = random.choice(empty)
        board[r][c] = player
        
        print(f"Player {player} moved:\n{board[0]}\n{board[1]}\n{board[2]}\n")
        time.sleep(1)

        if check_win(board, player):
            return f"Player {player} Wins!"
            
    return "It's a Tie!"
print(play())