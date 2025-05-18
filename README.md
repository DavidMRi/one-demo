# one-demo

**`one-demo`** is a minimal C++ project that exposes a simple function to Python using [SWIG](http://www.swig.org/), [CMake](https://cmake.org/), and [setuptools](https://setuptools.pypa.io/).

This repository demonstrates how to:

- Create a shared C++ library
- Generate Python bindings with SWIG
- Build and package the result for Python use

------

## Requirements

Before building the project, ensure the following dependencies are installed:

### System Requirements

- **CMake ≥ 3.22**
- **SWIG ≥ 4.0** (with Python support)
- **Python ≥ 3.6** (with `python3-dev` or equivalent)
- **A C++ compiler** (like `g++` or `clang++`)

### Python Packages

Used only if you want to install the generated Python package later:

```bash
pip install setuptools
```

------

## Building the Project

Run the provided `build.sh` script:

```bash
./build.sh
```

This script will:

1. Create a fresh `build/` directory
2. Configure the project with CMake
3. Build the C++ library (`libone`) and the SWIG Python wrapper
4. Prepare a minimal Python package inside `build/dist/one`

------

## Output

After running `build.sh`, the generated files will be located in:

```bash
build/
├── ...
├── dist/
│   └── one/
│       ├── one.py       # SWIG-generated Python module
│       ├── _one.so      # Compiled Python extension
│       ├── one.h        # C++ header (optional, for distribution)
│       └── setup.py     # Python packaging script
```

------

## Using from Python

To use the generated module directly without installation:

```python
# From inside build/dist/one
import one
print(one.func())  # should print: 1
```

Or to install it locally:

```bash
cd build/dist/one
pip install .
```

------

## Clean Build

To reset the build, just re-run:

```bash
./build.sh
```

This will delete the `build/` directory and rebuild everything from scratch.
