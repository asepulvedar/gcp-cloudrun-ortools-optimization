# Optimization Model for Diet Problem with Ortools, Deployed in Flask
"""The Stigler diet problem.
Link: https://developers.google.com/optimization/lp/stigler_diet

A description of the problem can be found here:
https://en.wikipedia.org/wiki/Stigler_diet.
"""
import pandas as pd
import os
from ortools.linear_solver import pywraplp
from data import data # Food Nutrients Data

from flask import Flask, request, jsonify

app = Flask(__name__)

# Optimization Model for Diet

@app.route('/nutrients', methods=['POST','GET'])
def solve():
    nutrients = request.json
    calories = nutrients['calories']
    protein = nutrients['protein']
    calcium = nutrients['calcium']
    iron = nutrients['iron']
    vitamin_a = nutrients['vitamin_a']
    vitamin_b1 = nutrients['vitamin_b1']
    vitamin_b2 = nutrients['vitamin_b2']
    niacin = nutrients['niacin']
    vitamin_c = nutrients['vitamin_c']

    print(nutrients)
    """Entry point of the program.
    nunutrients_parameters:
    Example:
    nutrients = [
        ["Calories (kcal)", 3],
        ["Protein (g)", 70],
        ["Calcium (g)", 0.8],
        ["Iron (mg)", 12],
        ["Vitamin A (KIU)", 5],
        ["Vitamin B1 (mg)", 1.8],
        ["Vitamin B2 (mg)", 2.7],
        ["Niacin (mg)", 18],
        ["Vitamin C (mg)", 75],]
    """

    nutrients = [
        ["Calories (kcal)", calories],
        ["Protein (g)", protein],
        ["Calcium (g)",calcium],
        ["Iron (mg)", iron],
        ["Vitamin A (KIU)", vitamin_a],
        ["Vitamin B1 (mg)", vitamin_b1],
        ["Vitamin B2 (mg)", vitamin_b2],
        ["Niacin (mg)", niacin],
        ["Vitamin C (mg)", vitamin_c],
    ]

    # Instantiate the data problem.
    # Nutrient minimums.

    # Instantiate a Glop solver and naming it.
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

    # Declare an array to hold our variables.
    foods = [solver.NumVar(0.0, solver.infinity(), item[0]) for item in data]

    print("Number of variables =", solver.NumVariables())

    # Create the constraints, one per nutrient.
    constraints = []
    for i, nutrient in enumerate(nutrients):
        constraints.append(solver.Constraint(nutrient[1], solver.infinity()))
        for j, item in enumerate(data):
            constraints[i].SetCoefficient(foods[j], item[i + 3])

    print("Number of constraints =", solver.NumConstraints())

    # Objective function: Minimize the sum of (price-normalized) foods.
    objective = solver.Objective()
    for food in foods:
        objective.SetCoefficient(food, 1)
    objective.SetMinimization()

    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    # Check that the problem has an optimal solution.
    if status != solver.OPTIMAL:
        print("The problem does not have an optimal solution!")
        if status == solver.FEASIBLE:
            print("A potentially suboptimal solution was found.")
        else:
            print("The solver could not solve the problem.")
            exit(1)

    # Display the amounts (in dollars) to purchase of each food.
    nutrients_result = [0] * len(nutrients)
    food_results = []
    print("\nAnnual Foods:")
    for i, food in enumerate(foods):
        if food.solution_value() > 0.0:
            food_cost = 365.0 * food.solution_value()
            print("{}: ${}".format(data[i][0], food_cost))
            food_results.append([data[i][0], food_cost])
            for j, _ in enumerate(nutrients):
                nutrients_result[j] += data[i][j + 3] * food.solution_value()
    print("\nOptimal annual price: ${:.4f}".format(365.0 * objective.Value()))

    print("\nNutrients per day:")
    nutrient_results = []
    for i, nutrient in enumerate(nutrients):
        nutrient_amount = nutrients_result[i]
        print(
            "{}: {:.2f} (min {})".format(nutrient[0], nutrient_amount, nutrient[1])
        )
        nutrient_results.append([nutrient[0], nutrient_amount, nutrient[1]])

    print("\nAdvanced usage:")
    print(f"Problem solved in {solver.wall_time():d} milliseconds")
    print(f"Problem solved in {solver.iterations():d} iterations")

    # Return the nutrients and food data in a pandas DataFrame.
    df_nutrients = pd.DataFrame(nutrient_results, columns=["Nutrient", "Amount", "Minimum"])
    df_foods = pd.DataFrame(food_results, columns=["Food", "Annual Cost"])

    print(df_nutrients)
    print(df_foods)

    # Convert dataframes to JSON
    nutrients_json = df_nutrients.to_json(orient='records')
    foods_json = df_foods.to_json(orient='records')

    return jsonify({
        'nutrients': nutrients_json,
        'foods': foods_json
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
