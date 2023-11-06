def tower_of_hanoi(n, source, auxiliary, destination, torre1, torre2, torre3):

    if n == 1:
        disk = torre1.pop()
        torre3.append(disk)
        return torre3

    tower_of_hanoi(n - 1, source, destination, auxiliary, torre1, torre3, torre2)

    disk = torre1.pop()
    torre3.append(disk)

    tower_of_hanoi(n - 1, auxiliary, source, destination, torre2, torre1, torre3)

torre1 = list(range(10, 0, -1))
torre2 = []
torre3 = []

tower_of_hanoi(10, 'A', 'B', 'C', torre1, torre2, torre3)

print("Torre final ", torre3)
