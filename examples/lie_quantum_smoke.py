from sage.all import *

def section(name):
    print(f"\n## {name}")

def show(label, value):
    print(f"{label}: {value}")

def run(name, fn):
    section(name)
    try:
        fn()
        print(f"STATUS: OK [{name}]")
    except Exception as e:
        print(f"STATUS: FAIL [{name}] {type(e).__name__}: {e}")


def cartan_roots():
    ct = CartanType(['A', 2])
    show('CartanType', ct)
    show('rank', ct.rank())
    show('index_set', ct.index_set())
    show('cartan_matrix', ct.cartan_matrix())
    R = RootSystem(ct)
    Q = R.root_lattice()
    alpha = Q.simple_roots()
    show('root_lattice', Q)
    show('simple_roots', alpha)
    show('alpha1+alpha2', alpha[1] + alpha[2])
    WL = R.weight_lattice()
    Lambda = WL.fundamental_weights()
    show('weight_lattice', WL)
    show('fundamental_weights', Lambda)
    show('alpha1 in fundamental weights basis', WL.simple_roots()[1])


def weyl_group():
    W = WeylGroup(['A', 2], prefix='s')
    s = W.simple_reflections()
    show('W', W)
    show('simple_reflections', s)
    show('s1^2', s[1] * s[1])
    show('s2^2', s[2] * s[2])
    show('braid s1 s2 s1', s[1] * s[2] * s[1])
    show('braid s2 s1 s2', s[2] * s[1] * s[2])
    show('braid equality', s[1] * s[2] * s[1] == s[2] * s[1] * s[2])
    show('order', W.order())
    show('long_element', W.long_element())


def weyl_characters():
    A2 = WeylCharacterRing('A2')
    # Sage's A2 WeylCharacterRing uses dominant weights as length-3 partitions.
    # (1,0,0) and (1,1,0) are the two 3-dimensional fundamental representations.
    V = A2(1, 0, 0)
    W = A2(1, 1, 0)
    show('A2 ring', A2)
    show('fundamental rep V(omega1)', V)
    show('fundamental rep V(omega2)', W)
    show('V*W decomposition', V * W)
    show('V^2 decomposition', V * V)
    show('V dimension', V.degree())


def lie_algebra_basic():
    L = LieAlgebra(QQ, cartan_type=['A', 2])
    show('LieAlgebra', L)
    e1, e2, f1, f2, h1, h2 = L.gens()
    show('gens', L.gens())
    show('[e1,f1]', e1.bracket(f1))
    show('[h1,e1]', h1.bracket(e1))
    show('[h1,e2]', h1.bracket(e2))
    # Computational Jacobi identity on a simple triple.
    jac = e1.bracket(e2.bracket(f1)) + e2.bracket(f1.bracket(e1)) + f1.bracket(e1.bracket(e2))
    show('Jacobi(e1,e2,f1)', jac)
    show('Jacobi is zero', jac == L.zero())


def crystals_basic():
    C = crystals.Tableaux(['A', 2], shape=[2, 1])
    show('Crystal', C)
    gens = C.module_generators
    show('module_generators', gens)
    b = gens[0]
    show('highest weight element', b)
    show('f_1(b)', b.f(1))
    show('f_2(b)', b.f(2))
    b1 = b.f(1)
    if b1 is not None:
        show('e_1(f_1(b))', b1.e(1))
        show('e_1(f_1(b)) == b', b1.e(1) == b)
    show('cardinality', C.cardinality())
    show('first few elements', list(C)[:8])


def quantum_q_numbers():
    from sage.algebras.quantum_groups.q_numbers import q_int, q_factorial, q_binomial
    q = polygen(ZZ, 'q')
    show('q_int(3)', q_int(3, q))
    show('q_factorial(4)', q_factorial(4, q))
    show('q_binomial(5,2)', q_binomial(5, 2, q))


def quantum_gap_probe():
    import importlib
    try:
        mod = importlib.import_module('sage.algebras.quantum_groups.quantum_group_gap')
        show('quantum_group_gap module', mod)
        show('module names sample', [x for x in dir(mod) if 'Quantum' in x or 'Group' in x][:20])
        try:
            from sage.all import algebras
            Q = algebras.QuantumGroup(['A', 2])
            show('QuantumGroup([A,2])', Q)
        except Exception as e:
            show('QuantumGroup([A,2]) construction', f'FAIL as expected on current HITK: {type(e).__name__}: {e}')
    except Exception as e:
        show('quantum_group_gap import failed', f'{type(e).__name__}: {e}')
    try:
        import sage.algebras.quantum_groups as qg
        show('quantum_groups package path', getattr(qg, '__path__', None))
        show('quantum_groups dir sample', [x for x in dir(qg) if not x.startswith('_')][:30])
    except Exception as e:
        show('quantum_groups package failed', f'{type(e).__name__}: {e}')

for name, fn in [
    ('Cartan types, root systems, weight lattices', cartan_roots),
    ('Weyl group and Coxeter relations', weyl_group),
    ('Weyl character ring / representation decompositions', weyl_characters),
    ('Lie algebra brackets / Jacobi identity', lie_algebra_basic),
    ('Crystals / Kashiwara operators', crystals_basic),
    ('Quantum q-numbers', quantum_q_numbers),
    ('Quantum group module probe', quantum_gap_probe),
]:
    run(name, fn)
