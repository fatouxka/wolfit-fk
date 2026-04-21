
import pytest
from datetime import datetime, timedelta
from app.helpers import pretty_date, less_than_day

def test_less_than_day_just_now():
    assert less_than_day(5) == "just now"
    assert less_than_day(9) == "just now"
    assert less_than_day(10) == "10 seconds ago"

def test_less_than_day_minute():
    assert less_than_day(60) == "a minute ago"
    assert less_than_day(61) == "a minute ago"
    assert less_than_day(119) == "a minute ago"

def test_less_than_day_minutes():
    assert less_than_day(120) == "2 minutes ago"
    assert less_than_day(300) == "5 minutes ago"
    assert less_than_day(3599) == "59 minutes ago"

def test_less_than_day_hour():
    assert less_than_day(3600) == "an hour ago"
    assert less_than_day(3610) == "an hour ago"
    assert less_than_day(7199) == "an hour ago"

def test_less_than_day_hours():
    assert less_than_day(7200) == "2 hours ago"
    assert less_than_day(10800) == "3 hours ago"
    assert less_than_day(86399) == "23 hours ago"

def test_pretty_date_int_timestamp():
    now = datetime.utcnow()
    timestamp = int(now.timestamp())
    result = pretty_date(timestamp)
    assert result in ["just now", "5 seconds ago", "10 seconds ago"]

def test_pretty_date_datetime():
    now = datetime.utcnow()
    result = pretty_date(now)
    assert result == "just now"

def test_pretty_date_future():
    future = datetime.utcnow() + timedelta(hours=1)
    result = pretty_date(future)
    assert result == "just now"

def test_pretty_date_invalid():
    result = pretty_date("invalid")
    assert result == "just now"

def test_pretty_date_seconds_ago():
    past = datetime.utcnow() - timedelta(seconds=30)
    result = pretty_date(past)
    assert result in ["30 seconds ago", "just now"]

def test_pretty_date_minutes_ago():
    past = datetime.utcnow() - timedelta(minutes=5)
    result = pretty_date(past)
    assert result == "5 minutes ago"

def test_pretty_date_hours_ago():
    past = datetime.utcnow() - timedelta(hours=3)
    result = pretty_date(past)
    assert result == "3 hours ago"

def test_pretty_date_days_ago():
    past = datetime.utcnow() - timedelta(days=2)
    result = pretty_date(past)
    assert result == "2 days ago"

def test_pretty_date_weeks_ago():
    past = datetime.utcnow() - timedelta(days=14)
    result = pretty_date(past)
    assert result == "2 weeks ago"

def test_pretty_date_months_ago():
    past = datetime.utcnow() - timedelta(days=60)
    result = pretty_date(past)
    assert result == "2 months ago"

def test_pretty_date_years_ago():
    past = datetime.utcnow() - timedelta(days=730)
    result = pretty_date(past)
    assert result == "2 years ago"

def test_pretty_date_one_week_ago():
    past = datetime.utcnow() - timedelta(days=7)
    result = pretty_date(past)
    assert result == "1 week ago"

def test_pretty_date_one_month_ago():
    past = datetime.utcnow() - timedelta(days=30)
    result = pretty_date(past)
    assert result == "4 weeks ago"

def test_pretty_date_one_year_ago():
    past = datetime.utcnow() - timedelta(days=365)
    result = pretty_date(past)
    assert result == "1 year ago"
def test_pretty_date_invalid_input():
    from app.helpers import pretty_date
    assert pretty_date(None) == 'just now'
    assert pretty_date("invalid") == 'just now'
    assert pretty_date(123) != ''
def test_pretty_date_with_none_timestamp():
    from app.helpers import pretty_date
    result = pretty_date(None)
    assert result == 'just now'

def test_pretty_date_with_string_timestamp():
    from app.helpers import pretty_date
    result = pretty_date('invalid')
    assert result == 'just now'
