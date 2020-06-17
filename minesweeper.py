from random import randint
import itertools
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-16s %(levelname)-12s %(lineno)-6s %(funcName)-28s %(message)-8s',
                    datefmt='%H:%M:%SS'
                    )


def play_minesweeper():
    minefield_rows = 4
    minefield_columns = 4

    logging.debug("set random mine row and column index given minefield size")
    mine_row_index = randint(0, minefield_rows - 1)
    mine_column_index = randint(0, minefield_columns - 1)
    logging.debug("mine is at: ({0}, {1})".format(mine_row_index, mine_column_index))

    def find_ones_possible_indices(mine_index, minefield_length):
        """
        Finds all possible indices of 1s that surround mine
        Function only works under assumption that minefield is square (all sides equal)
        :param mine_index: index of the mine for its corresponding row or column
        :param minefield_length: count of squares along one edge of minefield
        :return: one_indices
        """
        one_indices = []
        if mine_index == minefield_length - 1:
            logging.debug("mine is located in the bottom row of hidden_minefield")
            logging.debug("1s can only be in 2nd to bottom row and bottom row of hidden_minefield")
            for one_index in range(mine_index - 1, mine_index + 1):
                one_indices.append(one_index)
        elif mine_index == 0:
            logging.debug("mine is in the first aka top row of hidden_minefield")
            logging.debug("1s can only be in the top and 2nd to the top row of hidden_minefield")
            for one_index in range(mine_index, mine_index + 2):
                one_indices.append(one_index)
        else:
            logging.debug("mine is located in one of the middle rows")
            logging.debug("1s can be above, on same and below the row of the mine in hidden_minefield")
            for one_index in range(mine_index - 1, mine_index + 2):
                one_indices.append(one_index)
        return one_indices

    row_ones_indices = find_ones_possible_indices(mine_row_index, minefield_rows)
    logging.debug("row_ones_indices: {0}".format(row_ones_indices))
    column_ones_indices = find_ones_possible_indices(mine_column_index, minefield_columns)
    logging.debug("column_ones_indices: {0}".format(column_ones_indices))

    logging.debug("create list with list items of potential row indices and column indices of 1s")
    coordinate_indices_lists = [row_ones_indices, column_ones_indices]
    logging.debug("coordinate_indices_lists: {0}".format(coordinate_indices_lists))

    logging.debug("create empty list to store all possible coordinates of positions of 1s; not all coord. on field")
    ones_coordinates = []
    logging.debug("find cartesian product of values in coordinate_indices_lists")
    for coordinate in itertools.product(*coordinate_indices_lists):
        logging.debug("append coordinate of 1 to ones_coordinates")
        ones_coordinates.append(coordinate)
    logging.debug("ones_coordinates: {0}".format(ones_coordinates))

    logging.debug("generate hidden_minefield variable as a list of lists")
    hidden_minefield = [[] for _ in range(minefield_rows)]

    logging.debug("create counter for all 1s and 0s")
    count_ones_and_zeros = 0

    logging.debug("loop over all values in hidden_minefield; fill in with appropriate values")
    for row_index in range(minefield_rows):
        for column_index in range(minefield_columns):

            # check if this value on the hidden_minefield is the value of the mine
            if (row_index, column_index) == (mine_row_index, mine_column_index):
                hidden_minefield[row_index].append(9)

            # check if this value on the hidden_minefield is in the ones_coordinates list
            elif (row_index, column_index) in ones_coordinates:
                hidden_minefield[row_index].append(1)
                count_ones_and_zeros += 1

            # the value is not the mine or adjacent to the mine
            else:
                hidden_minefield[row_index].append(0)
                count_ones_and_zeros += 1

    logging.debug("output hidden_minefield with each row on a newline")
    for row in hidden_minefield:
        logging.debug(row)

    logging.debug("create the user interface minefield of all ? values")
    user_interface_minefield = [[] for _ in range(minefield_rows)]
    for empty_list in user_interface_minefield:
        for i in range(minefield_columns):
            empty_list.append('?')

    logging.debug("sleep so print messages appear after logging messages")
    time.sleep(0.5)

    print("Time for the user to play! Try to avoid the mines!")
    # only enough guesses for user to guess all 1s and 0s; otherwise, user guesses mine and game ends
    for guess_counter, guess in enumerate(range(count_ones_and_zeros)):
        print("\nIn minefield, row values start at 1 and go to {0}.".format(minefield_rows))
        print("In minefield, column values start at 1 and go to {0}.".format(minefield_columns))
        print("\nThis is the user_interface_minefield:")
        for row in user_interface_minefield:
            print(row)

        # prompt user to guess row and column
        def get_player_input():
            guess_row = int(input("Guess row: "))
            guess_column = int(input("Guess column: "))
            return guess_row, guess_column

        guess_row, guess_column = get_player_input()

        def check_condition_guess(guess_index, minefield_edge_size):
            if isinstance(guess_row, int) is False:
                print("You didn't guess an integer")
                bad_guess_status = True
            elif guess_index < 1 or guess_index > minefield_edge_size:
                print("Your guess integer is out of range of 1-4")
                bad_guess_status = True
            else:
                bad_guess_status = False
            return bad_guess_status

        bad_guess_status = check_condition_guess(guess_row, minefield_rows)
        bad_guess_status = check_condition_guess(guess_column, minefield_columns)

        if bad_guess_status is True:
            print("Please make a more appropriate guess")
            continue
   
        print("Your guessed coordinate: ({0}, {1})".format(guess_row, guess_column))

        # create new variables for offsets of 1 less than guesses because we use zero-based numbering in Python
        user_guess_row_offset = guess_row - 1
        user_guess_column_offset = guess_column - 1

        # make reveal of board and notify user with text change
        if hidden_minefield[user_guess_row_offset][user_guess_column_offset] == 1:
            print("You guessed a 1 so you're nearby a mine.")
            user_interface_minefield[user_guess_row_offset][user_guess_column_offset] = '1'

        elif hidden_minefield[user_guess_row_offset][user_guess_column_offset] == 0:
            print("You guessed far from a mine. You're ok!")
            user_interface_minefield[user_guess_row_offset][user_guess_column_offset] = '0'

        else:
            print("You guessed the mine! You lose!\nHere's what the minefield looks like:")
            for row in hidden_minefield:
                print(row)
            break

        if guess_counter == 0:
            print("You have made {0} guess".format(guess_counter+1))
        else:
            print("You have made {0} guesses".format(guess_counter + 1))

play_minesweeper()
