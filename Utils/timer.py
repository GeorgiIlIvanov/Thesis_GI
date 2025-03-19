import time
import datetime

# Calculate total seconds for 136 hours
total_hours = 130
total_minutes = total_hours * 60
total_seconds = total_minutes * 60

# Get start time
start_time = time.time()
end_time = start_time + total_seconds

print(f"Starting 136-hour timer ({total_hours} hours)")
print(f"Start time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"End time: {datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}")
print("Timer will update every minute")
print("-" * 40)

# Output initial time remaining
remaining_seconds = total_seconds
hours, minutes = divmod(remaining_seconds // 60, 60)
print(f"Time remaining: {int(hours):02d}:{int(minutes):02d}")

# Wait for first minute interval
next_update = start_time + 60

try:
    while time.time() < end_time:
        # Sleep until next update time
        sleep_time = max(0, next_update - time.time())
        time.sleep(sleep_time)
        
        # Calculate time remaining
        elapsed_seconds = time.time() - start_time
        remaining_seconds = total_seconds - elapsed_seconds
        hours, minutes = divmod(remaining_seconds // 60, 60)
        
        # Output current time and time remaining in HH:MM format
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{current_time}] Time remaining: {int(hours):02d}:{int(minutes):02d}")
        
        # Set next update time (1 minute later)
        next_update = next_update + 60
        
    print("Timer complete!")
    
except KeyboardInterrupt:
    # Calculate final time if interrupted with Ctrl+C
    elapsed_seconds = time.time() - start_time
    remaining_seconds = total_seconds - elapsed_seconds
    hours, minutes = divmod(remaining_seconds // 60, 60)
    print(f"\nTimer interrupted. Time remaining: {int(hours):02d}:{int(minutes):02d}")
