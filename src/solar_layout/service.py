from solar_layout.validators import check_data_integrity
from solar_layout.grouping import create_panels, group_points_by_row
from solar_layout.rafter_generator import RafterGenerator
from solar_layout.mount_calculator import MountCalculator
from solar_layout.joint_calculator import JointCalculator

class SolarService:
    def __init__(self):
        self.rafter_generator = RafterGenerator()
        self.mount_calculator = MountCalculator()
        self.joint_calculator = JointCalculator()

    def sort_points(self, points):  
        return sorted(points, key=lambda point: (point.y, point.x))


    def points_to_dicts(self, points):
        return [
            {"x": point.x, "y": point.y}
            for point in points
        ]

    def calculator(self, coords):
        check_data_integrity(coords)

        panels = create_panels(coords)
        rows = group_points_by_row(panels)

        result = {
            "mounts": [],
            "joints": [],
        }

        for row in rows:
            rafters = self.rafter_generator.generate_candidates(row)

            for rafter in rafters:
                if self.mount_calculator.check_mounts_in_panels(row, rafter):
                    mounts = self.mount_calculator.create_mounts(row, rafter)
                    result["mounts"].extend(mounts)
                    break

        joints = self.joint_calculator.calculate_joints(rows)
        result["joints"].extend(joints)

        result["mounts"] = self.sort_points(result["mounts"])
        result["joints"] = self.sort_points(result["joints"])

        result["mounts"] = self.points_to_dicts(result["mounts"])
        result["joints"] = self.points_to_dicts(result["joints"])

        return result