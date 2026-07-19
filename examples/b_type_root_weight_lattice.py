"""B_n root lattice and weight lattice examples in SageMath.

Run with:
    sage -python examples/b_type_root_weight_lattice.py
"""
from sage.all import CartanType, RootSystem


def main(n=3):
    cartan = CartanType(["B", n])
    ambient = RootSystem(cartan).ambient_space()
    alpha = ambient.simple_roots()
    omega = ambient.fundamental_weights()

    print(f"Cartan type: {cartan}")
    print(f"Rank: {n}")
    print("Cartan matrix:")
    print(cartan.cartan_matrix())
    print()

    print("Simple roots in the standard orthonormal basis e_i:")
    for i in range(1, n + 1):
        print(f"alpha_{i} = {alpha[i]}")
    print()

    print("Fundamental weights in the standard orthonormal basis e_i:")
    for i in range(1, n + 1):
        print(f"omega_{i} = {omega[i]}")
    print()

    print("Root lattice Q(B_n):")
    print("Q(B_n) = Z e_1 + ... + Z e_n")
    print("Check e_i = alpha_i + ... + alpha_n:")
    for i in range(1, n + 1):
        rhs = sum(alpha[j] for j in range(i, n + 1))
        print(f"e_{i} = {rhs}")
    print()

    print("Weight lattice P(B_n):")
    print("P(B_n) = Z^n + Z * 1/2(e_1 + ... + e_n)")
    print("Equivalently, coordinates are either all integers or all half-integers.")
    print(f"spin weight omega_{n} = {omega[n]}")
    print()

    print("Quotient:")
    print("P(B_n) / Q(B_n) ~= Z/2Z")
    print("The non-trivial coset is represented by omega_n.")


if __name__ == "__main__":
    main()
