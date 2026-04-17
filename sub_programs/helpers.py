
#Prints out a list of strings in a box format and an optional title for the list
def box_items(items, title=None):
    items = [str(i) for i in items]

    width = max(len(i) for i in items)
    if title:
        width = max(width, len(title))

    horizontal = "   +" + "-" * (width + 2) + "+"

    print(f"   \n{horizontal}")

    if title:
        print(f"   | {title.ljust(width)} |")
        print(horizontal)

    for item in items:
        print(f"   | {item.ljust(width)} |")

    print(f"{horizontal}\n")