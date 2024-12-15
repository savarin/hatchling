# hatchling

simple Python package example

## Quickstart

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate venv
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install ".[dev]"

# Run checks
chmod +x ./bin/test.sh
./bin/test.sh
```

## Project Structure

```
hatchling/
├── bin
│   └── test.sh
├── src
│   └── hatchling
│       ├── __init__.py
│       ├── data.py
│       └── test_data.py
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```
