# solar-calculator

A Python application for calculating rafters, mounts and joints for a solar panel layout.

The program receives a list of panel top-left coordinates and returns calculated positions of:

- rafters,
- mounting points,
- joints between panels.

## Run the app
To run the example usage file:

```python
python examples/example_usage.py
```
### Example input
```python
[
    {"x": 0, "y": 0},
    {"x": 45.05, "y": 0},
    {"x": 90.1, "y": 0}
]
```

### Example output
```python
{
    "mounts": [...],
    "joints": [...],
    "rafters": [...]
}
```
## Run tests

To execute the test suite:

pytest
