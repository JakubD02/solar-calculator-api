from solar_layout.models import Panel, JointRules
from solar_layout.joint_calculator import JointCalculator

JOINT_GAP_LIMIT = JointRules.GAP_LIMIT

def test_joint_is_required_when_horizontal_gap_is_less_than_configured_limit():
    calculator = JointCalculator()

    left_panel = Panel(0, 0)
    gap = JOINT_GAP_LIMIT / 2
    right_panel = Panel(left_panel.right_x + gap, 0)

    assert calculator.requires_joint(left_panel, right_panel) is True


def test_joint_is_not_required_when_horizontal_gap_is_greater_than_configured_limit():
    calculator = JointCalculator()

    left_panel = Panel(0, 0)
    gap = JOINT_GAP_LIMIT + 0.1
    right_panel = Panel(left_panel.right_x + gap, 0)

    assert calculator.requires_joint(left_panel, right_panel) is False


def test_joints_are_created_between_side_by_side_panels():
    calculator = JointCalculator()

    left_panel = Panel(0, 0)
    gap = JOINT_GAP_LIMIT / 2
    right_panel = Panel(left_panel.right_x + gap, 0)

    joints = calculator.create_joints_between_panels(left_panel, right_panel)

    expected_joint_x = round((left_panel.right_x + right_panel.left_x) / 2, 2)
    expected_top_y = round(left_panel.top_y, 2)
    expected_bottom_y = round(left_panel.bottom_y, 2)

    assert len(joints) == 2

    assert joints[0].x == expected_joint_x
    assert joints[0].y == expected_top_y

    assert joints[1].x == expected_joint_x
    assert joints[1].y == expected_bottom_y