
def recommend_crop(soil_type, season):
    recommendations = {
        "loamy": {
            "summer": ["Maize", "Groundnut"],
            "winter": ["Wheat", "Peas"],
            "monsoon": ["Rice", "Millets"]
        },
        "clay": {
            "summer": ["Rice", "Sugarcane"],
            "winter": ["Wheat", "Mustard"],
            "monsoon": ["Rice", "Jute"]
        },
        "sandy": {
            "summer": ["Groundnut", "Millets"],
            "winter": ["Carrot", "Potato"],
            "monsoon": ["Pearl Millet"]
        }
    }

    soil_type = soil_type.lower()
    season = season.lower()

    if soil_type in recommendations and season in recommendations[soil_type]:
        return recommendations[soil_type][season]

    return ["No recommendation available"]


if __name__ == "__main__":
    soil = input("Enter soil type (loamy/clay/sandy): ")
    season = input("Enter season (summer/winter/monsoon): ")

    crops = recommend_crop(soil, season)

    print("\nRecommended crops:")
    for crop in crops:
        print("-", crop)
