from config import parse_args, the
from num import NUM
from sym import SYM
from data import DATA
from row import ROW
from cols import COLS

if __name__ == "__main__":
    args = parse_args()

    if args.type == "stats":
        the = {
            "file": args.file,
            "cohen": args.cohen
        }
        data = DATA(the["file"])