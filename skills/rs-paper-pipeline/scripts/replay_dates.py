"""Explicit forced replay of dates, always without notifications."""
from datetime import datetime
import sys
from run_rs_daily_workday import main


def replay(value):
    dates = sorted(set(value.split(",")))
    if not 1 <= len(dates) <= 7:
        raise ValueError("Replay requires 1–7 dates")
    for date in dates:
        if len(date) != 8 or datetime.strptime(date, "%Y%m%d").strftime("%Y%m%d") != date:
            raise ValueError(f"Invalid replay date: {date}")
    failures = []
    for date in dates:
        try:
            main(target_date=date, notify=False, force=True)
        except Exception as exc:
            print(f"REPLAY FAILED {date}: {exc}", flush=True)
            failures.append(date)
    if failures:
        raise RuntimeError(f"Incomplete dates: {failures}")


if __name__ == "__main__":
    replay(sys.argv[1])
