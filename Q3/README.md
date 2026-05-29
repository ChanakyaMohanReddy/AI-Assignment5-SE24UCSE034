# Assignment 5 - Q3 - Knowledge Graphs and Tools Used to Build Them

Knowledge Graphs (KGs) are a method of representing information in a connected graph structure. They organize data using entities, relationships, and attributes so that machines can understand how different concepts are related to each other.

In a Knowledge Graph:

* Entities represent real-world objects such as cities, tourist places, people, restaurants, or products.
* Relationships connect these entities together.
* Attributes store additional information about the entities.

Knowledge Graphs help in linking related information instead of storing data separately like traditional databases. This makes searching, recommendation, and reasoning easier in AI systems.

Knowledge Graphs are widely used in AI systems, recommendation systems, search engines, and chatbots.


---


In this assignment, a simple Knowledge Graph was implemented using Python dictionaries. Different cities, tourist places, and food items were connected using relationships such as has_places, has_food, located_in, and category. The program also performs simple queries to retrieve connected information from the graph.
Example used in this assignment:

The Knowledge Graph created in this program stores information about cities, tourist places, and food items. Cities like Delhi and Kerala are connected to tourist attractions and food recommendations using relationships.

For example:

* Delhi is connected to India Gate, Red Fort, and Qutub Minar using the relationship has_places.
* Kerala is connected to Munnar, Alleppey, and Wayanad.
* Food items such as Chole Bhature, Paratha, Appam, and Kerala Sadya are connected to their respective cities.
* Tourist places are connected with categories such as Historical Monument, Hill Station, and Beach.
The program also performs simple queries such as:

retrieving tourist places of a city,
retrieving food recommendations,
retrieving the category of a place.

This shows how related information can be connected and queried using a simple Knowledge Graph.

---



Some commonly used tools for building Knowledge Graphs are Neo4j, Protégé, GraphDB, Apache Jena, RDF, SPARQL, and NetworkX.

* Neo4j is a graph database used to store nodes and relationships.
* Protégé is used for ontology creation and semantic modeling.
* GraphDB is used for storing RDF and semantic graph data.
* Apache Jena is a framework used for semantic web and linked data applications.
* RDF is used to represent graph data in subject-predicate-object format.
* SPARQL is a query language used for querying RDF data.
* NetworkX is a Python library used for graph creation and analysis.

---

### Sample Output

Knowledge Graph Entities:

- Delhi
- Kerala
- India Gate
- Red Fort
- Munnar

```text
Knowledge Graph Relationships:

Delhi -> has_places -> India Gate
Delhi -> has_places -> Red Fort
Delhi -> has_places -> Qutub Minar
Delhi -> has_food -> Chole Bhature
Delhi -> has_food -> Paratha

Kerala -> has_places -> Munnar
Kerala -> has_places -> Alleppey
Kerala -> has_places -> Wayanad
Kerala -> has_food -> Appam
Kerala -> has_food -> Kerala Sadya
```

Tourist Places in Delhi:
- India Gate
- Red Fort
- Qutub Minar

Food Recommendations in Delhi:
- Chole Bhature
- Paratha

Category of India Gate:
War Memorial
