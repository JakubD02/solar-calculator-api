from solar_layout.models import Panel

def create_panels(coords: list[dict[str, float]]) -> list[Panel]:
    panels = []
    for c in coords:
        panels.append(Panel(c["x"], c["y"]))

    return panels

def sort_key(panel: Panel) -> tuple[float, float]:
    return panel.top_y, panel.left_x

def group_points_by_row(panels: list[Panel]) -> list[list[Panel]]:
    panels.sort(key=sort_key)

    grouped_coords = []
    current_row = []
    current_y = panels[0].top_y

    for p in panels:
        if p.top_y  != current_y:
            grouped_coords.append(current_row)
            current_row = []
            current_y = p.top_y
        current_row.append(p)

    grouped_coords.append(current_row)
    return grouped_coords