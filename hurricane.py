from Storm import Storm


class Hurricane(Storm):
    def __init__(self, name, wind_speed):
        super().__init__("none", wind_speed)

    def calculate_classification(self) -> str:
        if self.wind_speed in range(75,96):
            return "Category one"
        elif self.wind_speed in range(97,112):
            return "Category two"
        elif self.wind_speed in range(113,131):
            return "Category three"
        elif self.wind_speed in range(131,158):
            return "Category four"
        elif self.wind_speed > 157:
            return "Category five"
        return "Unclassified"

    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification in ["Tropical Storm", "Category one", "Category two"]:
            return "Close storm shutters and stay away from windows"
        elif classification == "Category three":
            return "Coastal regions are encouraged to evacuate"
        return "Evacuate"
