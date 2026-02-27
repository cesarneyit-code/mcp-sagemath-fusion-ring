from __future__ import annotations

import logging
import os
import subprocess
import sys
from typing import Any

from mcp.server.fastmcp import FastMCP


# IMPORTANT: STDIO MCP servers must not write logs to stdout.
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("mcp-sagemath-server")

mcp = FastMCP("sagemath")

FUSION_RING_METHODS = [
    "D_minus",
    "D_plus",
    "N_ijk",
    "Nk_ij",
    "conj_matrix",
    "field",
    "fusion_l",
    "fusion_labels",
    "fusion_level",
    "fvars_field",
    "gens_satisfy_braid_gp_rels",
    "get_braid_generators",
    "get_computational_basis",
    "get_fmatrix",
    "get_order",
    "global_q_dimension",
    "is_multiplicity_free",
    "r_matrix",
    "root_of_unity",
    "s_ij",
    "s_ijconj",
    "s_matrix",
    "some_elements",
    "total_q_order",
    "twists_matrix",
    "virasoro_central_charge",
]

FUSION_RING_ELEMENT_METHODS = [
    "is_simple_object",
    "q_dimension",
    "ribbon",
    "twist",
    "weight",
]

FUSION_DOUBLE_METHODS = [
    "D_minus",
    "D_plus",
    "N_ijk",
    "Nk_ij",
    "dual",
    "field",
    "fvars_field",
    "get_fmatrix",
    "global_q_dimension",
    "group",
    "inject_variables",
    "is_multiplicity_free",
    "one_basis",
    "product_on_basis",
    "r_matrix",
    "root_of_unity",
    "s_ij",
    "s_ijconj",
    "s_matrix",
    "total_q_order",
]

FMATRIX_METHODS = [
    "attempt_number_field_computation",
    "certify_pentagons",
    "clear_equations",
    "clear_vars",
    "equations_graph",
    "f_from",
    "f_to",
    "field",
    "find_cyclotomic_solution",
    "find_orthogonal_solution",
    "findcases",
    "fmat",
    "fmatrix",
    "fmats_are_orthogonal",
    "fvars_are_real",
    "get_coerce_map_from_fr_cyclotomic_field",
    "get_defining_equations",
    "get_fvars",
    "get_fvars_by_size",
    "get_fvars_in_alg_field",
    "get_non_cyclotomic_roots",
    "get_orthogonality_constraints",
    "get_poly_ring",
    "get_qqbar_embedding",
    "get_radical_expression",
    "largest_fmat_size",
    "load_fvars",
    "save_fvars",
    "shutdown_worker_pool",
    "start_worker_pool",
]

PACKAGE_MODULES = [
    "fusion_ring",
    "fusion_double",
    "f_matrix",
    "fast_parallel_fmats_methods",
    "fast_parallel_fusion_ring_braid_repn",
    "poly_tup_engine",
    "shm_managers",
]


def _sage_command() -> str:
    return os.environ.get("SAGE_CMD", "sage")


