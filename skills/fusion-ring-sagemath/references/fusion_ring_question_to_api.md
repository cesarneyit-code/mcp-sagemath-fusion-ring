# FusionRing: natural language -> API mapping

Use this map to translate natural-language questions into executable Sage calls.

## Setup template
```python
from sage.algebras.fusion_rings.fusion_ring import FusionRing
FR = FusionRing("A2", 2)  # replace Cartan type and level
order = FR.get_order()
simples = [FR(w) for w in order]
```

## Typical user intents

1. "Give me the S-matrix" / "unitary S-matrix"
- `FR.s_matrix()`
- `FR.s_matrix(unitary=True)`
- Prefer MCP tool for full modular context:
  - `fusion_ring_modular_data(ct="G2", k=3, unitary=True)`

2. "Give me the entry S_{ij}"
- `FR.s_ij(simples[i], simples[j])`
- `FR.s_ijconj(simples[i], simples[j])`

3. "Fusion coefficients"
- `FR.Nk_ij(simples[i], simples[j], simples[k])`
- `FR.N_ijk(simples[i], simples[j], simples[k])`
- For full fusion table/rules in one shot:
  - `fusion_ring_fusion_rules(ct="G2", k=3)` (via MCP tool)

4. "Give me the T-matrix" / "modular data"
- `FR.twists_matrix()`
- Prefer MCP tool for S+T+indexing+interpretation:
  - `fusion_ring_modular_data(ct="G2", k=3, unitary=True)`

5. "Explain the simple objects / labels / weights / quantum dimensions / twists"
- `fusion_ring_simple_objects(ct="G2", k=3)`
- Optional numeric output:
  - `fusion_ring_simple_objects(ct="G2", k=3, include_numeric_approx=True, digits=30)`

6. "Is it multiplicity-free?"
- `FR.is_multiplicity_free()`

7. "Global quantum dimension / total quantum order"
- `FR.global_q_dimension()`
- `FR.total_q_order()`

8. "Twists / ribbon / central charge"
- `FR.twists_matrix()`
- `simples[i].twist()`
- `simples[i].ribbon()`
- `FR.virasoro_central_charge()`

9. "Dual conjugation and conjugation matrix"
- `FR.conj_matrix()`

10. "R-matrix"
- `FR.r_matrix(simples[i], simples[j], simples[k])`

11. "F-symbols / pentagon relations"
- `Fm = FR.get_fmatrix(...)`
- `Fm.get_defining_equations(...)`
- `Fm.find_cyclotomic_solution(...)`
- `Fm.fmat(a,b,c,d,x,y)` or `Fm.fmatrix(a,b,c,d)`

12. "Braid generators / validate braid relations"
- `FR.get_braid_generators(...)`
- `FR.gens_satisfy_braid_gp_rels(sig, ...)`
- Version-dependent:
 1. `FR.check_braid_representation(...)`
 2. or `FR.test_braid_representation(...)`

13. "Cyclotomic field / roots of unity"
- `FR.field()`
- `FR.root_of_unity(r)`
- If needed: rebuild ring with explicit `cyclotomic_order=...`

14. "Simple-object labels"
- `FR.fusion_labels(...)`
- `FR.fusion_labels()` to reset

## Translation patterns

1. If user says "simple object i", map to `simples[i]` after fixing `order`.
2. If user gives dominant weight explicitly, use `FR(weight_expression)`.
3. If user asks for "exacto + numérico", run exact call then `CC(...)` or `N(...)`.
4. If user asks "explica", always show both:
- exact Sage call,
- interpretation (what invariant means mathematically).

## Robust answer format

1. Setup used (`ct`, `k`, options).
2. Exact expression executed.
3. Output.
4. Interpretation.
5. Notes on version/field caveats if applicable.
