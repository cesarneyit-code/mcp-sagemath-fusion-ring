# MCP SageMath Fusion Rings

Public MCP server and skill bundle focused on `sage.algebras.fusion_rings` workflows.

## Contents
1. `mcp-sagemath-server/`
- Local stdio MCP server for SageMath.
- Includes generic tools (`sage_eval`, `sage_run`, etc.) plus fusion-ring tools:
 1. `fusion_ring_api_catalog`
 2. `fusion_ring_eval`
 3. `fusion_ring_fusion_rules`
 4. `fusion_ring_simple_objects`
 5. `fusion_ring_modular_data`

2. `skills/fusion-ring-sagemath/`
- Codex skill to translate natural-language math questions into exact `FusionRing` API calls.
- Includes package map and question-to-API references.

3. `revision_paquete_fusion_rings_sagemath.md`
- Detailed review of the package and practical usage checklist.

## Requirements
1. SageMath installed locally.
2. `uv` installed (`https://docs.astral.sh/uv/`).

## Local setup (recommended)
```bash
git clone https://github.com/cesarneyit-code/mcp-sagemath-fusion-ring.git
cd mcp-sagemath-fusion-ring/mcp-sagemath-server
uv sync
uv run server.py
```

## Register MCP in Codex

```bash
codex mcp add sagemath-mcp \
  --env SAGE_CMD=/Applications/SageMath-10-1.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  -- /usr/local/bin/uv run --project /ABSOLUTE/PATH/mcp-sagemath-fusion-ring/mcp-sagemath-server server.py
```

## Register MCP in Claude/Cursor style JSON

```json
{
  "mcpServers": {
    "sagemath-mcp": {
      "command": "/usr/local/bin/uv",
      "args": [
        "run",
        "--project",
        "/ABSOLUTE/PATH/mcp-sagemath-fusion-ring/mcp-sagemath-server",
        "server.py"
      ],
      "env": {
        "SAGE_CMD": "/Applications/SageMath-10-1.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage"
      }
    }
  }
}
```

## Example prompts
1. `Use sagemath-mcp and show the fusion_ring API catalog.`
2. `Use sagemath-mcp and evaluate on FusionRing("A2",2): FR.s_matrix(unitary=True).`
3. `Use sagemath-mcp and compute Nk_ij for selected simple objects in G2 level 1.`
4. `Use sagemath-mcp and give me the fusion rules of G_2 level 3.`
5. `Use sagemath-mcp and show simple objects of G_2 level 3 with labels, weights, q-dimensions and twists.`
6. `Use sagemath-mcp and give me modular data (S and T matrices) for G_2 level 3.`

## Practical examples (clear and ready to use)

### 1) Fusion rules
Question:
```text
Use sagemath-mcp and give me the fusion rules of G_2 level 3.
```

Tool used:
- `fusion_ring_fusion_rules(ct="G2", k=3)`

What you get:
- Full table of products `X_i * X_j = sum_k N^k_{ij} X_k`
- Canonical index order `[i]` for simple objects
- Output ready to cite in notes/classes

### 2) Modular data (S and T)
Question:
```text
Use sagemath-mcp and give me modular data (S and T matrices) for G_2 level 3.
```

Tool used:
- `fusion_ring_modular_data(ct="G2", k=3, unitary=True)`

What you get:
- `S` matrix (exact cyclotomic form)
- `T` matrix (exact, diagonal twists)
- Index map `i -> simple object` to interpret rows/columns
- Global quantum dimension and Virasoro central charge

Numeric approximation version:
```text
Use sagemath-mcp and give me modular data for G_2 level 3 with numerical approximation (25 digits).
```

### 3) Simple objects explained
Question:
```text
Use sagemath-mcp and show simple objects of G_2 level 3 with labels, weights, q-dimensions and twists.
```

Tool used:
- `fusion_ring_simple_objects(ct="G2", k=3)`

What you get:
- For each simple object:
  - index `[i]`
  - label (e.g. `G23(1,0)`)
  - weight
  - quantum dimension
  - twist
  - ribbon
