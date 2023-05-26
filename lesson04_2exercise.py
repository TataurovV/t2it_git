#Написати програму, яка виводить сама себе
filename = "lesson04_2exercise.py"
with open(filename, "w") as file:
    with open(__file__, "r") as current_file:
        file.write(current_file.read())
