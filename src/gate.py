from config import parse_args, the
from data import DATA

if __name__ == "__main__":
    args = parse_args()

    if args.type == "stats":
        the = {
            "file": args.file,
            "cohen": args.cohen
        }
        data = DATA(the["file"])
        print("Data Cols: ", data.cols.y)
        result = data.stats(cols='y', fun="mid", ndivs=2, u={})
        print(result)