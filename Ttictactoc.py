class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        print("---------")
        for row in self.board:
            print('|'.join(row))
            print("---------")

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True

        # Check columns
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]):
            return True
        if all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def is_full(self):
        return all([cell != ' ' for row in self.board for cell in row])

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        print("ברוכים הבאים לאיקס עיגול!")
        self.print_board()
        while True:
            try:
                move = input(f"שחקן {self.current_player}, הזן שורה ועמודה (0, 1, 2) מופרדות ברווח: ")
                row, col = map(int, move.strip().split())
                if row in range(3) and col in range(3):
                    if self.make_move(row, col):
                        self.print_board()
                        if self.is_winner(self.current_player):
                            print(f"שחקן {self.current_player} ניצח!")
                            break
                        elif self.is_full():
                            print("תיקו!")
                            break
                        self.switch_player()
                    else:
                        print("מקום זה כבר תפוס, נסה שוב.")
                else:
                    print("אנא הזן ערכים בין 0 ל-2.")
            except Exception:
                print("קלט לא תקין, נסה שוב.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()