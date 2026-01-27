# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed
- Migrated Python packaging from `setup.py` to `pyproject.toml` with `hatchling` build backend
- Updated `Dockerfile` to use `uv` for package installation
- Applied `isort` and `black` formatting to source files

### Added
- `.pre-commit-config.yaml` with `nbstripout`, `isort`, and `black` hooks
- `Taskfile.yml` with build, docker, development, and python task groups
- `pyproject.toml` with full project metadata and dev dependency group

### Removed
- `setup.py`, `packages.json`, and `requirements.txt` (replaced by `pyproject.toml`)

## [0.0.1] - Initial Release

### Added
- `ZakuroCache` in-memory caching system
- `@pure` decorator for automatic function memoization
- Stdout capture during cached function execution via `Capturing` logger
- Docker support with benchmark demo
- Fibonacci benchmark (`demo.py`) comparing cached vs uncached execution