- Explicit statement that this same index order is used in `S`, `T`, and fusion rules

### 4) Custom query on a fixed ring
Question:
```text
Use sagemath-mcp and evaluate on FusionRing("G2",3): FR.s_ij(simples[1], simples[2]).
```

Tool used:
- `fusion_ring_eval(ct="G2", k=3, expression="FR.s_ij(simples[1], simples[2])")`

What you get:
- Exact single matrix entry in cyclotomic form
- Ideal when you need one coefficient/invariant and not the full tables

## Prompt templates (copy/paste)
1. `Use sagemath-mcp and give me fusion rules for <CartanType> level <k>.`
2. `Use sagemath-mcp and give me modular data (S and T matrices) for <CartanType> level <k>.`
3. `Use sagemath-mcp and explain the simple objects for <CartanType> level <k> (labels, weights, q-dimensions, twists).`
4. `Use sagemath-mcp and compute <exact expression> on FusionRing("<CartanType>", <k>).`

## Complete natural-language capability list

1. Sage environment/version checks
Ask: `Use sagemath-mcp and show the Sage version.`

2. General symbolic evaluation
Ask: `Use sagemath-mcp and evaluate factor(x^6 - 1).`

3. Equation solving
Ask: `Use sagemath-mcp and solve x^2 - 5*x + 6 == 0 in x.`

4. Custom Sage snippets (multi-line)
Ask: `Use sagemath-mcp and run Sage code to define a matrix and compute its determinant.`

5. Fusion-ring API discovery
Ask: `Use sagemath-mcp and show the fusion_ring API catalog.`

6. Build-and-evaluate on a specific ring
Ask: `Use sagemath-mcp and evaluate on FusionRing("A2",2): FR.global_q_dimension().`

7. Full fusion rules
Ask: `Use sagemath-mcp and give me the fusion rules of G_2 level 3.`

8. Single fusion coefficient queries
Ask: `Use sagemath-mcp and evaluate on FusionRing("G2",3): FR.Nk_ij(simples[1], simples[2], simples[3]).`

9. Modular data (S and T, exact)
Ask: `Use sagemath-mcp and give me modular data (S and T matrices) for G_2 level 3.`

10. Modular data (numeric approximation)
Ask: `Use sagemath-mcp and give me modular data for G_2 level 3 with numerical approximation (30 digits).`

11. S-matrix entry queries
Ask: `Use sagemath-mcp and evaluate on FusionRing("G2",3): FR.s_ij(simples[1], simples[2]).`

12. Simple objects explained
Ask: `Use sagemath-mcp and show simple objects of G_2 level 3 with labels, weights, q-dimensions and twists.`

13. Twists/ribbon/central-charge interpretation
Ask: `Use sagemath-mcp and explain twists, ribbon values, and the Virasoro central charge for G_2 level 3.`

14. Multiplicity-free checks
Ask: `Use sagemath-mcp and check whether FusionRing("G2",3) is multiplicity-free.`

15. R-matrix and braid-related requests
Ask: `Use sagemath-mcp and evaluate an R-matrix coefficient for selected simple objects in G_2 level 3.`

16. F-symbol / F-matrix workflows
Ask: `Use sagemath-mcp and compute F-symbol data for a chosen FusionRing and explain the result.`

17. Field/roots-of-unity and cyclotomic options
Ask: `Use sagemath-mcp and explain the cyclotomic field and root-of-unity data for G_2 level 3.`

18. Conjugate-ring and conjugation matrix requests
Ask: `Use sagemath-mcp and compute the conjugation matrix for FusionRing("G2",3).`

19. Label customization/reset requests
Ask: `Use sagemath-mcp and set custom fusion labels, then show the updated simple-object view.`

20. Bilingual phrasing support in prompts
You can ask in English or Spanish; tool execution is the same and outputs remain mathematically explicit.

## Notes
1. Some Sage versions expose `test_braid_representation` instead of `check_braid_representation`.
2. Use exact outputs first (cyclotomic form), then request numerical approximation if needed.
3. This repo intentionally uses local execution from source; no automatic registry publication is required.
