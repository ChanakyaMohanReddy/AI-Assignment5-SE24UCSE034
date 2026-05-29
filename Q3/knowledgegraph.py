# simple knowledge graph demo

knowledge_graph = {
    "Delhi": {
        "has_places": ["India Gate", "Red Fort", "Qutub Minar"],
        "has_food": ["Chole Bhature", "Paratha"],
        "located_in": "India"
    },

    "Kerala": {
        "has_places": ["Munnar", "Alleppey", "Wayanad"],
        "has_food": ["Appam", "Kerala Sadya"],
        "located_in": "India"
    },

    "India Gate": {
        "category": "War Memorial",
        "located_in": "Delhi"
    },

    "Red Fort": {
        "category": "Historical Monument",
        "located_in": "Delhi"
    },

    "Munnar": {
        "category": "Hill Station",
        "located_in": "Kerala"
    }
}


def show_all_entities():
    print("Knowledge Graph Entities:\n")

    for entity in knowledge_graph:
        print("-", entity)


def show_relationships():
    print("\nKnowledge Graph Relationships:\n")

    for entity, details in knowledge_graph.items():
        for relation, value in details.items():

            if isinstance(value, list):
                for item in value:
                    print(entity, "->", relation, "->", item)

            else:
                print(entity, "->", relation, "->", value)


def get_places(city):
    if city in knowledge_graph and "has_places" in knowledge_graph[city]:
        return knowledge_graph[city]["has_places"]

    return []


def get_food(city):
    if city in knowledge_graph and "has_food" in knowledge_graph[city]:
        return knowledge_graph[city]["has_food"]

    return []


def get_category(place):
    if place in knowledge_graph and "category" in knowledge_graph[place]:
        return knowledge_graph[place]["category"]

    return "Category not found"


def main():
    show_all_entities()

    show_relationships()

    city = "Delhi"

    print("\nTourist Places in", city + ":")

    for place in get_places(city):
        print("-", place)

    print("\nFood Recommendations in", city + ":")

    for food in get_food(city):
        print("-", food)

    place = "India Gate"

    print("\nCategory of", place + ":")
    print(get_category(place))


if __name__ == "__main__":
    main()
