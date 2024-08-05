import ChessEngine as ce
import chess as ch
import pygame

class Main:
    def __init__(self, board=ch.Board()):
        self.board = board

    def playHumanMove(self):
        move_made = False
        while not move_made:
            try:
                print(self.board.legal_moves)
                print("""To undo your last move, type "undo".""")
                play = input("Your move: ")
                if play == "undo":
                    self.board.pop()
                    self.board.pop()
                    self.playHumanMove()
                    return
                self.board.push_san(play)
                move_made = True
            except:
                print("Invalid move, try again.")
                self.playHumanMove()

    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        best_move = engine.getBestMove()
        self.board.push(best_move)

    def startGame(self):
        color = None
        while color not in ["b", "w"]:
            color = input("""Play as (type "b" or "w"): """).strip().lower()

        max_depth = None
        while not isinstance(max_depth, int):
            try:
                max_depth = int(input("""Choose depth: """))
            except ValueError:
                print("Please enter a valid integer for depth.")

        running = True
        screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Chess Bot')
        load_images()
        clock = pygame.time.Clock()

        while running:
            screen.fill(pygame.Color("white"))
            draw_board(screen, self.board)
            pygame.display.flip()
            clock.tick(15)

            if color == "b":
                while not self.board.is_checkmate() and running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                    print("The engine is thinking...")
                    self.playEngineMove(max_depth, ch.WHITE)
                    screen.fill(pygame.Color("white"))
                    draw_board(screen, self.board)
                    pygame.display.flip()
                    clock.tick(15)

                    print(self.board)
                    self.playHumanMove()
                    screen.fill(pygame.Color("white"))
                    draw_board(screen, self.board)
                    pygame.display.flip()
                    clock.tick(15)
                    print(self.board)
            elif color == "w":
                while not self.board.is_checkmate() and running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                    print(self.board)
                    self.playHumanMove()
                    screen.fill(pygame.Color("white"))
                    draw_board(screen, self.board)
                    pygame.display.flip()
                    clock.tick(15)
                    print(self.board)

                    print("The engine is thinking...")
                    self.playEngineMove(max_depth, ch.BLACK)
                    screen.fill(pygame.Color("white"))
                    draw_board(screen, self.board)
                    pygame.display.flip()
                    clock.tick(15)
                    print(self.board)

            print(self.board)
            print(self.board.outcome())

            self.board.reset()

def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(f"images/{piece}.png"), (100, 100))

def draw_board(screen, board):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * 100, r * 100, 100, 100))
            piece = board.piece_at(ch.square(c, 7-r))
            if piece:
                piece_symbol = piece.symbol()
                image_key = ('w' if piece_symbol.isupper() else 'b') + piece_symbol.upper()
                if image_key in IMAGES:
                    screen.blit(IMAGES[image_key], pygame.Rect(c * 100, r * 100, 100, 100))

if __name__ == "__main__":
    pygame.init()
    IMAGES = {}
    new_board = ch.Board()
    game = Main(new_board)
    game.startGame()
