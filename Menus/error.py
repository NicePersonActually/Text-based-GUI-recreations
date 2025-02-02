import curses

def draw_gui(stdscr):
    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Window text
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK) # Shadow
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLUE)   # Title
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)   # Highlighted text

    # Get screen size
    height, width = stdscr.getmaxyx()

    # Set background color
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.clear()

    # Define window dimensions
    win_height = 10
    win_width = 40
    start_y = (height // 2) - (win_height // 2)
    start_x = (width // 2) - (win_width // 2)

    def draw_window(selected_idx=0):
        # Draw shadow
        for y in range(win_height):
            stdscr.addstr(start_y + y + 1, start_x + 2, " " * win_width, curses.color_pair(2))

        # Draw window border using double-line characters
        stdscr.addstr(start_y, start_x,     chr(0x2554) + "─" * (win_width - 2) + chr(0x2557), curses.color_pair(1))  # Top border
        for y in range(1, win_height - 2):
            stdscr.addstr(start_y + y, start_x, chr(0x2551) + " " * (win_width - 2) + chr(0x2551), curses.color_pair(1))  # Side borders
        stdscr.addstr(start_y + win_height - 2, start_x, chr(0x255A) + "─" * (win_width - 2) + chr(0x255D), curses.color_pair(1))  # Bottom border

        # Add title above the window
        stdscr.addstr(start_y - 2, start_x, "STANDARD BOOTLOADER | VERSION: 1.0 | MEMORY: 70GB", curses.color_pair(3))

        # Add options inside the window
        options = ["CONSOLE", "EXIT"]
        for i, option in enumerate(options):
            if i == selected_idx:
                stdscr.addstr(start_y + 2 + i, start_x + 2, f"→ {option}", curses.color_pair(4))  # Highlighted option
            else:
                stdscr.addstr(start_y + 2 + i, start_x + 2, f"   {option}", curses.color_pair(1))  # Regular options

        # Add error message below the window
        stdscr.addstr(start_y + win_height, start_x, "ERROR: COULDN'T LOAD THE OPERATING SYSTEM. TRY TO:", curses.color_pair(1))
        suggestions = [
            "- REINSTALL OPERATING SYSTEM",
            "- RESTART THE COMPUTER"
        ]
        for i, suggestion in enumerate(suggestions):
            stdscr.addstr(start_y + win_height + 1 + i, start_x + 2, suggestion, curses.color_pair(1))

        # Refresh screen
        stdscr.refresh()

    # Main loop to keep window open
    selected_idx = 0
    while True:
        draw_window(selected_idx)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected_idx = (selected_idx - 1) % 2  # Loop through options
        elif key == curses.KEY_DOWN:
            selected_idx = (selected_idx + 1) % 2  # Loop through options
        elif key == 10:  # Enter key
            if selected_idx == 0:
                break  # Go to CONSOLE option
            elif selected_idx == 1:
                break  # Go to EXIT option
        elif key == ord('q'):
            break  # Exit on 'q'

# Run the GUI
curses.wrapper(draw_gui)
