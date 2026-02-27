# FusionRing: natural language -> API mapping

Use this map to translate Spanish questions into executable Sage calls.

## Setup template
```python
from sage.algebras.fusion_rings.fusion_ring import FusionRing
FR = FusionRing("A2", 2)  # replace Cartan type and level
order = FR.get_order()
simples = [FR(w) for w in order]
```

## Typical user intents

1. "Dame la matriz S" / "S-matrix unitaria"
- `FR.s_matrix()`
- `FR.s_matrix(unitary=True)`
- Prefer MCP tool for full modular context:
  - `fusion_ring_modular_data(ct="G2", k=3, unitary=True)`

2. "Dame la entrada S_{ij}"
- `FR.s_ij(simples[i], simples[j])`
- `FR.s_ijconj(simples[i], simples[j])`

3. "Coeficientes de fusión"
- `FR.Nk_ij(simples[i], simples[j], simples[k])`
- `FR.N_ijk(simples[i], simples[j], simples[k])`
- For full fusion table/rules in one shot:
  - `fusion_ring_fusion_rules(ct="G2", k=3)` (via MCP tool)

4. "Dame la matriz T" / "modular data"
- `FR.twists_matrix()`
- Prefer MCP tool for S+T+indexing+interpretation:
  - `fusion_ring_modular_data(ct="G2", k=3, unitary=True)`

5. "Explícame los objetos simples / labels / pesos / dimensiones cuánticas / twists"
- `fusion_ring_simple_objects(ct="G2", k=3)`
- Optional numeric output:
  - `fusion_ring_simple_objects(ct="G2", k=3, include_numeric_approx=True, digits=30)`

6. "¿Es multiplicity-free?"
- `FR.is_multiplicity_free()`

7. "Dimensión cuántica global / orden cuántico total"
- `FR.global_q_dimension()`
- `FR.total_q_order()`

8. "Twists / ribbon / carga central"
- `FR.twists_matrix()`
- `simples[i].twist()`
- `simples[i].ribbon()`
- `FR.virasoro_central_charge()`

9. "Conjugación dual y matriz de conjugación"
- `FR.conj_matrix()`

10. "R-matrix"
- `FR.r_matrix(simples[i], simples[j], simples[k])`

11. "F-symbols / pentagon relations"
- `Fm = FR.get_fmatrix(...)`
- `Fm.get_defining_equations(...)`
- `Fm.find_cyclotomic_solution(...)`
- `Fm.fmat(a,b,c,d,x,y)` or `Fm.fmatrix(a,b,c,d)`

12. "Braid generators / validar relaciones de trenza"
- `FR.get_braid_generators(...)`
- `FR.gens_satisfy_braid_gp_rels(sig, ...)`
- Version-dependent:
 1. `FR.check_braid_representation(...)`
 2. or `FR.test_braid_representation(...)`

13. "Campo ciclotómico / raíces de unidad"
- `FR.field()`
- `FR.root_of_unity(r)`
- If needed: rebuild ring with explicit `cyclotomic_order=...`

14. "Etiquetas de objetos simples"
- `FR.fusion_labels(...)`
- `FR.fusion_labels()` to reset

## Translation patterns

1. If user says "objeto simple i", map to `simples[i]` after fixing `order`.
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
