class Particle:
    def __init__(self, mass, velocity, charge):
        # your code here — store all 3 parameters as self attributes
        self.mass = mass
        self.velocity = velocity
        self.charge = charge

    def kinetic_energy(self):
        # your code here — return 0.5 * mass * velocity^2
        return 0.5 * self.mass * self.velocity ** 2


def main():
    try:
        mass = float(input("Enter mass in kilograms: "))
        velocity = float(input("Enter velocity in meters per second: "))
        charge = float(input("Enter charge in coulombs: "))
        particle = Particle(mass, velocity, charge)
        ke = particle.kinetic_energy()
        print(f"The kinetic energy of the particle is {ke} joules.")
    except ValueError:
        print("Please enter valid numbers for mass, velocity, and charge.")


if __name__ == "__main__":
    main()