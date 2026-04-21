from app.helpers import less_than_day, pretty_date
from datetime import datetime, timedelta

def test_pretty_date_future_date():
    future = datetime.now() + timedelta(days=1)
    result = pretty_date(future)
    assert result is not None

def test_less_than_day_boundary():
    assert less_than_day(1) == 'just now'
    assert less_than_day(59) == '59 seconds ago'
    assert less_than_day(60) == 'a minute ago'
