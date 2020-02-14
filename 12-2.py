from functools import reduce
from itertools import combinations

from gmpy2 import lcm

data = open('12.txt').read()
data = data.split('\n')

class Moon:
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.velocity = [0, 0, 0]

    def update_velocity(self, moon):
        for i in range(3):
            if self.position[i] < moon.position[i]:
                self.velocity[i] += 1
                moon.velocity[i] -= 1
            elif self.position[i] > moon.position[i]:
                self.velocity[i] -= 1
                moon.velocity[i] += 1

    def update_position(self):
        self.position = [a + b for a, b in zip(self.position, self.velocity)]

    def potential_energy(self):
        return sum(map(abs, self.position))

    def kinetic_energy(self):
        return sum(map(abs, self.velocity))

    def energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def __repr__(self):
        return f"pos=<x={self.position[0]}, y={self.position[1]}, z={self.position[2]}>, vel=<x={self.velocity[0]}, y={self.velocity[1]}, z={self.velocity[2]}>"

    def as_tuple(self, pos):
        return self.position[pos], self.velocity[pos]

step = 0
moons = [Moon(*[int(b[2:]) for b in a[1:-1].split(', ')]) for a in data]
seen_states = [{tuple(moon.as_tuple(i) for moon in moons)} for i in range(3)]
cycles = [None, None, None]

while any([cycle is None for cycle in cycles]):
    for moon1, moon2 in combinations(moons, r=2):
        moon1.update_velocity(moon2)
    for moon in moons:
        moon.update_position()
    step += 1
    for i in range(3):
        state = tuple(moon.as_tuple(i) for moon in moons)
        if state in seen_states[i] and cycles[i] is None:
            cycles[i] = step
            print(f'({len([c for c in cycles if c is not None])}/{len(cycles)}) Found cycle in {"xyz"[i]} axis.')
        else:
            seen_states[i].add(state)

final_step = reduce(lcm, cycles)
print(final_step)
