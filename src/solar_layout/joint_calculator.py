from solar_layout.models import JointRules, Joint

class JointCalculator:
    JOINT_GAP_LIMIT = JointRules.GAP_LIMIT

    def requires_joint(self, left_panel, right_panel):
        gap = right_panel.left_x - left_panel.right_x
        return 0 <= gap < self.JOINT_GAP_LIMIT

#             TL <-- top horizontal    --> TR
#  vert. left |                             | vertical right
#             BL <-- bottom horizontal --> BR
    def requires_grid_joint(self, top_left, top_right, bottom_left, bottom_right):
        top_horizontal_gap = top_right.left_x - top_left.right_x
        bottom_horizontal_gap = bottom_right.left_x - bottom_left.right_x

        vertical_gap_left = bottom_left.top_y - top_left.bottom_y
        vertical_gap_right = bottom_right.top_y - top_right.bottom_y

        return (0 <= top_horizontal_gap < self.JOINT_GAP_LIMIT
                and 0 <= bottom_horizontal_gap < self.JOINT_GAP_LIMIT
                and 0 <= vertical_gap_right < self.JOINT_GAP_LIMIT
                and 0 <= vertical_gap_left < self.JOINT_GAP_LIMIT
        )

    def create_joints_between_panels(self, left_panel, right_panel):
        joint_x = round((left_panel.right_x + right_panel.left_x) / 2, 2)

        top_y = round(left_panel.top_y, 2)
        bottom_y = round(left_panel.bottom_y, 2)

        return [
            Joint(joint_x, top_y),
            Joint(joint_x, bottom_y)
        ]

    def calculate_joints(self, rows):
        joints = []

        for row in rows:
            row = sorted(row, key=lambda panel: panel.left_x)
            for idx in range(len(row) - 1):
                left_panel = row[idx]
                right_panel = row[idx + 1]

                if self.requires_joint(left_panel, right_panel):
                    new_joints = self.create_joints_between_panels(
                        left_panel,
                        right_panel
                    )

                    joints.extend(new_joints)

        return joints