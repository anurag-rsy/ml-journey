def kinetic_energy(mass, velocity):
    """
    Calculate the kinetic energy of an object.

    Parameters:
    mass (float): Mass of the object in kilograms.
    velocity (float): Velocity of the object in meters per second.

    Returns:
    float: Kinetic energy in joules.
    """
    return 0.5 * mass * velocity ** 2

def main():
    try:
        mass = float(input("Enter mass in kilograms: "))
        velocity = float(input("Enter velocity in meters per second: "))
        ke = kinetic_energy(mass, velocity)
        print(f"The kinetic energy of the object is {ke} joules.")
    except ValueError:
        print("Please enter valid numbers for mass and velocity.")

if __name__ == "__main__":
            main()      