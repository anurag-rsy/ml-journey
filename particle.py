import random


class Particle:
    def __init__(self, mass, velocity, charge):
        self.mass = mass
        self.velocity = velocity
        self.charge = charge

    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity**2

    def __repr__(self):
        return (
            f"Particle(mass={self.mass}, "
            f"velocity={self.velocity}, "
            f"charge={self.charge})"
        )

    def __eq__(self, other):
        if not isinstance(other, Particle):
            return False
        return (
            self.mass == other.mass
            and self.velocity == other.velocity
            and self.charge == other.charge
        )

    @property
    def momentum(self):
        return self.mass * self.velocity


def particle_generator(n):
    for _ in range(n):
        yield Particle(
            mass=random.uniform(0.1, 10),
            velocity=random.uniform(-50, 50),
            charge=random.choice([-1, 1])
        )


def main():
    try:
        for p in particle_generator(5):
            print(p)
            print(p.momentum)
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()