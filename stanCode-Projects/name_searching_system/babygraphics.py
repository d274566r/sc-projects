"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space_for_each = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    x_coord = []
    for i in range(len(YEARS)):
        x_coord.append(GRAPH_MARGIN_SIZE+i*space_for_each)
    ans = x_coord[year_index]
    return ans


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW, font='times 12')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    space_at_y = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000
    for i in range(len(lookup_names)):  # loop over the names
        ranking = []  # creating the list for ranking data from name_data
        name_x_pos = []  # creating the list for saving x positions to draw the line
        color = COLORS[i % 4]
        for year in YEARS:  # acquiring ranking data from name_data
            if str(year) in name_data[lookup_names[i]]:
                ranking.append(name_data[lookup_names[i]][str(year)])
            else:  # for the names ranked lower than 1000
                ranking.append('*')
        for j in range(len(YEARS)):
            name_x_pos.append(get_x_coordinate(CANVAS_WIDTH, j))  # get the x position info
        for s in range(len(YEARS)):
            if ranking[s] is '*':  # for names out of 1000
                canvas.create_text(name_x_pos[s]+TEXT_DX, GRAPH_MARGIN_SIZE+space_at_y*(MAX_RANK-1),
                                   text=lookup_names[i]+ranking[s], anchor=tkinter.SW,
                                   fill=color, font='times 12')
                for k in range(len(YEARS)-1):
                    if ranking[k] is '*' and ranking[k+1] is not '*':
                        # if the name get into the top 1000 in the k+1 loop
                        canvas.create_line(name_x_pos[k], GRAPH_MARGIN_SIZE+space_at_y*(MAX_RANK-1),
                                           name_x_pos[k+1], GRAPH_MARGIN_SIZE+space_at_y*(int(ranking[k+1])-1),
                                           width=LINE_WIDTH, fill=color)
                    elif ranking[k] is '*' and ranking[k+1] is '*':
                        canvas.create_line(name_x_pos[k], GRAPH_MARGIN_SIZE+space_at_y*(MAX_RANK-1),
                                           name_x_pos[k+1],
                                           GRAPH_MARGIN_SIZE+space_at_y*(MAX_RANK-1),
                                           width=LINE_WIDTH, fill=color)
            else:  # for names in the top 1000
                canvas.create_text(name_x_pos[s]+TEXT_DX, GRAPH_MARGIN_SIZE+space_at_y*(int(ranking[s])-1),
                                   text=lookup_names[i]+ranking[s], anchor=tkinter.SW,
                                   fill=color, font='times 12')
                for k in range(len(YEARS)-1):
                    if ranking[k] is '*' and ranking[k+1] is not '*':
                        canvas.create_line(name_x_pos[k], GRAPH_MARGIN_SIZE + space_at_y * (MAX_RANK - 1),
                                           name_x_pos[k + 1],
                                           GRAPH_MARGIN_SIZE + space_at_y * (int(ranking[k + 1]) - 1),
                                           width=LINE_WIDTH, fill=color)
                    elif ranking[k] is not '*':
                        canvas.create_line(name_x_pos[k], GRAPH_MARGIN_SIZE+space_at_y*(int(ranking[k])-1),
                                           name_x_pos[k+1], GRAPH_MARGIN_SIZE+space_at_y*(int(ranking[k+1])-1),
                                           width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
