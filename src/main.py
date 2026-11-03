
from crop_recommendation import recommend_crop
from soil_management import analyze_soil
from weather_advisory import weather_advisory


def main():
    while True:
        print("\n================================")
        print("       AGRINEXUS")
        print("  Smart Agriculture Platform")
        print("================================")
        print("1. Crop Recommendation")
        print("2. Soil Management")
        print("3. Weather Advisory")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            soil = input("Enter soil type (loamy/clay/sandy): ")
            season = input("Enter season (summer/winter/monsoon): ")

            crops = recommend_crop(soil, season)

            print("\nRecommended Crops:")
            for crop in crops:
                print("-", crop)

        elif choice == "2":
            try:
                ph = float(input("Enter soil pH: "))
                moisture = float(input("Enter soil moisture (%): "))
                analyze_soil(ph, moisture)
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                temp = float(input("Enter temperature (C): "))
                rain = float(input("Enter rainfall (mm): "))
                weather_advisory(temp, rain)
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "4":
            print("Thank you for using AgriNexus!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
