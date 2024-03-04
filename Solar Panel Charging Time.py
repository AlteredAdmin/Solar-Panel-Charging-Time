def calculate_charging_time(solar_panel_power, battery_voltage, battery_capacity, efficiency):
    """
    Calculate the time required to charge a battery using a solar panel.

    Parameters:
    solar_panel_power (float): Power of the solar panel in watts.
    battery_voltage (float): Voltage of the battery in volts.
    battery_capacity (float): Capacity of the battery in ampere-hours (Ah).
    efficiency (float): Efficiency of the system (percentage, e.g., 85 for 85%).

    Returns:
    float: Time required to charge the battery in hours.
    """
    # Convert the solar panel power to current
    solar_panel_current = solar_panel_power / battery_voltage

    # Adjust for efficiency losses
    effective_charging_current = solar_panel_current * (efficiency / 100)

    # Calculate charging time
    charging_time = battery_capacity / effective_charging_current

    return charging_time

# Example usage
if __name__ == "__main__":
    # Input parameters
    solar_panel_power = float(input("Enter solar panel power (in watts): "))
    battery_voltage = float(input("Enter battery voltage (in volts): "))
    battery_capacity = float(input("Enter battery capacity (in Ah): "))
    efficiency = float(input("Enter system efficiency (in %): "))

    # Calculate and display the charging time
    charging_time = calculate_charging_time(solar_panel_power, battery_voltage, battery_capacity, efficiency)
    print(f"The estimated charging time is {charging_time:.2f} hours.")
