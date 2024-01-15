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

    if args.type == "independent":
        independent_result = eg.independent()
        print(independent_result)

    elif args.type == "columns":
        columns_result = eg.columns()
        print(columns_result)

    elif args.type == "dependent":
        dependent_result = eg.dependent()
        print(dependent_result)


