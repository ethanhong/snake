import sys
import snake

def main(args = None):
    if args is None:
        args = sys.argv[1:]
    return snake.play()

if __name__ == '__main__':
    sys.exit(main())
    