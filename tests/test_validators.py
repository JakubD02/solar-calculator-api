import pytest
from solar_layout.validators import check_data_integrity
from solar_layout.models import Panel

PANEL_WIDTH = Panel.DEFAULT_WIDTH
PANEL_HEIGHT = Panel.DEFAULT_HEIGHT

def test_valid_coordinates_pass_validation():
    coords = [
        {"x": 0, "y": 0},
        {"x": PANEL_WIDTH + 0.35, "y": 0},
        {"x": 0, "y": PANEL_HEIGHT + 0.5}
    ]

    check_data_integrity(coords)

def test_missing_y_coordinate_raises_error():
    coords = [
        {"x": 0}
    ]

    with pytest.raises(ValueError):
        check_data_integrity(coords)

def test_empty_coordinates_raise_error():
    with pytest.raises(ValueError):
        check_data_integrity([])


def test_non_numeric_coordinate_raises_error():
    coords = [
        {"x": "abc", "y": 0}
    ]

    with pytest.raises(ValueError):
        check_data_integrity(coords)

def test_wrong_coordinate_names_raise_error():
    coords = [
        {"left": 0, "top": 0}
    ]

    with pytest.raises(ValueError):
        check_data_integrity(coords)

def test_overlapping_panels_raise_error():
    coords = [
        {"x": 0, "y": 0},
        {"x": PANEL_WIDTH / 2, "y": 0}
    ]

    with pytest.raises(ValueError):
        check_data_integrity(coords)

def test_reversed_x_y_order_passes_validation():
    coords = [
        {"y": 0, "x": 0}
    ]

    check_data_integrity(coords)