from config import parse_args, the
from data import DATA
import eg

if __name__ == "__main__":
    args = parse_args()
    
    if args.type == "stats":
        stats_result = eg.stats()
        print(stats_result)

    elif args.type == "all":
        eg.all()
