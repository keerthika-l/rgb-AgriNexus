
from src.crop_recommendation import recommend_crop
from src.soil_management import analyze_soil
from src.weather_advisory import weather_advisory


def main():
    while True:
        print("\n===== AGRINEXUS =====")
        print("1. Crop Recommendation")
        print("2. Soil Management")
        print("3. Weather Advisory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                soil = input("Enter soil type (loamy/clay/sandy): ")
                season = input("Enter season (summer/winter/monsoon): ")

                crops = recommend_crop(soil, season)
                print("\nRecommended Crops:")
                for crop in crops:
                    print("-", crop)

            elif choice == "2":
                ph = float(input("Enter soil pH: "))
                moisture = float(input("Enter soil moisture (%): "))
                analyze_soil(ph, moisture)

            elif choice == "3":
                temperature = float(input("Enter temperature (C): "))
                rainfall = float(input("Enter rainfall (mm): "))
                weather_advisory(temperature, rainfall)

            elif choice == "4":
                print("Thank you for using AgriNexus!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
