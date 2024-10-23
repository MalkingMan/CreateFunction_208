def konversi_temperatur(value, unit):
    if unit.upper() == 'C':
        # konversi Celsius to Fahrenheit
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        # Konversi Fahrenheit to Celsius
        return (value - 32) * 5/9
    else:
        raise ValueError("Angka tidak valid, gunakan 'C' untuk celcius dan 'F' untuk fahrenheit.")

celsius_value = 100
fahrenheit_value = konversi_temperatur(celsius_value, 'C')
print(f"{celsius_value}C is {fahrenheit_value}F")

fahrenheit_value = 77
celsius_value = konversi_temperatur(fahrenheit_value, 'F')
print(f"{fahrenheit_value}F is {celsius_value}C")
