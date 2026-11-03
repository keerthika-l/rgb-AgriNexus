
def analyze_soil(ph, moisture):
    print("\n===== AGRINEXUS SOIL ANALYSIS =====")

    if ph < 0 or ph > 14:
        print("Invalid pH value.")
        return

    if moisture < 0 or moisture > 100:
        print("Invalid moisture percentage.")
        return

    if ph < 5.5:
        print("Soil condition: Acidic")
        print("Suggestion: Get a soil test before considering lime.")

    elif ph > 7.5:
        print("Soil condition: Alkaline")
        print("Suggestion: Check soil nutrients and salinity.")

    else:
        print("Soil condition: Near-neutral")
        print("Suggestion: Maintain organic matter.")

    if moisture < 30:
        print("Moisture: Low")
        print("Suggestion: Check irrigation needs.")

    elif moisture > 70:
        print("Moisture: High")
        print("Suggestion: Check drainage.")

    else:
        print("Moisture: Moderate")

    print("==================================")


if __name__ == "__main__":
    ph = float(input("Enter soil pH (0-14): "))
    moisture = float(input("Enter soil moisture (0-100%): "))

    analyze_soil(ph, moisture)
