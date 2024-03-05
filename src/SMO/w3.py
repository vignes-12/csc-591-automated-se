from config import parse_args, the
from data import DATA
import eg
from sym import SYM
from num import NUM

def task_1(dataset):
    
        # Calculate the maximum length of class names
    max_class_length = max(len(klassCategory) for klassCategory in dataset.cols.klass.has)

    # Print the header
    print(f"{dataset.cols.klass.txt:>{max_class_length + 1}}")
    print("=" * (max_class_length + 1))

    # Define the maximum characters per line
    max_characters_per_line = 120

    # Print category headers with gaps in chunks
    class_categories = list(dataset.cols.klass.has.keys())
    for i in range(0, len(class_categories), max_characters_per_line // (max_class_length + 2)):
        chunk = class_categories[i:i + max_characters_per_line // (max_class_length + 2)]
        print("".join(f"{klassCategory:>{max_class_length}}  " for klassCategory in chunk))
    print("\n")

    # Print percentages for each category in chunks
    for i in range(0, len(class_categories), max_characters_per_line // (max_class_length + 2)):
        chunk = class_categories[i:i + max_characters_per_line // (max_class_length + 2)]
        for klassCategory in chunk:
            percentage = round(dataset.cols.klass.has[klassCategory] / len(dataset.rows) * 100, 2)
            print(f"{percentage:>{max_class_length - 1}.2f}%", end="")
        print("\n")
        
eg.km()


