import json

f = "tasks.json"

try:
    tasks = json.load(open(f))
except:
    tasks = []

while True:
    print("\n1.Add  2.View  3.Done  4.Delete  5.Exit")
    c = input("Choice: ")

    if c == "1":
        t = input("Task: ")
        tasks.append({"task": t, "done": False})

    elif c == "2":
        for i, t in enumerate(tasks, 1):
            print(i, t["task"], "✓" if t["done"] else "-")

    elif c == "3":
        try:
            n = int(input("Task no: ")) - 1
            tasks[n]["done"] = True
        except:
            print("Invalid task.")

    elif c == "4":
        try:
            n = int(input("Task no: ")) - 1
            tasks.pop(n)
        except:
            print("Invalid task.")

    elif c == "5":
        print("Exiting...")

    else:
        print("Invalid choice.")

    json.dump(tasks, open(f, "w"), indent=4)