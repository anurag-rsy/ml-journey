def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.

    Parameters:
    celsius (float): Temperature in degrees Celsius.

    Returns:
    float: Temperature in Kelvin.
    """
    kelvin = celsius + 273.15
    return kelvin

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} degrees Celsius is equal to {kelvin} Kelvin.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()