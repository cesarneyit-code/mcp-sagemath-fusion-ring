#!/usr/bin/env node
"use strict";

const { spawn } = require("node:child_process");

const uvx = process.env.UVX_BIN || "uvx";
const args = ["mcp-sagemath-fusion-rings", ...process.argv.slice(2)];

const child = spawn(uvx, args, {
  stdio: "inherit",
  env: process.env,
});

child.on("error", (err) => {
  console.error(
    "[mcp-sagemath-fusion-rings] Failed to launch uvx.\n" +
      "Install uv first: https://docs.astral.sh/uv/\n" +
      `Details: ${err.message}`
  );
  process.exit(1);
});

child.on("exit", (code, signal) => {
  if (signal) {
    process.kill(process.pid, signal);
    return;
  }
  process.exit(code === null ? 1 : code);
});
