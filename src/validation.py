
def validate_input(input_data):

    errors = []

    if not 0 <= input_data["sleep_hours"] <= 24:
        errors.append("Sleep hours must be between 0 and 24.")

    if input_data["screen_time_min"] < 0:
        errors.append("Screen time cannot be negative.")

    if input_data["hydration_l"] < 0:
        errors.append("Hydration cannot be negative.")

    if input_data["caffeine_mg"] < 0:
        errors.append("Caffeine intake cannot be negative.")

    if not 0 <= input_data["deep_sleep_pct"] <= 100:
        errors.append("Deep sleep percentage must be between 0 and 100.")

    return errors
