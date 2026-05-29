# Assignment 5 - Q2 - AI Based Travel Planner

## Aim

The objective of this assignment is to design an AI based Travel Planner that reuses existing knowledge bases in the travel domain such as tourist places, food recommendations, wine/drink recommendations, personalized travel planning, and cost assessment.

The system generates travel recommendations based on user preferences and budget.

---

## Features of the Travel Planner

The AI Travel Planner includes the following features:

* Tourist place recommendation
* Food recommendation
* Wine / drink recommendation
* Personalized travel planning
* Hotel recommendation
* Transport selection
* Cost estimation
* Budget checking

---

## Knowledge Bases Used

The planner reuses different knowledge bases stored in the program.

## 1. Tourist Places Knowledge Base

This contains information about tourist attractions in different destinations.

Examples:

* Charminar
* Golconda Fort
* Salar Jung Museum
* Baga Beach
* Fort Aguada

---

## 2. Food Recommendation Knowledge Base

This contains food recommendations based on food preference.

Examples:

* Vegetarian food
* Non-vegetarian food

---

## 3. Wine / Drink Recommendation Knowledge Base

This provides drink recommendations based on the selected food preference.

Examples:

* Light white wine
* Red wine
* Fresh fruit juice
* Local mocktails

---

## 4. Hotel Cost Knowledge Base

This stores hotel costs based on hotel category.

Categories used:

* Budget
* Standard
* Luxury

---

## 5. Transport Cost Knowledge Base

This stores transport cost information.

Transport types used:

* Public transport
* Cab
* Private transport

---

## Working of the System

The user enters:

* Destination
* Number of days
* Budget
* Interest
* Food preference
* Hotel type
* Transport type

The planner then:

1. Recommends tourist places
2. Suggests food options
3. Suggests wine/drink options
4. Generates a day-wise travel plan
5. Calculates estimated trip cost
6. Checks whether the trip is within the given budget

---

## Sample Input

```text
Destination: Hyderabad
Days: 3
Budget: 15000
Interest: heritage
Food Preference: vegetarian
Hotel Type: budget
Transport Type: public
```

---

## Sample Output

```text
Generated Travel Plan
Destination: Hyderabad
Number of Days: 3

Recommended Places:
- Charminar
- Golconda Fort

Food Recommendations:
- Chutneys
- Santosh Dhaba
- Minerva Coffee Shop

Wine / Drink Recommendation:
- Light white wine or fresh fruit juice

Cost Assessment:
Total Estimated Cost: 9350

Budget Check:
The plan is within the given budget.
```

---

## Observation
The planner generates travel plans based on user preferences and budget using different knowledge bases. It also estimates the trip cost and checks whether the plan matches the user budget.

The system can be expanded further by adding more destinations, hotels, restaurants, and real-time APIs.

---

## Conclusion

The AI based Travel Planner was implemented successfully using existing knowledge bases for tourist places, food recommendations, wine/drink recommendations, hotel cost, and transport cost.

The system generates personalized travel plans and performs cost assessment based on user preferences and budget.
