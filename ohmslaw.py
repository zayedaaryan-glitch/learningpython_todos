def calculate_ohms_law():
    print("--- EEE Milestone: Ohm's Law Calculator ---")
    try:
        # Ask user what they want to find
        choice = input("What do you want to calculate? (V, I, or R): ").upper()

        if choice == 'V':
            i = float(input("Enter Current (Amperes): "))
            r = float(input("Enter Resistance (Ohms): "))
            print(f"Voltage (V) = {i * r:.2f} Volts")
        elif choice == 'I':
            v = float(input("Enter Voltage (Volts): "))
            r = float(input("Enter Resistance (Ohms): "))
            print(f"Current (I) = {v / r:.2f} Amps")
        elif choice == 'R':
            v = float(input("Enter Voltage (Volts): "))
            i = float(input("Enter Current (Amperes): "))
            print(f"Resistance (R) = {v / i:.2f} Ohms")
        else:
            print("Invalid choice! Please enter V, I, or R.")

    except ValueError:
        print("Error: Please enter actual numbers, not text!")
    except ZeroDivisionError:
        print("Error: Current cannot be zero when calculating Resistance!")


calculate_ohms_law()