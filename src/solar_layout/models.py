class Panel:
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
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"(x = {self.x} , y = {self.y})"
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Mount) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Rafter:
    def __init__(self, x: float) -> None:
        self.start_x = x

class Joint:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"(x = {self.x} , y = {self.y})"
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Joint) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class MountRules:
    EDGE_CLEARANCE = 2
    CANTILEVER_LIMIT = 16
    SPAN_LIMIT = 48

class JointRules:
    GAP_LIMIT = 1

class RafterRules:
    SPACING = 16
