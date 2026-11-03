

from crop_recommendation import recommend_crop
from soil_management import analyze_soil


def main():
    while True:
        print("\n================================")
        print("       🌱 AGRINEXUS")
        print("   Smart Agriculture Platform")
        print("================================")
        print("1. Crop Recommendation")
        print("2. Soil Management")
        print("3. Exit")

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
                ph = float(input("Enter soil pH (0-14): "))
                moisture = float(input("Enter soil moisture (0-100%): "))
                analyze_soil(ph, moisture)
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            print("Thank you for using AgriNexus!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
