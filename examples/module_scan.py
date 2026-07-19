import importlib
import pkgutil

modules = [
    'sage.combinat.root_system.cartan_type',
    'sage.combinat.root_system.root_system',
    'sage.combinat.root_system.weyl_group',
    'sage.combinat.root_system.weight_lattice_realizations',
    'sage.combinat.root_system.weyl_characters',
    'sage.algebras.lie_algebras.lie_algebra',
    'sage.algebras.lie_algebras.catalog',
    'sage.combinat.crystals.catalog',
    'sage.combinat.crystals.tensor_product',
    'sage.combinat.crystals.highest_weight_crystals',
    'sage.algebras.quantum_groups',
    'sage.algebras.quantum_groups.q_numbers',
    'sage.algebras.quantum_groups.quantum_group_gap',
    'sage.algebras.quantum_groups.quantum_enveloping_algebra',
]
print('## import checks')
for m in modules:
    try:
        mod = importlib.import_module(m)
        print(f'OK {m} -> {getattr(mod, "__file__", None)}')
    except Exception as e:
        print(f'FAIL {m}: {type(e).__name__}: {e}')

print('\n## sage.algebras submodules containing quantum/lie')
try:
    import sage.algebras as algebras
    names = sorted([x.name for x in pkgutil.iter_modules(algebras.__path__) if 'quantum' in x.name.lower() or 'lie' in x.name.lower()])
    for n in names:
        print(n)
except Exception as e:
    print('scan algebras failed', repr(e))

print('\n## sage.combinat submodules containing crystal/root/weyl')
try:
    import sage.combinat as combinat
    names = sorted([x.name for x in pkgutil.iter_modules(combinat.__path__) if any(k in x.name.lower() for k in ['crystal','root','weyl'])])
    for n in names:
        print(n)
except Exception as e:
    print('scan combinat failed', repr(e))
