# mcp-sagemath-fusion-rings

MCP server to run SageMath from Codex/Claude with dedicated `FusionRing` helpers.

## Tools included
1. `sage_version`
2. `sage_eval`
3. `sage_solve`
4. `sage_run`
5. `fusion_ring_api_catalog`
6. `fusion_ring_eval`

## Local run (for development)
```bash
cd /ABSOLUTE/PATH/TO/mcp-sagemath-fusion-ring/mcp-sagemath-server
uv run server.py
```

If your Sage command is not `sage`, set:
```bash
export SAGE_CMD="/path/to/sage"
```

## Install from PyPI (planned target)
```bash
uv tool install mcp-sagemath-fusion-rings
```

Or one-shot execution:
```bash
uvx mcp-sagemath-fusion-rings
```

## Register in Codex
```bash
codex mcp add sagemath-mcp \
  --env SAGE_CMD=/path/to/sage \
  -- /Users/cesargalindo/.local/bin/uvx mcp-sagemath-fusion-rings
```

## Example requests
1. `Usa sagemath-mcp para calcular la version de Sage.`
2. `Usa sagemath-mcp y evalua factor(x^4 - 1).`
3. `Usa sagemath-mcp para resolver x^2 - 5*x + 6 == 0 en x.`
4. `Usa sagemath-mcp y ejecuta codigo Sage para una matriz 3x3 y su determinante.`
5. `Usa sagemath-mcp y dame el catalogo API de fusion_ring.`
6. `Usa sagemath-mcp y evalua en FusionRing("A2",2): FR.s_matrix(unitary=True).`
