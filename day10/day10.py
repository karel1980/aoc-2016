
from operator import mul

def main():
    f = BotFactory()
    f.process_instructions(open('input').readlines())

    values = f.outputs['0'].chips + f.outputs['1'].chips + f.outputs['2'].chips
    print "part 2:", reduce(mul, values)

class Bot:
    def __init__(self, id):
        self.id = id
        self.chips = []

    def handover(self, low_target, high_target):
        if len(self.chips) != 2:
            raise Error('bot %s can not hand over holding %s'%(self.id, self.chips))
        self.chips.sort()
        if self.chips == [ 17, 61 ]:
            print "part1: " + str(self)
        low_target.receive(self.chips[0])
        high_target.receive(self.chips[1])
        self.chips = []

    def receive(self, value):
        self.chips.append(value)

    def __str__(self):
        return "bot %s; chips=%s"%(self.id, self.chips)

class Output:
    def __init__(self, id):
        self.chips = []
        self.id = id

    def receive(self, value):
        self.chips.append(value)

    def __str__(self):
        return "output %s; chips = %s"%(self.id, self.chips)

class HandoverInstruction:
    def __init__(self, source, low_target, high_target):
        self.source = source
        self.low = low_target
        self.high = high_target

    def can_execute(self):
        return len(self.source.chips)==2

    def execute(self):
        self.source.handover(self.low, self.high)

    def __str__(self):
        return "handover from %s; low = %s; high = %s"%(self.source.id, self.low, self.high)

class SetValueInstruction:
    def __init__(self, target, value):
        self.target = target
        self.value = value

    def can_execute(self):
        return True

    def execute(self):
        self.target.receive(self.value)

    def __str__(self):
        return "set value %s to %s"%(self.value, self.target)

class BotFactory:
    def __init__(self):
        self.bots = {}
        self.outputs = {}

    def process_instructions(self, lines):
        instructions = self.parse_instructions(lines)

        while len(instructions) > 0:
            remaining = []
            for i in instructions:
                if i.can_execute():
                    i.execute()
                else:
                    remaining.append(i)

            instructions = remaining

    def parse_instructions(self, lines):
        result = []
        for l in lines:
            result.append(self.parse_instruction(l.strip()))

        return result

    def parse_instruction(self, line):
        parts = line.split(" ")
        if parts[0] == "bot":
            giver_id = parts[1]
            low_type = parts[5]
            low_id = parts[6]
            high_type = parts[10]
            high_id = parts[11]

            return HandoverInstruction(self.get_bot(giver_id), self.get_target(low_type, low_id), self.get_target(high_type, high_id))
        else:
            value = int(parts[1])
            bot_id = parts[5]
            return SetValueInstruction(self.get_bot(bot_id), value)

    def get_bot(self, id):
        return self.bots.setdefault(id, Bot(id))

    def get_output(self, id):
        return self.outputs.setdefault(id, Output(id))

    def get_target(self, t_type, t_id):
        if t_type == 'bot':
            return self.get_bot(t_id)
        if t_type == 'output':
            return self.get_output(t_id)

main()
