def evaluate_locker(
    medicine_type,
    current_temp,
    storage_hours,
    door_open_count,
    sensor_readings
):
    if storage_hours < 0 or door_open_count < 0:
        return "INVALID_INPUT"

    if medicine_type == "COLD_CHAIN":
        min_temp = 2
        max_temp = 8
        max_hours = 72

    elif medicine_type == "ROOM_TEMP":
        min_temp = 15
        max_temp = 25
        max_hours = 168

    else:
        return "UNKNOWN_MEDICINE_TYPE"

    if current_temp < min_temp or current_temp > max_temp:
        status = "TEMP_ALERT"

    elif storage_hours > max_hours:
        status = "STORAGE_LIMIT"

    else:
        status = "SAFE"

    unstable_readings = 0

    for temperature in sensor_readings:
        if temperature < min_temp or temperature > max_temp:
            unstable_readings += 1

    if door_open_count > 5 and status == "SAFE":
        status = "ACCESS_WARNING"

    if unstable_readings >= 2 and status != "TEMP_ALERT":
        status = "QUARANTINE"

    return status