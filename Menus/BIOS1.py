import curses

def draw_gui(stdscr):
    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Window text
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK) # Shadow
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLUE)   # Title

    # Get screen size
    height, width = stdscr.getmaxyx()

    # Set background color
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.clear()

    # Define window dimensions
    win_height = 7
    win_width = 40
    start_y = (height // 2) - (win_height // 2)
    start_x = (width // 2) - (win_width // 2)

    def draw_window():
        # Draw shadow
        for y in range(win_height):
            stdscr.addstr(start_y + y + 1, start_x + 2, " " * win_width, curses.color_pair(2))

        # Draw window border
        stdscr.addstr(start_y, start_x,     "┌" + "─" * (win_width - 2) + "┐", curses.color_pair(1))
        for y in range(1, win_height - 1):
            stdscr.addstr(start_y + y, start_x, "│" + " " * (win_width - 2) + "│", curses.color_pair(1))
        stdscr.addstr(start_y + win_height - 1, start_x, "└" + "─" * (win_width - 2) + "┘", curses.color_pair(1))

        # Add text inside the window
        text_lines = [
            "INFORMATION:",
            "BIOS VERSION 1.0",
            "MEMORY: FREE MB | USED: 15MB",
            "DISK OPERATING SYSTEM"
        ]
        
        for i, line in enumerate(text_lines):
            stdscr.addstr(start_y + 1 + i, start_x + 2, line, curses.color_pair(1))

        # Refresh screen
        stdscr.refresh()

    # Main loop to keep window open
    while True:
        draw_window()
        key = stdscr.getch()
        if key == ord('q'):
            break  # Exit on 'q'

# Run the GUI
curses.wrapper(draw_gui)
