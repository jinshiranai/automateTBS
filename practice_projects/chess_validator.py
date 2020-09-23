pos_numbers = [value for value in range(1,9)]
pos_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
max_pieces = {'wpawn': 8, 'bpawn': 8, 'wking': 1, 'bking': 1, 'total': 32}

def chessboard_checker(chessboard):
    """Function for determining validity of chessboard layouts."""
    piece_total = 0
    piece_count = {}
    b_total = 0
    w_total = 0
    board_valid = True

    for k, v in chessboard.items():
        piece_total += 1
        
        # Determine piece position validity.
        if int(k[0]) not in pos_numbers or k[1] not in pos_letters:
            print(f"Invalid board: {v} out of bounds")
            board_valid = False
            break

        # Determine piece count validity.
        if piece_total > max_pieces['total']:
            print("Invalid board: Too many pieces")
            board_valid = False
            break
        if v.startswith('b'):
            b_total +=1
            if b_total > 16:
                print("Invalid board: Too many black pieces")
                board_valid = False
                break
        if v.startswith('w'):
            w_total +=1
            if w_total > 16:
                print("Invalid board: Too many white pieces")
                board_valid = False
                break
        
        piece_count.setdefault(v, 0)
        piece_count[v] += 1
        if v in max_pieces:
            if piece_count[v] > max_pieces[v]:
                print(f"Invalid board: Too many {v}")
                board_valid = False
                break
    
    if board_valid:
        print("Board valid!")


board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
            '3e': 'wking'}
board2 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
            '3e': 'bking'}
board3 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
            '3e': 'wking', '5c': 'wqueen', '4c': 'wqueen', '3c': 'wqueen',
            '8c': 'wqueen', '7c': 'wqueen', '1c': 'wqueen', '2c': 'wqueen',
            '6d': 'wqueen', '6e': 'wqueen', '6f': 'wqueen', '6g': 'wqueen',
            '5d': 'wqueen', '7f': 'wqueen', '6b': 'wqueen', '6a': 'wqueen',}
board4 = {'1h': 'bking', '6c': 'wqueen', '2z': 'bbishop', '5h': 'bqueen',
            '3e': 'wking'}

chessboard_checker(board1)
chessboard_checker(board2)
chessboard_checker(board3)
chessboard_checker(board4)