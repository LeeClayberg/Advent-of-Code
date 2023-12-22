
class BaseModule:
    def __init__(self, mod_id, connected, system):
        self.mod_id = mod_id
        self.connected = connected
        self.system = system

    def process(self, is_high, sender):
        return [(connection, is_high, self.mod_id) for connection in self.connected]

class FlipFlop(BaseModule):
    def __init__(self, mod_id, connected, system):
        super().__init__(mod_id, connected, system)
        self.on = False

    def process(self, is_high, sender):
        if not is_high:
            self.on = not self.on
            return [(connection, self.on, self.mod_id) for connection in self.connected]
        return []

class Conjunction(BaseModule):
    def __init__(self, mod_id, connected, system):
        super().__init__(mod_id, connected, system)
        self.recent = {}

    def add_senders(self, senders):
        for sender in senders:
            self.recent[sender] = False

    def process(self, is_high, sender):
        self.recent[sender] = is_high
        new_is_high = not all(self.recent.values())
        return [(connection, new_is_high, self.mod_id) for connection in self.connected]


with open("files/day20.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    full_system = {}
    conjunctions = []
    sender_lists = {}

    for line in lines:
        key, connected_modules = line.split(' -> ')
        connected_modules = connected_modules.split(', ')

        if key == 'broadcaster':
            full_system[key] = BaseModule(key, connected_modules, full_system)
        else:
            mod_t, key = key[0], key[1:]
            if mod_t == '%':
                full_system[key] = FlipFlop(key, connected_modules, full_system)
            elif mod_t == '&':
                full_system[key] = Conjunction(key, connected_modules, full_system)
                conjunctions.append(full_system[key])

        for m_key in connected_modules:
            if m_key not in sender_lists:
                sender_lists[m_key] = set()
            sender_lists[m_key].add(key)

    for conjunction in conjunctions:
        conjunction.add_senders(sender_lists[conjunction.mod_id])

    high_pulses, low_pulses = 0, 0
    press = 0
    while True:
        press += 1
        queue = [('broadcaster', False, None)]
        while len(queue) > 0:
            curr_key, is_high_pulse, from_key = queue.pop(0)
            if curr_key == 'rx' and not is_high_pulse:
                print(press)
                exit()
            if curr_key in full_system:
                next_keys = full_system[curr_key].process(is_high_pulse, from_key)
                queue.extend(next_keys)
            high_pulses += 1 if is_high_pulse else 0
            low_pulses += 0 if is_high_pulse else 1