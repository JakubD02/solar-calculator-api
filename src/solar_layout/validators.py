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
