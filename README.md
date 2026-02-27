# MCP SageMath Fusion Rings

Public MCP server and skill bundle focused on `sage.algebras.fusion_rings` workflows.

## Contents
1. `mcp-sagemath-server/`
- Local stdio MCP server for SageMath.
- Includes generic tools (`sage_eval`, `sage_run`, etc.) plus fusion-ring tools:
 1. `fusion_ring_api_catalog`
 2. `fusion_ring_eval`

2. `skills/fusion-ring-sagemath/`
- Codex skill to translate natural-language math questions into exact `FusionRing` API calls.
- Includes package map and question-to-API references.

3. `revision_paquete_fusion_rings_sagemath.md`
- Detailed review of the package and practical usage checklist.

## Requirements
1. SageMath installed locally.
2. `uv` installed (`https://docs.astral.sh/uv/`).

## Install options for other clients

### Option A: PyPI / `uvx` (recommended)
```bash
uvx mcp-sagemath-fusion-rings
```

### Option B: npm / `npx` wrapper
```bash
npx -y mcp-sagemath-fusion-rings
```

## Register MCP in Codex

```bash
codex mcp add sagemath-mcp \
  --env SAGE_CMD=/Applications/SageMath-10-1.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  -- /Users/cesargalindo/.local/bin/uvx mcp-sagemath-fusion-rings
```

## Register MCP in Claude/Cursor style JSON

```json
{
  "mcpServers": {
    "sagemath-mcp": {
      "command": "/Users/cesargalindo/.local/bin/uvx",
      "args": [
        "mcp-sagemath-fusion-rings"
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

## Notes
1. Some Sage versions expose `test_braid_representation` instead of `check_braid_representation`.
2. Use exact outputs first (cyclotomic form), then request numerical approximation if needed.
3. Publication workflows are included:
- `.github/workflows/publish-pypi.yml` (tag `pypi-v*`)
- `.github/workflows/publish-npm.yml` (tag `npm-v*`)

## Release tags
1. PyPI release:
```bash
git tag pypi-v0.2.0
git push origin pypi-v0.2.0
```
2. npm wrapper release:
```bash
git tag npm-v0.2.0
git push origin npm-v0.2.0
```
