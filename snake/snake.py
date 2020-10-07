import curses
import random
from time import sleep

def play():
    s = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    wh, ww = int(curses.LINES/2), int(curses.COLS/2)
    w = curses.newwin(wh, ww, 0, 0)
    w.border()
    w.keypad(1)
    w.nodelay(1)
    w.addstr(0, 5, " Score: 0 ", curses.A_REVERSE)
    w.timeout(100)

    snake = [(10, 10), (10, 11), (10, 12)]
    food = (int(wh/2), int(ww/2))

    # draw food
    w.addstr(food[0], food[1], "#", curses.color_pair(2))

    # draw snake
    w.addstr(snake[0][0], snake[0][1], "*", curses.color_pair(1))
    for pos in snake[1:]:
        w.addstr(pos[0], pos[1], "*")
    y, x = snake[-1]  # coordinate of head

    score = 0
    status = ""
    dir = curses.KEY_RIGHT
    c = -1
    while True:
        if dir == curses.KEY_RIGHT:
            x += 1
        elif dir == curses.KEY_LEFT:
            x -= 1
        elif dir == curses.KEY_UP:
            y -= 1
        elif dir == curses.KEY_DOWN:
            y += 1

        # if eat snake itself
        if (y, x) in snake:
            status = " Eat yourself! "
            break

        if y == 0 or y == (wh-1) or x == 0 or x == (ww-1):
            status = " Jump into the wall! "
            break

        # relocate snake
        w.addstr(y, x, "*", curses.color_pair(1))
        snake.append((y, x))
        w.addstr(snake[-2][0], snake[-2][1], "*", curses.color_pair(0))

        # eat food
        if (y, x) == food:
            while True:
                food = (random.randint(1, wh-2), random.randint(1, ww-2))
                if food not in snake:
                    break
            w.addstr(food[0], food[1], "#", curses.color_pair(2))
            score += 1
            w.addstr(0, 5, f" Score: {score} ", curses.A_REVERSE)
        else:
            w.addstr(snake[0][0], snake[0][1], " ", curses.color_pair(0))
            del snake[0]

        # get next character
        c = w.getch()
        if (c == curses.KEY_RIGHT and dir != curses.KEY_LEFT)  or \
           (c == curses.KEY_LEFT  and dir != curses.KEY_RIGHT) or \
           (c == curses.KEY_UP    and dir != curses.KEY_DOWN)  or \
           (c == curses.KEY_DOWN  and dir != curses.KEY_UP):
            dir = c

        if c == ord('x'): break
        if c == 'x': break

    w.addstr(10, 10, status, curses.A_REVERSE)
    w.refresh()
    sleep(2)
    w.addstr(12, 10, " Press any key to finish. ", curses.A_REVERSE)
    while w.getch() == -1:
        sleep(0.1)
        continue


    # terminate a curses application
    curses.echo()
    curses.nocbreak()
    s.keypad(False)
    curses.endwin()

if __name__ == '__main__':
    play()
    