import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2300)

def process_line(elfs, elf, lines):
    if len(lines) <= 0:
        return
    else:
        line = lines.pop(0)
        if line == '':
            elfs.append(elf)
            return process_line(elfs, 0, lines)
        else:
            elf += int(line)
            return process_line(elfs, elf, lines)

def main():
    with open('day1_data.txt') as file:
        lines = [line.replace("\n", "") for line in file.readlines()]

    elfs = [0]
    elf = 0
    process_line(elfs, elf, lines)

    elfs = sorted(elfs)
    print(sum(elfs[-3:]))


main()
