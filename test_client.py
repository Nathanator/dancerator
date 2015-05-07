import curses
import socket


ARROW_KEYS = {
    curses.KEY_UP: "up",
    curses.KEY_DOWN: "down",
    curses.KEY_LEFT: "left",
    curses.KEY_RIGHT: "right",
}
NOTE_KEYS = map(ord, "ABCDEFGabcdefg")
NUMBER_KEYS = map(ord, "3456")
IP_ADDRESS = "10.246.36.101"


def main(screen):
    octave = "3"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        while True:
            screen.addstr(0, 0, "Arrow keys for dance moves, A-G for notes, 3-6 to change octave. Current octave is {}. q to quit.".format(octave))
            char = screen.getch()
            if char in ARROW_KEYS:
                sock.sendto(ARROW_KEYS[char], (IP_ADDRESS, 5005))
            elif char in NOTE_KEYS:
                sock.sendto(chr(char).upper() + octave, (IP_ADDRESS, 5005))
            elif char in NUMBER_KEYS:
                octave = chr(char)
            elif char == ord("q"):
                return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    screen = curses.initscr()
    try:
        curses.noecho()
        curses.cbreak()
        screen.keypad(1)
        curses.curs_set(0)
        main(screen)
    finally:
        curses.curs_set(1)
        screen.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
