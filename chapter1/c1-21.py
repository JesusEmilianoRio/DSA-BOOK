lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

for line in reversed(lines):
    print(line)