def allowed_to_attend_python_class(name, password):
    if name == "Mani":
        if password == "Yes":
            print("You are allowed to enter")
        else:
            print("Not allowed")
    else:
        print("wrong name")

allowed_to_attend_python_class("Mani", "Yes")
allowed_to_attend_python_class("Mani", "No")
allowed_to_attend_python_class("Balan", "Yes")