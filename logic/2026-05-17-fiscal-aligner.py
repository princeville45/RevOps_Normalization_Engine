from datetime import datetime

def align_to_fiscal_year(date_obj, start_month=7):
    """Maps a calendar date to a fiscal year (e.g., FY starts in July)."""
    if date_obj.month >= start_month:
        return f"FY{date_obj.year + 1}"
    return f"FY{date_obj.year}"