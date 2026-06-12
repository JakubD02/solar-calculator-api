from solar_layout.models import Panel, MountRules, RafterRules
from solar_layout.mount_calculator import MountCalculator

EDGE_CLEARANCE = MountRules.EDGE_CLEARANCE
SPAN_LIMIT = MountRules.SPAN_LIMIT
CANTILEVER_LIMIT = MountRules.CANTILEVER_LIMIT
RAFTER_SPACING = RafterRules.SPACING

def test_supports_can_only_be_placed_on_rafters():
    calculator = MountCalculator()
    panel = Panel(0, 0)

    rafter_x_positions = [
        panel.left_x,
        panel.left_x + EDGE_CLEARANCE,
        panel.left_x + panel.width / 2,
        panel.right_x - EDGE_CLEARANCE,
        panel.right_x,
        panel.right_x + RAFTER_SPACING
    ]

    supports = calculator.get_panel_supports(panel, rafter_x_positions)

    assert supports == [
        panel.left_x + EDGE_CLEARANCE,
        panel.left_x + panel.width / 2,
        panel.right_x - EDGE_CLEARANCE
    ]

    for support in supports:
        assert support in rafter_x_positions

def test_supports_are_not_closer_than_edge_clearance_from_panel_edges():
    calculator = MountCalculator()
    left_x, top_y = 0, 0
    panel = Panel(left_x, top_y)

    right_x = panel.right_x
    possible_supports = [
        left_x,
        left_x + EDGE_CLEARANCE - 0.01,
        left_x + EDGE_CLEARANCE,
        right_x - EDGE_CLEARANCE,
        right_x - EDGE_CLEARANCE + 0.01,
        right_x
    ]

    supports = calculator.get_panel_supports(panel, possible_supports)

    assert supports == [
        left_x + EDGE_CLEARANCE,
        right_x - EDGE_CLEARANCE
    ]


def test_span_limit_passes_when_distance_is_equal_or_less():
    calculator = MountCalculator()

    start_point = 2
    supports = [start_point, start_point + SPAN_LIMIT]

    assert calculator.check_span_limit(supports) is True


def test_span_limit_fails_when_distance_is_greater():
    calculator = MountCalculator()

    start_point = 2
    supports = [start_point, start_point + SPAN_LIMIT + 0.1]

    assert calculator.check_span_limit(supports) is False


def test_cantilever_limit_passes_when_first_and_last_support_are_close_enough():
    calculator = MountCalculator()
    left_x, top_y = 0, 0
    panel = Panel(left_x, top_y)

    right_x = panel.right_x
    panels = [panel]

    supports = [
        left_x + CANTILEVER_LIMIT,
        right_x - CANTILEVER_LIMIT
    ]

    assert calculator.check_cantilever_limit(panels, supports) is True


def test_cantilever_limit_fails_when_first_support_is_too_far_from_left_edge():
    calculator = MountCalculator()
    left_x, top_y = 0, 0
    panel = Panel(left_x, top_y)

    right_x = panel.right_x
    panels = [panel]

    supports = [
        left_x + CANTILEVER_LIMIT + 0.1,
        right_x - CANTILEVER_LIMIT
    ]

    assert calculator.check_cantilever_limit(panels, supports) is False


def test_cantilever_limit_fails_when_last_support_is_too_far_from_right_edge():
    calculator = MountCalculator()
    left_x, top_y = 0, 0
    panel = Panel(left_x, top_y)

    right_x = panel.right_x
    panels = [panel]

    supports = [
        left_x + CANTILEVER_LIMIT,
        right_x - CANTILEVER_LIMIT - 0.1
    ]

    assert calculator.check_cantilever_limit(panels, supports) is False