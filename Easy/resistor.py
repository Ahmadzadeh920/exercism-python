# Define the resistor color code as a list
# The index of each color corresponds to its value
resistor_colors = [
    "black",  # 0
    "brown",  # 1
    "red",    # 2
    "orange", # 3
    "yellow", # 4
    "green",  # 5
    "blue",   # 6
    "violet", # 7
    "grey",   # 8
    "white"   # 9
]


def color_code(color:str)->int:
    code = resistor_colors.index(color.lower())
    return code

def list_colors()->list:
    """
    Returns the list of all resistor colors in order.
    """
    return resistor_colors


#Example Usage

if __name__ =="__main__":
    print(f"list colors is {list_colors()}")
    list_color = list_colors()
    for i in  list_color:
        print(f"the color of code {i} is {list_color.index(i)}")