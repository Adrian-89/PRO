class Plane:
    def __init__(
        self,
        gates: int,
        total_fuel: float,
        fuel_consumption: float,
        plane_model: str,
        passengers_capacity: int,
        travel_km: int,
        engine: bool = True,
        window_position: bool = True,
        plane_wheels: bool = True,
        plane_fly: bool = True,
    ):
        self.gates = gates
        self.total_fuel = total_fuel
        self.fuel_consumption = fuel_consumption
        self.plane_model = plane_model
        self.passengers_capacity = passengers_capacity
        self.engine = engine
        self.window_position = window_position
        self.plane_wheels = plane_wheels
        self.plane_fly = plane_fly
        self.travel_km = travel_km

    def num_gates(self):
        self.gates = 6

    def set_total_fuel(self, fuel_amount: float):
        self.total_fuel = fuel_amount

    def set_fuel_consumption(self, consumption: float):
        self.fuel_consumption = consumption

    def set_plane_model(self, model: str):
        self.plane_model = model

    def set_passengers_capacity(self, capacity: int):
        self.passengers_capacity = capacity

    def set_engine(self, engine: bool):
        if self.total_fuel > 0:
            self.engine = engine
        else:
            self.engine = False

    def set_window_position(self, position: bool):
        self.window_position = position

    def set_plane_wheels(self, has_wheels: bool):
        if self.plane_fly:
            self.plane_wheels = False
        else:
            self.plane_wheels = has_wheels

    def set_plane_fly(self):
        if self.total_fuel >= (self.fuel_consumption * self.travel_km):
            self.plane_fly = True
        else:
            self.plane_fly = False

    def travel_distance(self):
        self.travel_km

    def fuel_needed(self):
        self.fuel_consumption * self.travel_km
