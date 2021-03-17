def determine_series(third_term, third_last_term, series_sum):
    series_length = 2 * series_sum / (third_term + third_last_term)

    #   Fix 0 / 0 case -> step size = 1
    if (2 * series_sum - 5 * (third_term + third_last_term) == (third_last_term**2 - third_term**2)):
        series_step = 1
    else:
        series_step = int((third_last_term** 2 - third_term ** 2) / (2 * series_sum - 5 * (third_term + third_last_term)))

    series_start = int(third_term - 2 * series_step)
    series_end = int(series_start + (series_length - 1) * series_step)
    print(series_length)
    print(series_step)
    if (series_step > 0):
        series = list(range(series_start, series_end+1, series_step))
    else:
        series = list(range(series_start, series_end-1, series_step))
    print(series)

determine_series(3, 6, 36) 
determine_series(3, 3, 15)  
determine_series(3, 55, 87)
