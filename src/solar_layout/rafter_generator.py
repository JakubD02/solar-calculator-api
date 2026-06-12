from solar_layout.models import RafterRules

class RafterGenerator:
    SPACING = RafterRules.SPACING

    def generate_positions(self, start_x, min_x, max_x, spacing=SPACING):
        positions = []
        x = start_x
        while x < min_x:
            x += spacing

        while x <= max_x:
            positions.append(round(x, 2))
            x += spacing

        return positions

    def generate_candidates(self, panels, spacing=SPACING):
        min_x = panels[0].left_x
        max_x = panels[-1].right_x

        candidates = []
        for start_x in range(0, int(spacing) + 1):
            positions = self.generate_positions(start_x, min_x, max_x, spacing=spacing)
            candidates.append(positions)

        return candidates
