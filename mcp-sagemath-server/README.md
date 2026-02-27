# mcp-sagemath-server

Minimal MCP server to run SageMath from Codex/Claude.

## Tools included
1. `sage_version`
2. `sage_eval`
3. `sage_solve`
4. `sage_run`
5. `fusion_ring_api_catalog`
6. `fusion_ring_eval`

## Local run (for development)
```bash
cd /Users/cesargalindo/Documents/docencia/presentaciones/mcp-sagemath-server
uv run server.py
```

If your Sage command is not `sage`, set:
```bash
export SAGE_CMD="/path/to/sage"
```

## Register in Codex
```bash
codex mcp add sagemath-mcp -- /Users/cesargalindo/.local/bin/uv run --directory /Users/cesargalindo/Documents/docencia/presentaciones/mcp-sagemath-server server.py
```

## Example requests
1. `Usa sagemath-mcp para calcular la version de Sage.`
2. `Usa sagemath-mcp y evalua factor(x^4 - 1).`
3. `Usa sagemath-mcp para resolver x^2 - 5*x + 6 == 0 en x.`
4. `Usa sagemath-mcp y ejecuta codigo Sage para una matriz 3x3 y su determinante.`
5. `Usa sagemath-mcp y dame el catalogo API de fusion_ring.`
6. `Usa sagemath-mcp y evalua en FusionRing("A2",2): FR.s_matrix(unitary=True).`