def _run_sage(code: str, timeout_seconds: int) -> dict[str, Any]:
    cmd = [_sage_command(), "-c", code]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
    except FileNotFoundError:
        return {
            "ok": False,
            "returncode": 127,
            "stdout": "",
            "stderr": f"Sage command not found: {_sage_command()}",
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "ok": False,
            "returncode": 124,
            "stdout": (exc.stdout or "").strip(),
            "stderr": ((exc.stderr or "").strip() + "\nTimed out").strip(),
        }

    return {
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def _format_result(result: dict[str, Any]) -> str:
    if result["ok"]:
        out = result["stdout"] or "(no stdout)"
        err = result["stderr"]
        if err:
            return f"{out}\n\n[stderr]\n{err}"
        return out
    return (
        f"Error running SageMath (code {result['returncode']}).\n"
        f"stderr:\n{result['stderr'] or '(empty)'}\n\n"
        f"stdout:\n{result['stdout'] or '(empty)'}"
    )


@mcp.tool()
def sage_version(timeout_seconds: int = 10) -> str:
    """Return SageMath version.

    Args:
        timeout_seconds: Max runtime in seconds.
    """
    cmd = [_sage_command(), "--version"]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
    except FileNotFoundError:
        return f"Sage command not found: {_sage_command()}"
    except subprocess.TimeoutExpired:
        return f"Sage command timed out after {timeout_seconds}s: {_sage_command()} --version"

    stdout = proc.stdout.strip()
    stderr = proc.stderr.strip()
    if proc.returncode == 0:
        return stdout or "(no stdout)"
    return (
        f"Sage --version failed (code {proc.returncode}).\n"
        f"stderr:\n{stderr or '(empty)'}\n\n"
        f"stdout:\n{stdout or '(empty)'}"
    )


@mcp.tool()
def sage_eval(expression: str, timeout_seconds: int = 20) -> str:
    """Evaluate one SageMath expression and return its printed result.

    Args:
        expression: Sage expression, e.g. "factor(x^4 - 1)".
        timeout_seconds: Max runtime in seconds.
    """
    code = (
        "from sage.all import *\n"
        "from sage.misc.sage_eval import sage_eval\n"
        f"expr = {expression!r}\n"
        "result = sage_eval(expr, locals())\n"
        "print(result)\n"
    )
    result = _run_sage(code, timeout_seconds=timeout_seconds)
    return _format_result(result)


@mcp.tool()
def sage_solve(equation: str, variable: str = "x", timeout_seconds: int = 20) -> str:
    """Solve one equation in SageMath.

    Args:
        equation: Equation text, e.g. "x^2 - 5*x + 6 == 0".
        variable: Variable name, e.g. "x".
        timeout_seconds: Max runtime in seconds.
    """
    code = (
        "from sage.all import *\n"
        "from sage.misc.sage_eval import sage_eval\n"
        f"var_name = {variable!r}\n"
        "v = var(var_name)\n"
        f"eq_text = {equation!r}\n"
        "eq = sage_eval(eq_text, locals())\n"
        "print(solve(eq, v))\n"
    )
    result = _run_sage(code, timeout_seconds=timeout_seconds)
    return _format_result(result)


@mcp.tool()
def sage_run(code: str, timeout_seconds: int = 30) -> str:
    """Run raw SageMath code (multi-line allowed).

    Args:
        code: Raw Sage code. Use print(...) to emit outputs.
        timeout_seconds: Max runtime in seconds.
    """
    result = _run_sage(code, timeout_seconds=timeout_seconds)
    return _format_result(result)


@mcp.tool()
def fusion_ring_api_catalog(scope: str = "all") -> str:
    """Return a curated API catalog for SageMath fusion rings.

    Args:
        scope: One of "all", "fusion_ring", "fusion_double", "f_matrix".
    """
    scope = scope.strip().lower()
    if scope not in {"all", "fusion_ring", "fusion_double", "f_matrix"}:
        return (
            "Invalid scope. Use one of: all, fusion_ring, fusion_double, f_matrix."
        )

    parts: list[str] = []
    parts.append("Package modules:")
    parts.extend(f"- {m}" for m in PACKAGE_MODULES)

    if scope in {"all", "fusion_ring"}:
        parts.append("\nFusionRing methods:")
        parts.extend(f"- {m}" for m in FUSION_RING_METHODS)
        parts.append("\nFusionRing.Element methods:")
        parts.extend(f"- {m}" for m in FUSION_RING_ELEMENT_METHODS)
        parts.append(
            "\nNote: some Sage versions expose test_braid_representation "
            "instead of check_braid_representation."
        )

    if scope in {"all", "fusion_double"}:
        parts.append("\nFusionDouble methods:")
        parts.extend(f"- {m}" for m in FUSION_DOUBLE_METHODS)

    if scope in {"all", "f_matrix"}:
        parts.append("\nFMatrix methods:")
        parts.extend(f"- {m}" for m in FMATRIX_METHODS)

    return "\n".join(parts)


@mcp.tool()
def fusion_ring_eval(
    ct: str,
    k: int,
    expression: str,
    conjugate: bool = False,
    cyclotomic_order: int | None = None,
    fusion_labels: str | None = None,
    inject_variables: bool = False,
    timeout_seconds: int = 45,
) -> str:
    """Evaluate an expression on FusionRing(ct, k) with prepared locals.

    Prepared locals:
    - FR, R: the FusionRing object
    - basis: FR.basis()
    - order: FR.get_order()
    - simples: list of simple objects in fixed order

    Args:
        ct: Cartan type, e.g. "A2", "G2", "['A',2]".
        k: Fusion level.
        expression: Sage expression using FR/R, e.g. "FR.s_matrix(unitary=True)".
        conjugate: Build the conjugate ring.
        cyclotomic_order: Optional cyclotomic order override.
        fusion_labels: Optional labels setup.
        inject_variables: Passed to FusionRing constructor.
        timeout_seconds: Max runtime in seconds.
    """
    code = (
        "from sage.all import *\n"
        "from sage.misc.sage_eval import sage_eval\n"
        "from sage.algebras.fusion_rings.fusion_ring import FusionRing\n"
        f"ct_text = {ct!r}\n"
        "try:\n"
        "    ct_obj = sage_eval(ct_text, locals())\n"
        "except Exception:\n"
        "    ct_obj = ct_text\n"
        "kwargs = {}\n"
        f"kwargs['conjugate'] = {bool(conjugate)!r}\n"
        f"kwargs['inject_variables'] = {bool(inject_variables)!r}\n"
        f"kwargs['k'] = {int(k)!r}\n"
        f"cyclo = {cyclotomic_order!r}\n"
        "if cyclo is not None:\n"
        "    kwargs['cyclotomic_order'] = cyclo\n"
        f"lbls = {fusion_labels!r}\n"
        "if lbls is not None:\n"
        "    kwargs['fusion_labels'] = lbls\n"
        "FR = FusionRing(ct_obj, **kwargs)\n"
        "R = FR\n"
        "basis = FR.basis()\n"
        "order = FR.get_order()\n"
        "simples = [FR(w) for w in order]\n"
        f"expr = {expression!r}\n"
        "result = sage_eval(expr, locals())\n"
        "print(result)\n"
    )
    result = _run_sage(code, timeout_seconds=timeout_seconds)
    return _format_result(result)


@mcp.tool()
def fusion_ring_fusion_rules(
    ct: str,
    k: int,
    conjugate: bool = False,
    cyclotomic_order: int | None = None,
    fusion_labels: str | None = None,
    inject_variables: bool = False,
    timeout_seconds: int = 90,
) -> str:
    """Return full fusion rules N^k_{ij} for FusionRing(ct, k).

    Args:
        ct: Cartan type, e.g. "A2", "G2", "['A',2]".
        k: Fusion level.
        conjugate: Build the conjugate ring.
        cyclotomic_order: Optional cyclotomic order override.
        fusion_labels: Optional labels setup.
        inject_variables: Passed to FusionRing constructor.
        timeout_seconds: Max runtime in seconds.
    """
    code = (
        "from sage.all import *\n"
        "from sage.misc.sage_eval import sage_eval\n"
        "from sage.algebras.fusion_rings.fusion_ring import FusionRing\n"
        f"ct_text = {ct!r}\n"
        "try:\n"
        "    ct_obj = sage_eval(ct_text, locals())\n"
        "except Exception:\n"
        "    ct_obj = ct_text\n"
        "kwargs = {}\n"
        f"kwargs['conjugate'] = {bool(conjugate)!r}\n"
        f"kwargs['inject_variables'] = {bool(inject_variables)!r}\n"
        f"kwargs['k'] = {int(k)!r}\n"
        f"cyclo = {cyclotomic_order!r}\n"
        "if cyclo is not None:\n"
        "    kwargs['cyclotomic_order'] = cyclo\n"
        f"lbls = {fusion_labels!r}\n"
        "if lbls is not None:\n"
        "    kwargs['fusion_labels'] = lbls\n"
        "FR = FusionRing(ct_obj, **kwargs)\n"
        "order = FR.get_order()\n"
        "simples = [FR(w) for w in order]\n"
        "labels = [str(s) for s in simples]\n"
        "print(f'Fusion rules for FusionRing(ct={ct_text}, k={kwargs[\"k\"]})')\n"
        "print(f'Rank: {len(simples)}')\n"
        "print('Simple object order:')\n"
        "for idx, lbl in enumerate(labels):\n"
        "    print(f'  [{idx}] {lbl}')\n"
        "print('')\n"
        "for i, a in enumerate(simples):\n"
        "    for j, b in enumerate(simples):\n"
        "        terms = []\n"
        "        for kk, c in enumerate(simples):\n"
        "            coeff = FR.Nk_ij(a, b, c)\n"
        "            if coeff:\n"
        "                if coeff == 1:\n"
        "                    terms.append(labels[kk])\n"
        "                else:\n"
        "                    terms.append(f'{coeff}*{labels[kk]}')\n"
        "        rhs = ' + '.join(terms) if terms else '0'\n"
        "        print(f'[{i}] {labels[i]} * [{j}] {labels[j]} = {rhs}')\n"
    )
    result = _run_sage(code, timeout_seconds=timeout_seconds)
    return _format_result(result)


def main() -> None:
    logger.info("Starting mcp-sagemath-server with command: %s", _sage_command())
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
