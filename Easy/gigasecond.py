'''The task: Given a date (with or without a specific time), compute the exact date and time that occurs 1 gigasecond later.

'''

from datetime import datetime , timedelta



def add_gigasecond(start_date):
    """
    Given a datetime object 'start_date',
    return the datetime that occurs exactly
    one gigasecond later.
    """
    giga_seconds = 1_000_000_000
    return(start_date + timedelta(seconds= giga_seconds))


#Example Usage
if __name__ =="__main__":
    birth_datetime = datetime(2015, 1, 24, 22, 0, 0)
    print(f"if gigaseconds add to this date {birth_datetime} the result is {add_gigasecond(birth_datetime)}")