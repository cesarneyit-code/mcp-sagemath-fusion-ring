# SageMath `fusion_rings` package map (detailed)

## Primary sources
1. `fusion_ring` docs:
https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/fusion_rings/fusion_ring.html
2. Package index:
https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/fusion_rings/index.html

## Module list in package
1. `fusion_ring`
2. `fusion_double`
3. `f_matrix`
4. `fast_parallel_fmats_methods`
5. `fast_parallel_fusion_ring_braid_repn`
6. `poly_tup_engine`
7. `shm_managers`

## Runtime caveat
Local runtime may differ from latest docs.
Example observed: some versions expose `test_braid_representation` instead of `check_braid_representation`.

## `FusionRing` constructor
Documented signature:
`FusionRing(ct, base_ring=Integer Ring, prefix=None, style='lattice', k=None, conjugate=False, cyclotomic_order=None, fusion_labels=None, inject_variables=False)`

Most common practical call:
`FusionRing("A2", 2)` or `FusionRing("G2", 1)`

Important arguments:
1. `ct`: Cartan type
2. `k`: level
3. `conjugate`: conjugate ring
4. `cyclotomic_order`: override field order when needed
5. `fusion_labels`, `inject_variables`: basis labels and variable injection

## `FusionRing` method catalog

### Core invariants and dimensions
1. `fusion_level()`
2. `fusion_l()`
3. `global_q_dimension()`
4. `total_q_order()`
5. `virasoro_central_charge()`
6. `D_plus()`
7. `D_minus()`

### Fusion coefficients and basis/order
1. `get_order()`
2. `some_elements()`
3. `N_ijk(elt_i, elt_j, elt_k)`
4. `Nk_ij(elt_i, elt_j, elt_k)`
5. `is_multiplicity_free()`
6. `fusion_labels(labels=None, inject_variables=False)`

### S, R, twist data
1. `s_matrix(unitary=False, base_coercion=True)`
2. `s_ij(elt_i, elt_j, base_coercion=True)`
3. `s_ijconj(elt_i, elt_j, base_coercion=True)`
4. `r_matrix(i, j, k, base_coercion=True)`
5. `twists_matrix()`
6. `conj_matrix()`
7. `root_of_unity(r, base_coercion=True)`

### Braid and computational basis
1. `get_braid_generators(...)`
2. `gens_satisfy_braid_gp_rels(sig, ...)`
3. `get_computational_basis(a, b, n_strands)`
4. `check_braid_representation(...)` or `test_braid_representation(...)` (version-dependent)

### Field and F-symbols
1. `field()`
2. `fvars_field()`
3. `get_fmatrix(*args, **kwargs)`

## `FusionRing.Element` methods
1. `is_simple_object()`
2. `weight()`
3. `q_dimension(base_coercion=True)`
4. `twist(reduced=True)`
5. `ribbon(base_coercion=True)`

## `FusionDouble` method catalog (main points)
1. `group()`
2. `dual(...)`
3. `N_ijk(...)`, `Nk_ij(...)`
4. `s_matrix(...)`, `s_ij(...)`, `s_ijconj(...)`
5. `r_matrix(...)`, `root_of_unity(...)`
6. `global_q_dimension()`, `total_q_order()`
7. `get_fmatrix(...)`
8. `inject_variables()`
9. `is_multiplicity_free()`

Element-level methods include:
1. `char`
2. `dual()`
3. `g`
4. `is_simple_object()`
5. `q_dimension()`
6. `twist()`
7. `ribbon()`

## `FMatrix` catalog (solver/factory)

### Lifecycle
1. `clear_vars()`
2. `clear_equations()`
3. `start_worker_pool()`
4. `shutdown_worker_pool()`

### Building equations and solving
1. `get_defining_equations(...)`
2. `get_orthogonality_constraints(...)`
3. `find_cyclotomic_solution(...)`
4. `find_orthogonal_solution(...)`
5. `certify_pentagons(...)`

### Accessing F-symbols
1. `fmat(a,b,c,d,x,y)`
2. `fmatrix(a,b,c,d)`
3. `get_fvars()`
4. `get_fvars_by_size(n)`
5. `get_fvars_in_alg_field()`
6. `fvars_are_real()`
7. `fmats_are_orthogonal()`

### Fields/embeddings/storage
1. `field()`
2. `get_non_cyclotomic_roots()`
3. `get_qqbar_embedding()`
4. `get_coerce_map_from_fr_cyclotomic_field()`
5. `get_radical_expression(...)`
6. `save_fvars(...)`
7. `load_fvars(...)`

## Utility modules

### `poly_tup_engine`
Polynomial tuple representation helpers:
1. `poly_to_tup`
2. `tup_to_univ_poly`
3. `compute_known_powers`
4. `apply_coeff_map`
5. `variables`
6. `get_variables_degrees`
7. `constant_coeff`
8. `resize`
9. `poly_tup_sortkey`

### `shm_managers`
Shared-memory helpers for parallel F-symbol workflows:
1. `FvarsHandler`, `KSHandler`
2. `make_FvarsHandler`, `make_KSHandler`
3. `items`, `update`, `shm`

### Parallel executors
1. `fast_parallel_fmats_methods.executor`
2. `fast_parallel_fusion_ring_braid_repn.executor`

## Practical coverage checklist
Use this list when user asks to "use the package completely":
1. Build `FusionRing(ct,k)`
2. Inspect basis/order and fusion coefficients
3. Compute modular data (`S`, twists, conjugation)
4. Validate braid-related computations
5. Compute F-symbols via `get_fmatrix`
6. Report field/cyclotomic assumptions explicitly
