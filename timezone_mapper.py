import pytz
from datetime import datetime

def get_local_time(timezone_str):
    """
    Maps lead location to local time for optimized RevOps outreach.
    Financial Pivot Law: Timing is everything in high-stakes deal closure.
    """
    try:
        tz = pytz.timezone(timezone_str)
        return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return "Unknown Timezone"

if __name__ == "__main__":
    print(f"Lagos Time: {get_local_time('Africa/Lagos')}")
