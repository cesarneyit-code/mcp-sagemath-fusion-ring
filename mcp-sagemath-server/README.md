# mcp-sagemath-fusion-rings

MCP server to run SageMath from Codex/Claude with dedicated `FusionRing` helpers.

## Tools included
1. `sage_version`
2. `sage_eval`
3. `sage_solve`
4. `sage_run`
5. `fusion_ring_api_catalog`
6. `fusion_ring_eval`
7. `fusion_ring_fusion_rules`
8. `fusion_ring_simple_objects`
9. `fusion_ring_modular_data`

## Local run (for development)
```bash
cd /ABSOLUTE/PATH/TO/mcp-sagemath-fusion-ring/mcp-sagemath-server
uv sync
uv run server.py
```

If your Sage command is not `sage`, set:
```bash
export SAGE_CMD="/path/to/sage"
```

## Register in Codex
```bash
codex mcp add sagemath-mcp \
  --env SAGE_CMD=/path/to/sage \
  -- /usr/local/bin/uv run --project /ABSOLUTE/PATH/TO/mcp-sagemath-fusion-ring/mcp-sagemath-server server.py
```

## Example requests
1. `Use sagemath-mcp and show the Sage version.`
2. `Use sagemath-mcp and evaluate factor(x^4 - 1).`
3. `Use sagemath-mcp and solve x^2 - 5*x + 6 == 0 in x.`
4. `Use sagemath-mcp and run Sage code for a 3x3 matrix and its determinant.`
5. `Use sagemath-mcp and show the fusion_ring API catalog.`
6. `Use sagemath-mcp and evaluate on FusionRing("A2",2): FR.s_matrix(unitary=True).`
7. `Use sagemath-mcp and give me the fusion rules of G_2 level 3.`
8. `Use sagemath-mcp and show simple objects for G_2 level 3 with q-dimensions and twists.`
9. `Use sagemath-mcp and give me modular data (S and T matrices) for G_2 level 3.`
