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

## Notes
1. Some Sage versions expose `test_braid_representation` instead of `check_braid_representation`.
2. Use exact outputs first (cyclotomic form), then request numerical approximation if needed.
3. This repo intentionally uses local execution from source; no automatic registry publication is required.
