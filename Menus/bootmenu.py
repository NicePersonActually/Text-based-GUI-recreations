import curses

def draw_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Blue background
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Grey window
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)  # Highlighted option
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLACK)  # Shadow

    options = ["ANDROID", "FASTBOOT", "RECOVERY", "EXIT"]
    current_selection = 0

    while True:
        stdscr.clear()
        stdscr.bkgd(' ', curses.color_pair(1))  # Set blue background

        # Get terminal size
        max_y, max_x = stdscr.getmaxyx()

        # Define box dimensions
        box_width, box_height = 60, len(options) + 8  # Increased width
        title_height = 3  # Height of the title box
        total_height = box_height + title_height + 1  # Title + Menu + Space
        start_x = (max_x - box_width) // 2
        start_y = (max_y - total_height) // 2
        left_padding = 4  # Padding for left alignment of options

        # Draw shadow
        for i in range(title_height + box_height):
            stdscr.addstr(start_y + i + 1, start_x + box_width, "█", curses.color_pair(4))  # Right shadow
        stdscr.addstr(start_y + title_height + box_height, start_x + 1, "█" * (box_width - 1), curses.color_pair(4))  # Bottom shadow

        # Draw the title box (DUAL BOOT)
        stdscr.attron(curses.color_pair(2))  # Grey window
        stdscr.addstr(start_y, start_x, "╔" + "═" * (box_width - 2) + "╗")
        stdscr.addstr(start_y + 1, start_x, "║" + " " * (box_width - 2) + "║")
        stdscr.addstr(start_y + 1, start_x + (box_width - len(" DUAL BOOT ")) // 2, " DUAL BOOT ", curses.A_BOLD)
        stdscr.addstr(start_y + 2, start_x, "╚" + "═" * (box_width - 2) + "╝")
        stdscr.attroff(curses.color_pair(2))

        # Draw the main menu box (Gray Window)
        menu_start_y = start_y + title_height  # Position below title box
        stdscr.attron(curses.color_pair(2))  # Grey window
        stdscr.addstr(menu_start_y, start_x, "╔" + "═" * (box_width - 2) + "╗")
        for i in range(1, box_height - 1):
            stdscr.addstr(menu_start_y + i, start_x, "║" + " " * (box_width - 2) + "║")
        stdscr.addstr(menu_start_y + box_height - 1, start_x, "╚" + "═" * (box_width - 2) + "╝")
        stdscr.attroff(curses.color_pair(2))

        # Draw menu options (left-aligned inside the box)
        for idx, option in enumerate(options):
            y = menu_start_y + 2 + idx * 2  # Extra spacing
            x = start_x + left_padding  # Align options to the left
            if idx == current_selection:
                stdscr.attron(curses.color_pair(3))  # Highlighted option
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.color_pair(3))
            else:
                stdscr.addstr(y, x, option)

        # Instructions below the box, centered
        instruction_text = "HIGHLIGHT OPTIONS WITH ↑↓. PRESS ENTER TO SELECT."
        stdscr.addstr(menu_start_y + box_height + 1, (max_x - len(instruction_text)) // 2, instruction_text)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
            current_selection += 1
        elif key in [10, 13]:  # Enter key
            stdscr.clear()


curses.wrapper(draw_menu)
