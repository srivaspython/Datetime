import datetime
import pytest
from main import MyDatetime  

def test_datetime_creation_no_args():
    current_datetime = MyDatetime()
    print("Current datetime:", current_datetime)
    
    datetime_obj_no_args = MyDatetime()
    print("Datetime object:", datetime_obj_no_args)
    
    assert isinstance(datetime_obj_no_args, MyDatetime)
    assert datetime_obj_no_args.year == current_datetime.year
    assert datetime_obj_no_args.month == current_datetime.month
    assert datetime_obj_no_args.day == current_datetime.day
    assert datetime_obj_no_args.hour == current_datetime.hour
    assert datetime_obj_no_args.minute == current_datetime.minute
    assert datetime_obj_no_args.second == current_datetime.second



def test_datetime_creation_with_args():
    datetime_obj_with_args = MyDatetime(2023, 11, 28, 15, 30, 45)
    assert isinstance(datetime_obj_with_args, MyDatetime)
    assert datetime_obj_with_args.year == 2023
    assert datetime_obj_with_args.month == 11
    assert datetime_obj_with_args.day == 28
    assert datetime_obj_with_args.hour == 15
    assert datetime_obj_with_args.minute == 30
    assert datetime_obj_with_args.second == 45

def test_from_iso8601_valid():
    iso8601_string = "2023-11-28T15:30:45"
    datetime_obj = MyDatetime.from_iso8601(iso8601_string)
    assert isinstance(datetime_obj, MyDatetime)
    assert datetime_obj.year == 2023
    assert datetime_obj.month == 11
    assert datetime_obj.day == 28
    assert datetime_obj.hour == 15
    assert datetime_obj.minute == 30
    assert datetime_obj.second == 45

def test_from_iso8601_invalid():
    invalid_iso8601_string = "invalid"
    with pytest.raises(ValueError):
        MyDatetime.from_iso8601(invalid_iso8601_string)

def test_is_valid_date_valid():
    assert MyDatetime.is_valid_date(2023, 11, 28)

def test_is_valid_date_invalid():
    assert not MyDatetime.is_valid_date(2023, 13, 28)

def test_to_iso8601():
    datetime_obj = MyDatetime(2023, 11, 28, 15, 30, 45)
    iso8601_string = datetime_obj.to_iso8601()
    assert iso8601_string == "2023-11-28T15:30:45"

def test_to_human_readable():
    datetime_obj = MyDatetime(2023, 11, 28, 15, 30, 45)
    human_readable_string = datetime_obj.to_human_readable()
    assert human_readable_string == "2023-11-28 15:30:45"
