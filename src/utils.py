from datetime import datetime, timezone, date, timedelta

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def utc_timestamp() -> int:
    return int(utc_now().timestamp())

def utc_timestamp_micros() -> int:
    return int(utc_now().timestamp() * 1000000)

def utc_date_str() -> str:
    return str(utc_now().date())




def daterange_timestamps(start_date: date, end_date: date):
    """Yields pairs (start_of_day, start_of_next_day) in ms."""
    epoch = date(1970, 1, 1)
    for n in range(int((end_date - start_date).days) + 1):
        current_day = start_date + timedelta(n)
        next_day = current_day + timedelta(1)
        
        ts_start = int((current_day - epoch).total_seconds() * 1000)
        ts_end = int((next_day - epoch).total_seconds() * 1000)
        yield ts_start, ts_end

# 2. For Facebook (Strings)
def daterange_strings(start_date: date, end_date: date):
    """Yields date in 'YYYY-MM-DD' format."""
    for n in range(int((end_date - start_date).days) + 1):
        yield str(start_date + timedelta(n))