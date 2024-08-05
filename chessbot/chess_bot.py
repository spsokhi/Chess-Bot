import chess
import chess.engine

def get_best_move(board, engine_path):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        return result.move

def print_board(board):
    board_str = str(board)
    board_lines = board_str.split("\n")
    board_lines = [f"{8-i} {line}" for i, line in enumerate(board_lines)]
    board_lines.append("  a b c d e f g h")
    print("\n".join(board_lines))

def algebraic_to_uci(board, move):
    try:
        return board.parse_san(move).uci()
    except ValueError:
        return move

def main():
    engine_path = "/path/to/your/stockfish/executable" # path to the Stockfish binary
    board = chess.Board()

    color = input("Do you want to play as white or black? (w/b): ").strip().lower()
    player_color = chess.WHITE if color == 'w' else chess.BLACK

    while not board.is_game_over():
        print_board(board)

        if player_color == chess.WHITE:
            if board.turn == chess.WHITE:
                best_move = get_best_move(board, engine_path)
                board.push(best_move)
                print(f"Bot's move: {best_move}")
            else:
                move = input("Enter black's move (e.g., e5 or Nf6): ").strip()
                move = algebraic_to_uci(board, move)
                try:
                    board.push_uci(move)
                except ValueError:
                    print("Invalid move. Try again.")
                    continue
        else:
            if board.turn == chess.BLACK:
                best_move = get_best_move(board, engine_path)
                board.push(best_move)
                print(f"Bot's move: {best_move}")
            else:
                move = input("Enter white's move (e.g., e4 or Nf3): ").strip()
                move = algebraic_to_uci(board, move)
                try:
                    board.push_uci(move)
                except ValueError:
                    print("Invalid move. Try again.")
                    continue

        print("\n")

    print("Game over!")
    print(board.result())

if __name__ == "__main__":
    main()
