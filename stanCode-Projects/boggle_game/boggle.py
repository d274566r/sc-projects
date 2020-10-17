"""
File: boggle.py
Name: 謝濡駿
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic = []
word_count = 0
word_list = []


def main():
    """
    TODO:
    """
    read_dictionary()
    word_board = create_word_board()
    # word_board = ['f', 'y', 'c', 'l', 'i', 'o', 'm', 'g', 'o', 'r', 'i', 'l', 'h', 'j', 'h', 'u']
    print(word_board)
    board_index = []
    for i in range(4):
        for j in range(4):
            board_index.append((i, j))
    print(board_index)
    for k in range(len(word_board)):
        boggle_game(word_board[k], board_index[k], word_board, board_index)
    print(f'There are {word_count} words in total')


def boggle_game(start, start_position, word_board, board_index):
    current_ch = ''
    current_ch += start
    visited = []
    visited.append(start_position)

    boggle_game_helper(start, start_position, [], visited, current_ch, word_board, board_index)


def boggle_game_helper(character, start_position, neighbors, visited, current_ch, word_board, board_index):
    global dic
    global word_count
    global word_list

    if len(current_ch) >= 4:
        if current_ch not in word_list:
            if current_ch in dic:
                word_count += 1
                print(f'Found: "{current_ch}"')
                word_list.append(current_ch)

    if has_prefix(current_ch) is False:
        pass

    else:
        
        neighbors = get_neighbors(visited[len(visited)-1], visited)
        for position in neighbors:
            
            i = board_index.index(position)
            
            # choose
            if has_prefix(current_ch):
                visited.append(position)

                boggle_game_helper(character, start_position, neighbors, visited, current_ch+word_board[i], word_board, board_index)
            
                visited.pop()


def get_neighbors(start_position, visited):
    neighbors = []
    row = start_position[1]  # y position
    col = start_position[0]  # x position
    for x in range(-1, 2):
        for y in range(-1, 2):
            row_plus_y = row + y
            col_plus_x = col + x
            if 0 <= col_plus_x < 4:
                if 0 <= row_plus_y < 4:
                    if (col_plus_x, row_plus_y) not in visited:
                        neighbors.append((col_plus_x, row_plus_y))
    return neighbors


def create_word_board():
    """
    :return:
    """
    board = []
    for i in range(4):
        line = input(f'{i+1} row of letters: ')
        if len(line) != 7 and line[1] != ' ' or line[3] != ' ' or line[5] != ' ':
            print('format incorrect')
            break
        else:
            chs = line.strip()
            chs = chs.split()
            for ch in chs:
                ch = ch.lower()
                board.append(ch)
    return board


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global dic
    with open(FILE, 'r') as d:
        for line in d:
            new_line = line.strip()
            dic.append(new_line)


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    global dic
    # start_with = ''
    # for ele in sub_s:
    #     start_with += ele
    for vocabulary in dic:
        if vocabulary.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
