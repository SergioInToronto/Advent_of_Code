input_filename = __file__.split(".")[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split("\n")

reach_bustop_at = int(raw[0])
in_service_bus_routes = [int(x) for x in raw[1].split(",") if x != "x"]

earliest = {}
for bus in in_service_bus_routes:
    x = 0
    while x < reach_bustop_at:
        x += bus
    earliest[bus] = x

earliest_buses = sorted(earliest.items(), key=lambda x: x[1])
print(earliest_buses)

waiting_time = earliest_buses[0][1] - reach_bustop_at
print(waiting_time)
print(earliest_buses[0][0] * waiting_time)
