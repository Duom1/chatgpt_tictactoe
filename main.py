import pygame

# Initialize pygame
pygame.init()

# Set the screen size
size = (400, 400)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Tic Tac Toe")

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load font
font = pygame.font.Font(None, 100)

# Initialize board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Initialize player
player = 'X'

def check_winner():
    # check rows
    for row in board:
        if row == ['X','X','X']:
            return 'X'
        elif row == ['O','O','O']:
            return 'O'
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] != ' ':
                return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != ' ':
            return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != ' ':
            return board[0][2]
    return None

def check_tie():
    for row in board:
        if ' ' in row:
            return False
    return True

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Get the column and row
            col = pos[0] // (size[0] // 3)
            row = pos[1] // (size[1] // 3)
            # Check if the spot is empty
            if board[row][col] == ' ':
                # Make a move
                board[row][col] = player
                # Switch player
                player = 'X' if player == 'O' else 'O'
                #Check for winner
                if check_winner()== 'X':
                    print("Player X wins!")
                    running = False
                elif check_winner()== 'O':
                    print("Player O wins!")
                    running = False
                elif check_tie()== True:
                    print("It's a tie!")
                    running = False
    # Clear the screen
    screen.fill(white)
    # Draw the board
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, black, (col*(size[0]//3), row*(size[1]//3), (size[0]//3), (size[1]//3)), 2)
            text = font.render(board[row][col], True, black)
            text_rect = text.get_rect(center=(col*(size[0]//3)+(size[0]//6), row*(size[1]//3)+(size[1]//6)))
            screen.blit(text, text_rect)
    # Update the screen
    pygame.display.flip()

    pygame
