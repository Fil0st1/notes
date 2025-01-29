for n in range(2, 21):
    filename = f"table_{n}.txt"
    with open(filename, "w") as file:
        file.write(f"Multiplication table of {n}\n")
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n * i}\n")

