"""Domain models representing physical elements of the solar panel layout:
panels, mounting rules, and connector positions (mounts, joints).
"""

class Panel:
    """A single solar panel defined by its top-left corner and fixed dimensions."""
    
    DEFAULT_WIDTH = 44.7
    DEFAULT_HEIGHT = 71.1

    def __init__(self, x: float, y: float, width: float=DEFAULT_WIDTH, height: float=DEFAULT_HEIGHT) -> None:
        self.left_x = x
        self.top_y = y
        self.width = width
        self.height = height

    @property
    def right_x(self) -> float:
        return self.left_x + self.width

    @property
    def bottom_y(self) -> float:
        return self.top_y + self.height

class Mount:
    """A support point where the panel attaches to a rafter."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"(x = {self.x} , y = {self.y})"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Mount) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Rafter:
    def __init__(self, x: float) -> None:
        self.start_x = x

class Joint:
    """A connector point joining two or more adjacent panels."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"(x = {self.x} , y = {self.y})"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Joint) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class MountRules:
    """Business constraints for support placement (edge clearance, span, cantilever)."""

    EDGE_CLEARANCE: float = 2
    CANTILEVER_LIMIT: float = 16
    SPAN_LIMIT: float = 48

class JointRules:
    """Business constraints for joint placement between panels."""

    GAP_LIMIT = 1

class RafterRules:
    """Business constraints for rafter placement."""

    SPACING = 16
