import curses
import time

def progress_bar(stdscr):
    """ Displays a progress bar indicating installation progress. """
    height, width = curses.LINES, curses.COLS
    win_width, win_height = 40, 5
    x, y = (width - win_width) // 2, (height - win_height) // 2

    stdscr.clear()
    stdscr.refresh()

    # Draw shadow
    for i in range(1, win_height + 1):
        stdscr.addstr(y + i, x + 2, " " * win_width, curses.color_pair(2))

    # Draw progress window
    stdscr.addstr(y, x, "╔" + "═" * (win_width - 2) + "╗", curses.color_pair(3))
    for i in range(1, win_height - 1):
        stdscr.addstr(y + i, x, "║" + " " * (win_width - 2) + "║", curses.color_pair(3))
    stdscr.addstr(y + win_height - 1, x, "╚" + "═" * (win_width - 2) + "╝", curses.color_pair(3))

    stdscr.addstr(y + 1, x + 2, "Installing...", curses.color_pair(4))

    for i in range(1, win_width - 4):
        time.sleep(0.1)
        stdscr.addstr(y + 2, x + 2, "█" * i, curses.color_pair(4))
        stdscr.refresh()

    time.sleep(1)  # Pause after installation completes
    stdscr.clear()
    stdscr.refresh()

def install_window(stdscr):
    """ Displays the install confirmation window with EXIT first and INSTALL second. """
    height, width = curses.LINES, curses.COLS
    win_width, win_height = 40, 7
    x, y = (width - win_width) // 2, (height - win_height) // 2

    options = ["INSTALL", "EXIT"]
    current_option = 0

    while True:
        stdscr.clear()

        # Draw shadow
        for i in range(1, win_height + 1):
            stdscr.addstr(y + i, x + 2, " " * win_width, curses.color_pair(2))

        # Draw window
        stdscr.addstr(y, x, "╔" + "═" * (win_width - 2) + "╗", curses.color_pair(3))
        for i in range(1, win_height - 1):
            stdscr.addstr(y + i, x, "║" + " " * (win_width - 2) + "║", curses.color_pair(3))
        stdscr.addstr(y + win_height - 1, x, "╚" + "═" * (win_width - 2) + "╝", curses.color_pair(3))

        stdscr.addstr(y + 1, x + 2, "SYSTEM INFORMATION", curses.color_pair(4))

        # Display options (EXIT first, then INSTALL)
        for idx, option in enumerate(options):
            attr = curses.A_REVERSE if idx == current_option else curses.A_NORMAL
            stdscr.addstr(y + 3 + idx, x + (win_width - len(option)) // 2, option, attr)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_option = (current_option - 1) % len(options)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(options)
        elif key == 10:  # Enter key
            if options[current_option] == "EXIT":
                progress_bar(stdscr)
                break
            elif options[current_option] == "INSTALL":
                break

def boot_manager(stdscr):
    """ Main boot manager menu. """
    curses.curs_set(0)
    curses.start_color()

    # Define color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Background
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)  # Shadow
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Window
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_WHITE)  # Title

    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.clear()

    options = ["BOOT FROM FLOPPY", "INSTALL SYSTEM TO FLOPPY", "EXIT"]
    current_option = 0
    box_width = max(len(option) for option in options) + 4
    title = "DUSA BOOT MANAGER"
    title_x = (curses.COLS - box_width) // 2
    menu_y = 6

    while True:
        stdscr.clear()

        # Draw title box
        stdscr.addstr(2, title_x, "╔" + "═" * (box_width - 2) + "╗", curses.color_pair(3))
        stdscr.addstr(3, title_x, "║" + title.center(box_width - 2) + "║", curses.color_pair(3))
        stdscr.addstr(4, title_x, "╚" + "═" * (box_width - 2) + "╝", curses.color_pair(3))

        # Draw options
        for idx, option in enumerate(options):
            attr = curses.A_REVERSE if idx == current_option else curses.A_NORMAL
            stdscr.addstr(menu_y + idx, (curses.COLS - len(option)) // 2, option, attr)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_option = (current_option - 1) % len(options)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(options)
        elif key == 10:  # Enter key
            if options[current_option] == "INSTALL SYSTEM TO FLOPPY":
                install_window(stdscr)
            elif options[current_option] == "EXIT":
                break

if __name__ == "__main__":
    curses.wrapper(boot_manager)
