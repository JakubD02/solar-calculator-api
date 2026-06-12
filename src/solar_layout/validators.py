from solar_layout.models import Panel

def panels_overlap(panel_1, panel_2):
    return (
        panel_1.left_x < panel_2.right_x
        and panel_1.right_x > panel_2.left_x
        and panel_1.top_y < panel_2.bottom_y
        and panel_1.bottom_y > panel_2.top_y
    )

def check_data_integrity(coords):
    if not isinstance(coords, list):
        raise TypeError("Coordinates must be a list OF POINTS")
    
    if not coords:
        raise ValueError("Coordinates cannot be empty")

    for idx, c in enumerate(coords):
        if not isinstance(c, dict):
            raise ValueError(f"Point {idx} must be a dict")
        
        if "x" not in c or "y" not in c:
            raise ValueError(f"Point {idx} must contain 'x' and 'y' values")

        if len(c) != 2:
            raise ValueError(f"Point {idx} must contain two values")

        if not isinstance(c["x"], (int, float)):
            raise ValueError(f"Point {idx} 'x' must contain only numbers")

        if not isinstance(c["y"], (int, float)):
            raise ValueError(f"Point {idx} 'y' must contain only numbers")
        
        panels = [Panel(c["x"], c["y"]) for c in coords]
        n = len(panels)

        for i in range(n):
            for j in range(i + 1, n):
                if panels_overlap(panels[i], panels[j]):
                    raise ValueError("Panels cannot overlap")

