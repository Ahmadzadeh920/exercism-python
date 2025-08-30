'''Input: Age in seconds.

Earth conversion:

1 Earth year = 365.25 days = 31,557,600 seconds.

Age in Earth years = seconds / 31_557_600.

Other planets:

Each planet has an orbital period relative to Earth.

Age on that planet = Earth age / orbital period.

Output:

Rounded to two decimal places.

Class Design:

Class SpaceAge with __init__ storing seconds.
'''

class SpaceAge:
    # Orbital periods relative to Earth
    orbital_periods = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    # Number of seconds in one Earth year
    EARTH_SECONDS = 31_557_600

    def __init__(self, seconds: float):
        self.seconds = seconds

    def _age_on_planet(self, planet: str) -> float:
        """
        Calculate age on a given planet.
        """
        if planet.lower() not in list(self.orbital_periods.keys()):
            raise ValueError("the name of planet doesnot exist")
        else:
            earth_years = self.seconds / self.EARTH_SECONDS
            planet_years = earth_years / self.orbital_periods[planet]
            return round(planet_years, 2)


# Exapmle Udage
if __name__ =="__main__":
    age_seconds = 1_000_000_000
    space_age = SpaceAge(age_seconds)
    test_cases =["neptune", "saturn" , "venus"]
    for test in test_cases:
        print(f"the age space of {test} is {space_age._age_on_planet(test)}")
