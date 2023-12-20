from collections import deque

HIGH = 42
LOW = 13

class SignalCounter():
    def __init__(self, low=0, high=0):
        self.l = low
        self.h = high

    def count(self, signal):
        if signal == LOW:
            self.l += 1
        else:
            self.h += 1

    def pulse_product(self):
        return self.l * self.h


class Mod():
    def __init__(self, type: str, links: list):
        self.type = type
        self.links = links
        self.on = False
        self.received = dict()

    def __str__(self) -> str:
        return f'[{self.type}{self.name}->{self.links}]'

    def is_conj_high(self):
        return all(sig == HIGH for sig in self.received.values())
    
    def flip(self):
        self.on = not self.on

def process_input(input: str):
    mods = dict()
    mods['button'] = Mod('button', ['broadcaster'])
    for line in input.rstrip().split('\n'):
        type_name, links_str = line.split(' -> ')
        links_arr = links_str.split(', ')
        if line[0:2] == 'br':
            mods[type_name] = Mod('broadcaster', links_arr)
        else:
            mods[type_name[1:]] = Mod(type_name[0], links_arr)
    return mods

def process_signals(mods: dict[str, Mod], sc: SignalCounter):
    q = deque()
    q.append((LOW, 'broadcaster', 'button'))
    while q:
        signal, mod_key, old_mod_key = q.popleft()
        sc.count(signal)

        if mod_key not in mods.keys():
            continue

        mod = mods[mod_key]

        if mod.type == '%':
            if signal == HIGH:
                continue
            else:
                # signal is low
                if mod.on == True:
                    mod.on = False
                    for next_mod_key in mod.links:
                        q.append((LOW, next_mod_key, mod_key))
                else:
                    mod.on = True
                    for next_mod_key in mod.links:
                        q.append((HIGH, next_mod_key, mod_key))

        elif mod.type == '&':
            mod.received[old_mod_key] = signal
            if mod.is_conj_high():
                for next_mod_key in mod.links:
                    q.append((LOW, next_mod_key, mod_key))
            else:
                for next_mod_key in mod.links:
                    q.append((HIGH, next_mod_key, mod_key))

        elif mod.type == 'broadcaster':
            for next_mod_key in mod.links:
                q.append((signal, next_mod_key, mod_key))

def set_up_watched_modules(mods: dict[str, Mod]):
    for key, mod in mods.items():
        for link in mod.links:
            if link in mods.keys():
                if mods[link].type == '&':
                    mods[link].received[key] = False


def part1(input):
    mods = process_input(input)
    set_up_watched_modules(mods)
    sc = SignalCounter(0, 0)
    for _ in range(1000):
        process_signals(mods, sc)
    return sc.pulse_product()