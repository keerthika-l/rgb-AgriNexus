
def weather_advisory(temperature, rainfall):
    print("\n===== AGRINEXUS WEATHER ADVISORY =====")

    if temperature < -10 or temperature > 60:
        print("Invalid temperature.")
        return

    if rainfall < 0:
        print("Invalid rainfall value.")
        return

    if temperature > 35:
        print("High temperature detected.")
        print("Suggestion: Monitor crop water requirements.")

    elif temperature < 15:
        print("Low temperature detected.")
        print("Suggestion: Monitor crops for cold stress.")

    else:
        print("Temperature is moderate.")

    if rainfall > 100:
        print("Heavy rainfall detected.")
        print("Suggestion: Check field drainage.")

    elif rainfall < 10:
        print("Low rainfall detected.")
        print("Suggestion: Monitor irrigation requirements.")

    else:
        print("Rainfall is moderate.")

    print("====================================")


if __name__ == "__main__":
    try:
        temp = float(input("Enter temperature in Celsius: "))
        rain = float(input("Enter rainfall in mm: "))

        weather_advisory(temp, rain)

    except ValueError:
        print("Please enter valid numbers.")
