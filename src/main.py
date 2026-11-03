
def main():
    print("=" * 40)
    print("       🌱 WELCOME TO AGRINEXUS")
    print("    Smart Agriculture Platform")
    print("=" * 40)

    print("\n1. Crop Information")
    print("2. Smart Farming")
    print("3. Soil Management")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("Crop Information - Coming Soon!")
    elif choice == "2":
        print("Smart Farming - Coming Soon!")
    elif choice == "3":
        print("Soil Management - Coming Soon!")
    elif choice == "4":
        print("Thank you for using AgriNexus!")
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
