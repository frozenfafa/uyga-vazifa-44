class SpaceAircraft:
    def __init__(self,model: str,height: int,fuel: int,fuel_per_km = 5,fuel_to_land = 3):
        self.model = model
        self.height = height
        self.fuel = fuel
        self.fuel_per_km = fuel_per_km
        self.fuel_to_land = fuel_to_land
    def launch(self,km: int):
        if self.fuel - self.fuel_per_km * km < 0:
            print("Fuel is not enough")
        else:
            self.fuel -= self.fuel_per_km * km
            print(f"Launching was successful! Remaining fuel: {self.fuel}")
    def land(self,km: int):
        if self.fuel < self.fuel_to_land * km:
            print("NO FUEL for landing ! ! !")
        else:
            self.fuel -= self.fuel_to_land * km
            print(f"Landing was succesful! Remaining fuel: {self.fuel} litres")
    def info(self):
        print(f"""
Model:          {self.model}
Height:         {self.height}
Current fuel:   {self.fuel} litres
Fuel per km:    {self.fuel_per_km} litres
Fuel to land:   {self.fuel_to_land} litres
""")

class MinutesConverter:
    def __init__(self,minutes: int) -> int:
        self.minutes = minutes

    def toHours(self) -> int:
        return str(round(self.minutes / 60, 2))
    
    def toSeconds(self) -> int:
        return self.minutes * 60
    
    def toDays(self) -> int:
        return round(self.minutes / 1440, 2) 
