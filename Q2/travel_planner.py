# AI based travel planner

places_kb = {
    "Hyderabad": [
        {"name": "Charminar", "type": "heritage", "cost": 100},
        {"name": "Golconda Fort", "type": "heritage", "cost": 150},
        {"name": "Salar Jung Museum", "type": "museum", "cost": 100},
        {"name": "Ramoji Film City", "type": "entertainment", "cost": 1200},
        {"name": "Hussain Sagar", "type": "nature", "cost": 200},
        {"name": "Laad Bazaar", "type": "shopping", "cost": 500}
    ],
    "Goa": [
        {"name": "Baga Beach", "type": "nature", "cost": 300},
        {"name": "Fort Aguada", "type": "heritage", "cost": 100},
        {"name": "Dudhsagar Falls", "type": "nature", "cost": 800},
        {"name": "Anjuna Market", "type": "shopping", "cost": 500},
        {"name": "Old Goa Church", "type": "heritage", "cost": 100}
    ]
}

food_kb = {
    "Hyderabad": {
        "vegetarian": ["Chutneys", "Santosh Dhaba", "Minerva Coffee Shop"],
        "non-vegetarian": ["Paradise Biryani", "Shah Ghouse", "Bawarchi"]
    },
    "Goa": {
        "vegetarian": ["Bean Me Up", "Navtara", "Saraya Cafe"],
        "non-vegetarian": ["Ritz Classic", "Fisherman's Wharf", "Britto's"]
    }
}

wine_kb = {
    "vegetarian": "Light white wine or fresh fruit juice",
    "non-vegetarian": "Red wine or local mocktail"
}

hotel_cost_kb = {
    "budget": 1500,
    "standard": 3000,
    "luxury": 6000
}

transport_cost_kb = {
    "public": 500,
    "cab": 1500,
    "private": 2500
}


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def get_user_details():
    print("AI Based Travel Planner")

    destination = input("Enter destination (Hyderabad/Goa): ").strip().title()
    days = get_number("Enter number of days: ")
    budget = get_number("Enter total budget: ")

    interest = input(
        "Enter interest (heritage/nature/museum/shopping/entertainment): "
    ).strip().lower()

    food_type = input(
        "Food preference (vegetarian/non-vegetarian): "
    ).strip().lower()

    hotel_type = input(
        "Hotel type (budget/standard/luxury): "
    ).strip().lower()

    transport_type = input(
        "Transport type (public/cab/private): "
    ).strip().lower()

    return destination, days, budget, interest, food_type, hotel_type, transport_type


def recommend_places(destination, interest):
    selected_places = []

    if destination not in places_kb:
        return selected_places

    for place in places_kb[destination]:
        if place["type"] == interest:
            selected_places.append(place)

    if not selected_places:
        selected_places = places_kb[destination][:3]

    return selected_places


def recommend_food(destination, food_type):
    if destination in food_kb and food_type in food_kb[destination]:
        return food_kb[destination][food_type]

    return ["Local food options available"]


def recommend_wine_or_drink(food_type):
    return wine_kb.get(food_type, "Local drink recommendation available")


def calculate_cost(days, selected_places, hotel_type, transport_type):
    hotel_cost = hotel_cost_kb.get(hotel_type, 1500) * days
    transport_cost = transport_cost_kb.get(transport_type, 500) * days
    food_cost = 700 * days
    place_cost = sum(place["cost"] for place in selected_places)
    extra_cost = 1000

    total = hotel_cost + transport_cost + food_cost + place_cost + extra_cost

    return hotel_cost, transport_cost, food_cost, place_cost, extra_cost, total


def generate_plan(days, places):
    plan = {}
    place_index = 0

    for day in range(1, days + 1):
        day_plan = []

        for _ in range(2):
            if place_index < len(places):
                day_plan.append(places[place_index]["name"])
                place_index += 1

        if not day_plan:
            day_plan.append("Relax and explore local area")

        plan["Day " + str(day)] = day_plan

    return plan


def show_plan(destination, days, budget, places, food_options, drink, cost_details, plan):
    hotel_cost, transport_cost, food_cost, place_cost, extra_cost, total = cost_details

    print("\nGenerated Travel Plan")
    print("Destination:", destination)
    print("Number of Days:", days)

    print("\nRecommended Places:")
    for place in places:
        print("-", place["name"], "(" + place["type"] + ")")

    print("\nFood Recommendations:")
    for food in food_options:
        print("-", food)

    print("\nWine / Drink Recommendation:")
    print("-", drink)

    print("\nDay-wise Plan:")
    for day, activities in plan.items():
        print(day + ":")
        for activity in activities:
            print("  -", activity)

    print("\nCost Assessment:")
    print("Hotel Cost:", hotel_cost)
    print("Transport Cost:", transport_cost)
    print("Food Cost:", food_cost)
    print("Place Visit Cost:", place_cost)
    print("Extra Cost:", extra_cost)
    print("Total Estimated Cost:", total)

    print("\nBudget Check:")
    if total <= budget:
        print("The plan is within the given budget.")
    else:
        print("The plan exceeds the budget. Choose budget hotel or public transport.")


def main():
    destination, days, budget, interest, food_type, hotel_type, transport_type = get_user_details()

    if destination not in places_kb:
        print("Sorry, destination not available in knowledge base.")
        return

    places = recommend_places(destination, interest)
    food_options = recommend_food(destination, food_type)
    drink = recommend_wine_or_drink(food_type)
    cost_details = calculate_cost(days, places, hotel_type, transport_type)
    plan = generate_plan(days, places)

    show_plan(destination, days, budget, places, food_options, drink, cost_details, plan)


if __name__ == "__main__":
    main()
