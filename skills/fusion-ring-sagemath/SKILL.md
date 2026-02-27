---
name: fusion-ring-sagemath
description: Interpret and solve advanced SageMath questions about fusion categories using `sage.algebras.fusion_rings`, with emphasis on `FusionRing` and related modules (`fusion_double`, `f_matrix`). Use when users ask in natural language (Spanish or English) for S-matrix, twists, fusion coefficients, R/F-symbols, braid generators, global quantum dimension, or verification workflows in fusion-ring computations.
---

# Fusion Ring Sagemath

## Overview

Translate natural-language questions into exact SageMath calls for `FusionRing` workflows.
Use this skill to move from conceptual/math phrasing to executable expressions with precise parameters and interpretable output.

## Quick Workflow

1. Identify ring setup from the question.
- Extract Cartan type `ct` (e.g. `"A2"`, `"G2"`) and level `k`.
- Detect optional settings: `conjugate`, `cyclotomic_order`, `fusion_labels`.

2. Instantiate and normalize notation.
- Use `FR = FusionRing(ct, k, ...)`.
- Keep aliases `R = FR`, `order = FR.get_order()`, `simples = [FR(w) for w in order]`.

3. Map user intent to API method(s).
- Use `references/fusion_ring_question_to_api.md` for intent-to-method mapping.
- Use `references/fusion_rings_package_map.md` for full module/method coverage.

4. Execute and explain.
- Prefer the `fusion_ring_eval` tool from `sagemath-mcp` when available.
- Otherwise run equivalent Sage code using `sage_run`.
- Always return:
 1. exact call used,
 2. mathematical interpretation,
 3. any caveat about field/roots of unity or multiplicities.

## Version Compatibility Notes

1. Docs may describe newer Sage versions than local runtime.
2. In some versions, `check_braid_representation` appears as `test_braid_representation`.
3. If a method is missing, report the version mismatch and propose the closest available method.

## Response Rules

1. Keep the response mathematically explicit.
2. Show the exact Sage expression before giving interpretation.
3. If result is cyclotomic-heavy, offer a simplified/numeric view after the exact output.
4. For ambiguous questions, state assumptions (`ct`, `k`, object labels/order).
5. When asked to "review all package details", cover all modules listed in `references/fusion_rings_package_map.md`.

## Minimal Examples

1. User asks: "Calcula la S-matrix unitaria para A2 nivel 2."
- Call: `FR = FusionRing("A2", 2); FR.s_matrix(unitary=True)`

2. User asks: "Dame N^k_{ij} para i,j,k concretos."
- Call: `FR.Nk_ij(i, j, k)` after defining basis elements from `FR.get_order()`.

3. User asks: "Quiero F-symbols."
- Call: `Fm = FR.get_fmatrix(...); Fm.fmat(...)` / `Fm.fmatrix(...)` depending on requested coefficient/matrix.

## References

1. Full package map and methods:
- `references/fusion_rings_package_map.md`

2. Natural language to API mapping (Spanish prompts):
- `references/fusion_ring_question_to_api.md`
