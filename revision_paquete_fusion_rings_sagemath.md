# Revision detallada del paquete `sage.algebras.fusion_rings`
Fecha: 27 febrero 2026

## Fuente principal revisada
1. https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/fusion_rings/fusion_ring.html
2. Índice del paquete: https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/fusion_rings/index.html

## Cobertura del paquete completo
Módulos incluidos en la documentación del paquete:
1. `fusion_ring`
2. `fusion_double`
3. `f_matrix`
4. `fast_parallel_fmats_methods`
5. `fast_parallel_fusion_ring_braid_repn`
6. `poly_tup_engine`
7. `shm_managers`

## Núcleo del trabajo matemático: `FusionRing`
Constructor documentado:
`FusionRing(ct, ..., k=None, conjugate=False, cyclotomic_order=None, fusion_labels=None, inject_variables=False)`

Uso habitual:
1. `FR = FusionRing("A2", 2)`
2. `order = FR.get_order()`
3. `simples = [FR(w) for w in order]`

### Invariantes y datos modulares más usados
1. `FR.s_matrix(unitary=True)` (matriz S unitaria)
2. `FR.s_ij(...)`, `FR.s_ijconj(...)`
3. `FR.twists_matrix()`
4. `FR.global_q_dimension()`
5. `FR.total_q_order()`
6. `FR.virasoro_central_charge()`
7. `FR.conj_matrix()`

### Coeficientes de fusión
1. `FR.Nk_ij(i,j,k)` (coeficiente \(N^k_{ij}\))
2. `FR.N_ijk(i,j,k)` (versión simétrica)
3. `FR.is_multiplicity_free()`

### Braid y representaciones
1. `FR.get_braid_generators(...)`
2. `FR.gens_satisfy_braid_gp_rels(...)`
3. `FR.check_braid_representation(...)` o `FR.test_braid_representation(...)` (depende de versión)

### F-symbols
1. `Fm = FR.get_fmatrix(...)`
2. `Fm.get_defining_equations(...)`
3. `Fm.find_cyclotomic_solution(...)` / `Fm.find_orthogonal_solution(...)`
4. `Fm.fmat(...)` y `Fm.fmatrix(...)`

## `FusionDouble`
Para cálculos sobre el doble cuántico:
1. `FD = FusionDouble(...)`
2. `FD.s_matrix()`, `FD.r_matrix(...)`
3. `FD.Nk_ij(...)`
4. `FD.global_q_dimension()`, `FD.total_q_order()`

## Módulos auxiliares del paquete
1. `f_matrix`: construcción/solución de ecuaciones para F-symbols
2. `poly_tup_engine`: utilidades internas para polinomios en representación tipo tupla
3. `shm_managers`: estructuras para memoria compartida en cómputo paralelo
4. `fast_parallel_*`: ejecutores paralelos para tareas de F-matrices y braid

## Diferencias versión doc vs runtime local
Observación práctica importante:
1. Tu runtime local de Sage reportó `SageMath version 10.1.beta5`.
2. En esta versión, puede aparecer `test_braid_representation` donde la doc usa `check_braid_representation`.

## Cómo preguntar para que Codex interprete bien
Usa formato explícito:
1. Tipo de Cartan y nivel.
2. Invariante/matriz exacta.
3. Formato de salida (exacto, numérico, explicación).

Ejemplos:
1. `Usa FusionRing("G2",1) y calcula la s_matrix unitaria.`
2. `En A2 nivel 2, dame N^k_{ij} para i=0, j=1, k=2 usando el orden fijo de get_order().`
3. `Construye FMatrix para A2 nivel 2 y reporta fmat(a,b,c,d,x,y) para los índices que te dé.`

## Entregables implementados en este proyecto
1. Skill local: `skills/fusion-ring-sagemath`
2. Referencia completa del paquete:
- `skills/fusion-ring-sagemath/references/fusion_rings_package_map.md`
3. Mapeo pregunta natural -> API:
- `skills/fusion-ring-sagemath/references/fusion_ring_question_to_api.md`
4. MCP Sage ampliado con tools:
- `fusion_ring_api_catalog`
- `fusion_ring_eval`
