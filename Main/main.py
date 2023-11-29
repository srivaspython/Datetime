import datetime

class MyDatetime:

    def __init__(self, year=None, month=None, day=None, hour=None, minute=None, second=None):
        """
        Creates a new Datetime object.

        Args:
            year (int): The year of the date.
            month (int): The month of the date (1-12).
            day (int): The day of the month (1-31).
            hour (int): The hour of the time (0-23).
            minute (int): The minute of the time (0-59).
            second (int): The second of the time (0-59).
        """

        if year is None and month is None and day is None and hour is None and minute is None and second is None:
            current_datetime = datetime.datetime.utcnow()
            self.year = current_datetime.year
            self.month = current_datetime.month
            self.day = current_datetime.day
            self.hour = current_datetime.hour
            self.minute = current_datetime.minute
            self.second = current_datetime.second
        else:
            self.year = year or 0
            self.month = month or 0
            self.day = day if day is not None else 0  # Only set day if provided
            self.hour = hour or 0
            self.minute = minute or 0
            self.second = second or 0

    @classmethod
    def from_iso8601(cls, iso8601_string):
        """
        Creates a Datetime object from an ISO 8601 formatted date and time string.

        Args:
            iso8601_string (str): The ISO 8601 formatted date and time string.

        Returns:
            Datetime: A Datetime object representing the specified date and time.
        """

        try:
            datetime_obj = datetime.datetime.fromisoformat(iso8601_string)
            return cls(datetime_obj.year, datetime_obj.month, datetime_obj.day,
                       datetime_obj.hour, datetime_obj.minute, datetime_obj.second)
        except ValueError:
            raise ValueError(f"Invalid ISO 8601 format: {iso8601_string}")

    @staticmethod
    def is_valid_date(year, month, day):
        """
        Checks whether the given set of date arguments (day, month, year) forms a valid date.

        Args:
            year (int): The year of the date.
            month (int): The month of the date (1-12).
            day (int): The day of the month (1-31).

        Returns:
            bool: True if the given date is valid, False otherwise.
        """

        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    def to_iso8601(self):
        return datetime.datetime(
            self.year, 
            self.month,
            self.day,
            self.hour,
            self.minute, 
            self.second
        ).isoformat()

    def to_human_readable(self):
        """
        Returns the Datetime object in a human-readable format.

        Returns:
            str: The human-readable formatted date and time string.
        """

        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

    @classmethod
    def validate_date(cls, year, month, day):
        """
        Class method to validate whether the given set of date arguments forms a valid date.

        Args:
            year (int): The year of the date.
            month (int): The month of the date (1-12).
            day (int): The day of the month (1-31).

        Returns:
            bool: True if the given date is valid, False otherwise.
        """
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        """
        Class method to calculate the difference between two dates.

        Args:
            date1 (Datetime): The first date.
            date2 (Datetime): The second date.
            unit (str): The unit for the difference ('days', 'weeks', 'months').

        Returns:
            int: The difference between the two dates in the specified unit.
        """
        if not isinstance(date1, cls) or not isinstance(date2, cls):
            raise ValueError("Both arguments must be instances of the Datetime class.")

        delta = abs(date1.to_datetime() - date2.to_datetime())

        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return delta.days // 30
            
    def __repr__(self):
        return f"Datetime(year={self.year}, month={self.month}, day={self.day}, " \
               f"hour={self.hour}, minute={self.minute}, second={self.second})"

    @classmethod
    def from_string(cls, date_string):
        """
        Class method to create a Datetime object from a date string.

        Args:
            date_string (str): The date string.

        Returns:
            Datetime: A Datetime object representing the specified date.
        """
        try:
            date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            return cls(date_obj.year, date_obj.month, date_obj.day,
                       date_obj.hour, date_obj.minute, date_obj.second)
        except ValueError:
            raise ValueError(f"Invalid date string format: {date_string}")

    @staticmethod
    def format_iso8601(date_obj):
        """
        Static method to format a Datetime object in ISO 8601 format.

        Args:
            date_obj (Datetime): The Datetime object.

        Returns:
            str: The ISO 8601 formatted date and time string.
        """
        return date_obj.to_iso8601()

    @staticmethod
    def format_human_readable(date_obj):
        """
        Static method to format a Datetime object in a human-readable format.

        Args:
            date_obj (Datetime): The Datetime object.

        Returns:
            str: The human-readable formatted date and time string.
        """
        return date_obj.to_human_readable()

    @staticmethod
    def convert_between_calendars(date_obj, from_calendar, to_calendar):
        
        pass

    @staticmethod
    def calculate_weekday(date_obj):
        """
        Static method to determine the day of the week for a given date.

        Args:
            date_obj (Datetime): The Datetime object.

        Returns:
            str: The day of the week.
        """
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[date_obj.to_datetime().weekday()]

    def to_datetime(self):
        """
        Returns the Datetime object as a datetime.datetime object.

        Returns:
            datetime.datetime: The datetime object.
        """
        return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)


# Example usage:

# Creating a Datetime object without arguments (defaults to current date and time)
datetime_obj_no_args = MyDatetime()
print(datetime_obj_no_args.to_human_readable())
print(datetime_obj_no_args.to_iso8601())

# Creating a Datetime object with arguments
datetime_obj_with_args = MyDatetime(2023, 11, 28, 15, 30, 45)
print(datetime_obj_with_args.to_human_readable())
print(datetime_obj_with_args.to_iso8601())

# Validating a date
print(MyDatetime.validate_date(2023, 11, 28))

# Calculating the difference between two dates
date1 = MyDatetime(2023, 11, 28)
date2 = MyDatetime(2023, 12, 5)
print(MyDatetime.date_difference(date1, date2, unit='days'))

# Creating a Datetime object from a date string
date_string = "2023-11-28 15:30:45"
print(MyDatetime.from_string(date_string))

# Formatting a Datetime object in ISO 8601 format
print(MyDatetime.format_iso8601(datetime_obj_with_args))

# Formatting a Datetime object in human-readable format
print(MyDatetime.format_human_readable(datetime_obj_with_args))

# Determining the day of the week for a given date
print(MyDatetime.calculate_weekday(datetime_obj_with_args))
