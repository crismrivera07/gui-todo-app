# Recap of Section 11. We introduced a custom function `get_todos()` and
# called it from every branch that needed the current todos list.

FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH): #if you have default argument, don't have to pass it later.
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local: #returns a local file
        file_local = file_local.readlines()
    return file_local

def write_todos(todos_arg, filepath = FILEPATH): #writes the todos in a txt file, does not return nothing
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

#put this in a conditional block
if __name__ == " __main__":
    print("hello")
    print(get_todos())
    print(write_todos())
