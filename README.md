<h1 align="center">
  <br>
  <img src="imgs/zakuro.png">
</h1>
<p align="center">
  <a href="#modules">Modules</a> •
  <a href="#code-structure">Code structure</a> •
  <a href="#code-design">Code design</a> •
  <a href="#installing-the-application">Installing the application</a> •
  <a href="#taskfile-commands">Taskfile commands</a> •
  <a href="#environments">Environments</a> •
  <a href="#running-the-application">Running the application</a> •
  <a href="#changelog">Changelog</a>
</p>

ZakuroCache is a Python package that provides two high-level features:
- A simple decorator to identify the pure functions you want to cache.
- A caching system that never repeats twice the same execution and returns a cached result instead.

You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend ZakuroCache integration.

# Modules

At a granular level, ZakuroCache is a library that consists of the following components:

| Component | Description |
| ---- | --- |
| **zakuro_cache** | Contains the implementation of the caching system. |
| **zakuro_cache.loggers** | Captures stdout into an array during function execution. |
| **zakuro_cache.function** | Pipeline to execute, cache, and retrieve results. |

# Code structure

```
.
├── .pre-commit-config.yaml
├── Dockerfile
├── README.md
├── CHANGELOG.md
├── Taskfile.yml
├── taskfiles/
│   ├── build.yml
│   ├── development.yml
│   ├── docker.yml
│   └── python.yml
├── pyproject.toml
├── demo.py
├── docker.sh
├── imgs/
│   └── zakuro.png
└── zakuro_cache/
    ├── __init__.py
    ├── zakuro_cache.py
    ├── function/
    │   └── __init__.py
    └── loggers/
        └── __init__.py
```

# Code design

ZakuroCache uses a decorator-based approach to transparent function memoization:

1. The `@pure` decorator wraps any function to intercept its calls.
2. On each call, a unique hash is computed from the function name, module, arguments, and keyword arguments using MD5.
3. If the hash exists in the cache, the stored result is returned immediately without re-executing the function.
4. If not cached, the function executes inside a `Capturing` context manager that redirects stdout into a buffer, so both the return value and any printed output are stored together.
5. `ZakuroCache` is a simple in-memory dictionary-backed store with `get`/`set`/`set_logger` methods.

# Installing the application

### Prerequisites
- Python >= 3.6
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- Docker (optional, for containerized execution)

### Install with uv
```bash
uv pip install .
```

### Install with pip
```bash
pip install .
```

### Install in development mode
```bash
uv pip install -e .
```

### Docker
```bash
docker build . -t zakuro/zakuro-cache
```

# Taskfile commands

This project uses [Task](https://taskfile.dev/) as a task runner. Install it and run `task --list` to see all available commands.

| Command | Description |
| --- | --- |
| `task setup` | Install prerequisites and verify environment |
| `task help` | Show detailed help for all tasks |
| **Build** | |
| `task build:wheel` | Build wheel distribution with uv |
| `task build:sdist` | Build source distribution with uv |
| `task build:all` | Build wheel and source distribution |
| `task build:clean` | Remove dist directory |
| **Docker** | |
| `task docker:build` | Build the Docker image |
| `task docker:run` | Run demo in Docker with caching |
| `task docker:run-nocache` | Run demo in Docker without caching |
| `task docker:benchmark` | Full benchmark (cached vs uncached) |
| **Development** | |
| `task dev:install` | Install the package locally |
| `task dev:demo` | Run benchmark demo with caching |
| `task dev:demo-nocache` | Run benchmark demo without caching |
| `task dev:demo-compare` | Run both for comparison |
| **Python** | |
| `task python:build` | Build the Python package |
| `task python:install` | Install via setup.py |
| `task python:install-dev` | Install in development mode |
| `task python:deps` | Install dependencies |
| `task python:clean` | Remove build artifacts |

# Environments

| Variable | Default | Description |
| --- | --- | --- |
| `NTERMS` | `35` | Number of Fibonacci terms for the benchmark demo |
| `DOCKER_IMAGE` | `zakuro/zakuro-cache` | Docker image tag |

# Running the application

### Getting started

To apply the cache, add the `@pure` decorator to your functions:

```python
from zakuro_cache.function import pure

@pure
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        res1, res2 = recur_fibo(n - 1), recur_fibo(n - 2)
        return res1 + res2


if __name__ == "__main__":
    nterms = 35
    for i in range(nterms):
       print(recur_fibo(i))
```

### Performances

Run the benchmark locally:
```bash
python demo.py
```

Or via Docker:
```bash
task docker:benchmark
```

Expected output:
```
=====ZAKURO-CACHE=====
0.03user 0.00system 0:00.03elapsed 97%CPU (0avgtext+0avgdata 15444maxresident)k
0inputs+128outputs (0major+2493minor)pagefaults 0swaps


=====NO-CACHE=====
10.18user 0.00system 0:10.18elapsed 99%CPU (0avgtext+0avgdata 15568maxresident)k
496inputs+128outputs (3major+2491minor)pagefaults 0swaps
```

# Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed list of changes.
