class Panel:
    DEFAULT_WIDTH = 44.7
    DEFAULT_HEIGHT = 71.1

    def __init__(self, x, y, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"(x = {self.x} , y = {self.y})"

class Rafter:
    def __init__(self, x):
        self.start_x = x

class Joint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class MountRules:
    EDGE_CLEARANCE = 2
    CANTILEVER_LIMIT = 16
    SPAN_LIMIT = 48

class JointRules:
    GAP_LIMIT = 1

class RafterRules:
    SPACING = 16