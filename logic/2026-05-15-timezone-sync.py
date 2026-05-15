from datetime import datetime
import pytz

def sync_to_wat(dt_str, source_tz='UTC'):
    """Normalizes disparate timestamps to West Africa Time (WAT) for regional reporting."""
    source = pytz.timezone(source_tz)
    wat = pytz.timezone('Africa/Lagos')
/bin/bash: line 1: printf: `Y': invalid format character
    dt = datetime.strptime(dt_str, '