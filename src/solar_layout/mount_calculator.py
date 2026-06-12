from solar_layout.models import MountRules, Mount

class MountCalculator:
    EDGE_CLEARANCE = MountRules.EDGE_CLEARANCE
    CANTILEVER_LIMIT = MountRules.CANTILEVER_LIMIT
    SPAN_LIMIT = MountRules.SPAN_LIMIT

    def get_panel_supports(self, panel, possible_support_x):
        panel_supports = []
        for x in possible_support_x:
            if panel.left_x + self.EDGE_CLEARANCE <= x <= panel.right_x - self.EDGE_CLEARANCE:
                panel_supports.append(x)

        return panel_supports

    def check_span_limit(self, supports):
        supports.sort()
        for idx in range(len(supports) - 1):
            if supports[idx + 1] - supports[idx] > self.SPAN_LIMIT:
                return False

        return True
    
    def check_cantilever_limit(self, panels, supports):
        panels = sorted(panels, key=lambda panel: panel.left_x)
        supports = sorted(set(supports)) # to remove duplicats

        if not supports:
            return False
        
        left_edge = panels[0].left_x
        right_edge = panels[-1].right_x

        first_support = supports[0]
        last_support = supports[-1]

        return first_support - left_edge <= self.CANTILEVER_LIMIT and right_edge - last_support <= self.CANTILEVER_LIMIT


    def check_mounts_in_panels(self, panels, rafter_x_positions):
        all_supports = []

        for panel in panels:
            panel_supports = self.get_panel_supports(panel, rafter_x_positions)

            if not panel_supports:
                return False

            if not self.check_span_limit(panel_supports):
                return False

            all_supports.extend(panel_supports)
        
        return self.check_cantilever_limit(panels, all_supports)

    def create_mounts(self, panels, rafter_x_positions):
        mounts = set()
        for panel in panels:
            panel_supports = self.get_panel_supports(panel, rafter_x_positions)
            for x in panel_supports:
                mounts.add(Mount(round(x, 2), round(panel.top_y, 2)))
                mounts.add(Mount(round(x, 2), round(panel.bottom_y, 2)))
        return mounts
