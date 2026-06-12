from solar_layout.service import SolarService
import json

example_input = [
 {"x": 0, "y": 0}, {"x": 45.05, "y": 0}, {"x": 90.1, "y": 0},
 {"x": 0, "y": 71.6}, {"x": 135.15, "y": 0}, {"x": 135.15, "y": 71.6},
 {"x": 0, "y": 143.2}, {"x": 45.05, "y": 143.2}, {"x": 135.15, "y": 143.2},
 {"x": 90.1, "y": 143.2}
]

service = SolarService()
result = service.calculator(example_input)

def print_points(title, points):
    print(f"\n{title}:")

    for point in points:
        print(f"  x = {point["x"]}, y = {point["y"]}")


service = SolarService()
result = service.calculator(example_input)

print(json.dumps(result, indent=1))

# print_points("MOUNTS", result["mounts"])
# print_points("JOINTS", result["joints"])