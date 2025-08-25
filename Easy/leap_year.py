# leap_year.py
# Program to check if a given year is a leap year

def is_leap_year(year):
    """Return True if the given year is a leap year, False otherwise."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

    # Example usage:
if __name__ == "__main__":
    years = [1900, 2000, 2004, 2019, 2020]

    # Loop through each year
    for year in years:
        if is_leap_year(year):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")