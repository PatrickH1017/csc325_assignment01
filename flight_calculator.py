def calculate_flight_time(weight_grams): 
    """
    Calculate active flight time in minutes for a given payload weight.

       Args:
           weight_grams (float): Payload weight in grams. Must be >= 0.

       Returns:
           float: Active flight time in minutes, using T(w) = 180 - 0.1w,
           floored at 0 if the formula would go negative.

       Raises:
           ValueError: If weight_grams is negative.
    """
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")
    
    flight_time = max(0, 180 - (0.1 * weight_grams)) 
    
    return flight_time

def flight_time_table(max_weight_grams, step_grams): 
    """
     Build a table of payload weight vs. active flight time.

    Args:
        max_weight_grams (float): The highest payload weight to include,
            in grams. Must be >= 0.
        step_grams (float): The increment between successive weights in
            the table, in grams. Must be > 0.

    Returns:
        list[tuple[float, float]]: A list of (weight, flight_time) pairs
        for weights from 0 up to and including max_weight_grams, spaced
        step_grams apart. Each flight_time value is produced by calling
        calculate_flight_time() rather than recomputing the formula.

    Raises:
        ValueError: If max_weight_grams is negative, or if step_grams is
            not positive.
    """
    if max_weight_grams < 0 or step_grams <= 0:
        raise ValueError("Max weight must be non-negative and step must be positive.")
    
    flight_times = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        flight_times.append((weight, flight_time))
    
    return flight_times
