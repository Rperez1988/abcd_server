

def symbol_passed_pct(number_of_patterns, passed_abcds, failed_abcds):
    passed_pct = None
    if len(failed_abcds) == 0:
        passed_pct = 100

    if number_of_patterns == 0:

        passed_pct = 100
    elif len(failed_abcds) > 0:
        passed_pct = (len(passed_abcds) / number_of_patterns) * 100
    return passed_pct