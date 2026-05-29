# Bayesian network example for medical diagnosis

try:
    from pgmpy.models import DiscreteBayesianNetwork as BayesianNetwork
except ImportError:
    from pgmpy.models import BayesianNetwork

from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# building the bayesian network
def build_model():
    model = BayesianNetwork([
        ("Flu", "Fever"),
        ("Flu", "Cough"),
        ("Covid", "Fever"),
        ("Covid", "Cough"),
        ("Covid", "BreathingProblem")
    ])

    cpd_flu = TabularCPD(
        variable="Flu",
        variable_card=2,
        values=[
            [0.70],
            [0.30]
        ]
    )

    cpd_covid = TabularCPD(
        variable="Covid",
        variable_card=2,
        values=[
            [0.85],
            [0.15]
        ]
    )

    cpd_fever = TabularCPD(
        variable="Fever",
        variable_card=2,
        values=[
            [0.95, 0.40, 0.30, 0.10],
            [0.05, 0.60, 0.70, 0.90]
        ],
        evidence=["Flu", "Covid"],
        evidence_card=[2, 2]
    )

    cpd_cough = TabularCPD(
        variable="Cough",
        variable_card=2,
        values=[
            [0.90, 0.35, 0.40, 0.15],
            [0.10, 0.65, 0.60, 0.85]
        ],
        evidence=["Flu", "Covid"],
        evidence_card=[2, 2]
    )

    cpd_breathing = TabularCPD(
        variable="BreathingProblem",
        variable_card=2,
        values=[
            [0.90, 0.30],
            [0.10, 0.70]
        ],
        evidence=["Covid"],
        evidence_card=[2]
    )

    model.add_cpds(
        cpd_flu,
        cpd_covid,
        cpd_fever,
        cpd_cough,
        cpd_breathing
    )

    return model


# printing probability result
def print_probability(result, variable_name):
    print("\nProbability of", variable_name)
    print("No :", round(result.values[0], 4))
    print("Yes:", round(result.values[1], 4))


def main():
    model = build_model()

    if model.check_model():
        print("Bayesian Network model created successfully.")
    else:
        print("Model has some error.")
        return

    inference = VariableElimination(model)

    print("\nNodes in the network:")
    print(list(model.nodes()))

    print("\nEdges in the network:")
    print(list(model.edges()))

    # test case 1
    result1 = inference.query(
        variables=["Flu"],
        evidence={"Fever": 1, "Cough": 1}
    )
    print_probability(result1, "Flu given Fever and Cough")

    # test case 2
    result2 = inference.query(
        variables=["Covid"],
        evidence={
            "Fever": 1,
            "Cough": 1,
            "BreathingProblem": 1
        }
    )
    print_probability(
        result2,
        "Covid given Fever, Cough and Breathing Problem"
    )

    # test case 3
    result3 = inference.query(
        variables=["Covid"],
        evidence={"BreathingProblem": 1}
    )
    print_probability(result3, "Covid given Breathing Problem")

    # test case 4
    result4 = inference.query(
        variables=["Flu"],
        evidence={"Fever": 1}
    )
    print_probability(result4, "Flu given Fever")

    # test case 5
    result5 = inference.query(
        variables=["Covid"],
        evidence={"Fever": 1}
    )
    print_probability(result5, "Covid given Fever")

    # test case 6
    result6 = inference.query(
        variables=["Cough"],
        evidence={"Covid": 1}
    )
    print_probability(result6, "Cough given Covid")


if __name__ == "__main__":
    main()
