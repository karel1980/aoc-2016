
class Cpu:
    def __init__(self):
        self.registers = dict(a=0, b=0, c=0, d=0)
        self.pos = 0

    def execute(self, instruction):
        parts = instruction.split(" ")

        if parts[0] == "cpy":
            if parts[1] in ["a","b","c","d"]:
                self.registers[parts[2]] = self.registers[parts[1]]
            else:
                self.registers[parts[2]] = int(parts[1])
            self.pos += 1

        if parts[0] == "inc":
            self.registers[parts[1]] += 1
            self.pos += 1

        if parts[0] == "dec":
            self.registers[parts[1]] -= 1
            self.pos += 1

        if parts[0] == "jnz":
            value = parts[1]
            if value in ["a","b","c","d"]:
                value = self.registers[value]
            else:
                value = int(value)
            if value == 0:
                self.pos += 1
            else:
                self.pos += int(parts[2])

def day12_part1():
    instructions = [ l.strip() for l in open('input') ]

    cpu = Cpu()
    while cpu.pos <= len(instructions):
        cpu.execute(instructions[cpu.pos])

    return cpu.registers

def day12_part2():
    instructions = [ l.strip() for l in open('input') ]

    cpu = Cpu()
    cpu.execute("cpy 1 c")
    cpu.pos = 0
    while cpu.pos < len(instructions):
        cpu.execute(instructions[cpu.pos])

    return cpu.registers

if __name__=="__main__":
    #print day12_part1()
    print day12_part2()

