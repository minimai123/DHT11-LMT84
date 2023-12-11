class OhmsLawCalculator:
    def calculate_current(self, voltage, resistance):
        current = voltage / resistance
        print(f"Strøm: {current:.2f} A")
        return current

    def calculate_voltage(self, current, resistance):
        voltage = current * resistance
        print(f"Spænding: {voltage:.2f} V")
        return voltage

    def calculate_resistance(self, voltage, current):
        resistance = voltage / current
        print(f"Modstand: {resistance:.2f} ohm")
        return resistance

    def calculate_power(self, voltage, current):
        power = voltage * current
        print(f"Effekt: {power:.2f} W")
        return power

# Opret en instans af OhmsLawCalculator-klassen
ohm = OhmsLawCalculator()

# Test metoderne med forskellige argumenter
ohm.calculate_current(12, 4)  # Forventet resultat: Strøm: 3.00 A
ohm.calculate_voltage(3, 5)   # Forventet resultat: Spænding: 15.00 V
ohm.calculate_resistance(9, 3) # Forventet resultat: Modstand: 3.00 ohm
ohm.calculate_power(6, 2)      # Forventet resultat: Effekt: 12.00 W
