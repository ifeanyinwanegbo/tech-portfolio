import numpy as np
from scipy.optimize import minimize


# -----------------------------
# Problem data (editable)
# -----------------------------
DEMAND = np.array([300.0, 200.0, 300.0])   # customers C1, C2, C3
CAPACITY_A = 500.0
CAPACITY_B = 700.0

# Shipping cost per unit
# rows: factory A,B ; cols: customers C1,C2,C3
SHIP_COST = np.array([
    [15.0, 20.0, 25.0],   # A -> C1,C2,C3
    [18.0, 22.0, 30.0],   # B -> C1,C2,C3
])


# -----------------------------
# Model
# Decision variables:
# x = [A->C1, A->C2, A->C3, B->C1, B->C2, B->C3]
# -----------------------------
def total_cost(x: np.ndarray) -> float:
    a1, a2, a3, b1, b2, b3 = x

    xA = a1 + a2 + a3
    xB = b1 + b2 + b3

    # Nonlinear production costs (example)
    prod_cost_A = 3.0 * xA**2 - 4.0 * xA + 20.0
    prod_cost_B = 1.5 * xB**2 + 2.0 * xB + 15.0

    # Linear shipping costs
    ship_cost = (
        15.0 * a1 + 20.0 * a2 + 25.0 * a3
        + 18.0 * b1 + 22.0 * b2 + 30.0 * b3
    )

    return float(prod_cost_A + prod_cost_B + ship_cost)


def solve_model():
    # A decent initial guess that already meets demand:
    # Send all demand from A first (up to its capacity) then rest from B
    a_guess = np.array([300.0, 200.0, 0.0])  # totals 500 (at capacity)
    b_guess = DEMAND - a_guess               # [0,0,300]
    x0 = np.concatenate([a_guess, b_guess])

    # Constraints: meet each customer demand exactly
    constraints = [
        {"type": "eq", "fun": lambda x: (x[0] + x[3]) - DEMAND[0]},  # C1
        {"type": "eq", "fun": lambda x: (x[1] + x[4]) - DEMAND[1]},  # C2
        {"type": "eq", "fun": lambda x: (x[2] + x[5]) - DEMAND[2]},  # C3
        # Capacity constraints (inequalities: <= 0 form or >= 0 form)
        {"type": "ineq", "fun": lambda x: CAPACITY_A - (x[0] + x[1] + x[2])},
        {"type": "ineq", "fun": lambda x: CAPACITY_B - (x[3] + x[4] + x[5])},
    ]

    # Bounds: non-negative shipments
    bounds = [(0.0, None)] * 6

    result = minimize(
        total_cost,
        x0,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
        options={"maxiter": 500, "ftol": 1e-9, "disp": False},
    )

    return result


def pretty_print_solution(result):
    if not result.success:
        print("❌ Optimization failed.")
        print("Reason:", result.message)
        return

    x = result.x
    a = x[:3]
    b = x[3:]

    print("✅ Optimization successful\n")

    print("Optimal shipment quantities (units):")
    print(f"  A → C1: {a[0]:.2f}")
    print(f"  A → C2: {a[1]:.2f}")
    print(f"  A → C3: {a[2]:.2f}")
    print(f"  B → C1: {b[0]:.2f}")
    print(f"  B → C2: {b[1]:.2f}")
    print(f"  B → C3: {b[2]:.2f}")

    xA = a.sum()
    xB = b.sum()

    print("\nFactory totals:")
    print(f"  Total from A: {xA:.2f} / {CAPACITY_A:.2f}")
    print(f"  Total from B: {xB:.2f} / {CAPACITY_B:.2f}")

    print("\nDemand check (A+B):")
    print(f"  C1: {(a[0]+b[0]):.2f} / {DEMAND[0]:.2f}")
    print(f"  C2: {(a[1]+b[1]):.2f} / {DEMAND[1]:.2f}")
    print(f"  C3: {(a[2]+b[2]):.2f} / {DEMAND[2]:.2f}")

    print(f"\nMinimum total cost: {result.fun:.2f}")


if __name__ == "__main__":
    res = solve_model()
    pretty_print_solution(res)
