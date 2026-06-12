from solar_layout.rafter_generator import RafterGenerator
from solar_layout.models import RafterRules

generator = RafterGenerator()
spacing = RafterRules.SPACING

def test_rafters_are_generated_every_configured_spacing_units():
    rafters = generator.generate_positions(
        start_x=0,
        min_x=0,
        max_x=spacing*3
    )

    assert rafters == [0, spacing, spacing*2, spacing*3]


def test_rafters_keep_configured_spacing():
    rafters = generator.generate_positions(
        start_x=0,
        min_x=0,
        max_x=spacing*6
    )

    for idx in range(len(rafters) - 1):
        assert rafters[idx + 1] - rafters[idx] == spacing