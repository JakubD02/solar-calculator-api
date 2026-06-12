# solar-calculator

A Python application for calculating mounts and joints for a solar panel layout.

The program receives a list of panel top-left coordinates and returns calculated positions of:

- **mounting points** - calculated mounting points locations,
- **joints** - calculated joints between adjacent panels.

Each returned item contains coordinates (x, y).

## Requirements:
- Python 3.10 or newer
- pip

## Setup

```python
git clone https://github.com/JakubD02/solar-calculator.git 
cd solar-calculator
```

Create and activate a virtual environment.

On Windows PowerShell:

```python
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On macOS/Linux:

```python
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```python
pip install -r requirements.txt
```

Install the project in editable mode:
```python
pip install -e .
```

## Run the App

To run the example usage file:

```python
python examples/example_usage.py
```
### Example input
```json
[
    {"x": 0, "y": 0},
    {"x": 45.05, "y": 0},
    {"x": 90.1, "y": 0}
]
```

### Example output
```json
{
    "mounts": [
        {"x": 16, "y": 0},
        {"x": 32, "y": 0}    
    ],

    "joints": [
        {"x": 44.88, "y": 0},
        {"x": 44.88, "y": 71.1}
    ]
}
```

## Run Tests

To execute the test suite:

pytest

Test verify:
- input validation,
- rafter generation,
- mount placement rules,
- joint calculation,
- main service flow.


