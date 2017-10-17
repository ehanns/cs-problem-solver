from __future__ import print_function

from ortools.constraint_solver import pywrapcp
from programme_grade_limits import programme_grade_limits
from operator import itemgetter
import calendar

# OBJECTIVE = MAXIMISE VIEWERSHIP FOR A GIVEN PROGRAMME K OF QUALITY X ON SLOT I ON DAY J

# BELOW ALGORITHM TAKEN FROM PAPER http://eprints.lancs.ac.uk/87877/1/2017haniphd.pdf
# THESIS DETAILS OPTIMISATION FOR TV SCHEDULES BASED ON INCREASING VIEWERSHIP PER PROGRAMME

# MODEL ASSUMPTIONS

# BASED ON ONE 24/7 CHANNEL THAT OFFERS FIVE GENRES OF PROGRAMMES OF DIFFERENT QUALITIES
# THREE MAIN QUALITIES OF PROGRAMMES (1,2,3) WHICH OFFER DIFFERENT RATES OF VIEWERSHIP RESPECTIVELY (15%, 10%, 5%)
# ONE TIME ZONE
# ONE COUNTRY
# ONE LANGUAGE
# FORECASTED VIEWERSHIP RATINGS AVAILABLE PER PROGRAMME
# EACH TIME SLOT ONLY TAKES ONE PROGRAMME TYPE/QUALITY ONLY.

# grades of programmes could be calculated based on: cost_of_production, popularity, guests, tech used.
# Viewers also tend to stick to the same programmes.

days_of_the_week_count = 7
programme_types = ['FACTUAL', 'TRUE CRIME', 'REALITY', 'PARANORMAL', 'GAMESHOW/QUIZ']
slots_per_day_count = 96
grades_of_programme_count = 3
grade_weightings = [0.2, 0.1, 0.05]
programme_weightings = [0.5, 0.3, 0.4, 0.7, 0.4]
total_amount_of_hours_per_genre = 45

start_index = 1


def main():
    solver = pywrapcp.Solver('schedule_programmes_viewership')

    days = range(start_index, days_of_the_week_count + 1)
    time_slots = range(start_index, slots_per_day_count + 1)
    grades_of_programme = range(0, grades_of_programme_count)
    total_slots_across_days = (days_of_the_week_count) * (slots_per_day_count)
    total_programme_grade_combinations = len(programme_types) * (grades_of_programme_count)
    total_possible_combo_count = total_slots_across_days * total_programme_grade_combinations

    # C(i,j,k,x) = Contrib of viewers to z if programme type of quality x is assigned to slot j on day i
    total_combos = get_total_contrib_of_viewers(total_possible_combo_count, days, time_slots, grades_of_programme,
                                                solver)

    optimised_slots = []
    total_viewership_count = 0

    # add constraint to only play genres that are show anytime before slot 64 per day
    show_anytime_cut_off = 64

    for day in days:
        for slot in time_slots:
            possible_programme_slots = [combo for combo in total_combos if combo[0] == day and combo[1] == slot]

            if slot <= show_anytime_cut_off:
                possible_programme_slots = remove_watershed_only_programmes(possible_programme_slots)

            sorted_programmes = sorted(possible_programme_slots, key=itemgetter(4), reverse=True)
            total_viewership_count += sorted_programmes[0][4]
            optimised_slots.append(sorted_programmes[0])

    for optimised_slot in optimised_slots:
        print('Day: %s ' % calendar.day_abbr[optimised_slot[0] - 1])
        print('Slot: %i,' % optimised_slot[1])
        print('Programme Type: %s' % programme_types[optimised_slot[2]])
        print('Grade: %i' % optimised_slot[3])
        print('Viewership: %i' % optimised_slot[4])

    print("Total Slots Filled out of 672: %i " % len(optimised_slots))
    print("Total Viewership Figures: %i " % total_viewership_count)


def get_total_contrib_of_viewers(total_possible_combo_count, days, time_slots, grades_of_programme, solver):
    total_contrib_of_viewers = {}

    for day in days:
        for slot in time_slots:
            for index, programme_type in enumerate(programme_types):
                for grade in grades_of_programme:
                    viewer_val = get_contrib_viewer_value(day, slot, index, grade)
                    total_contrib_of_viewers[(day, slot, index, grade, viewer_val)] = solver.IntVar(
                        0,
                        total_possible_combo_count,
                        "total_contrib_of_viewers(%i,%i,%i,%i,%i)" % (day, slot, index, grade, viewer_val)
                    )

    return total_contrib_of_viewers


def get_contrib_viewer_value(day, slot, programme_index, grade):
    # C(i, k, j, x) = P(i, j, k) * F(x) * POPULATION

    weighting = grade_weightings[grade]  # F(x)
    population = 100
    percentage_of_viewers = day * slot * (programme_weightings[programme_index])

    viewer_contrib_value = percentage_of_viewers * weighting * population

    return int(viewer_contrib_value)


def remove_watershed_only_programmes(possible_programmes_for_slot):
    anytime_programmes = []

    for programme in possible_programmes_for_slot:
        programme_type = programme_types[programme[2]]
        grade = programme[3]

        programme_limit = [programme_limit for programme_limit in programme_grade_limits if
                           programme_limit.programme_type == programme_type and programme_limit.grade == grade]

        if programme_limit[0].show_anytime is True:
            anytime_programmes.append(programme)

    return anytime_programmes


if __name__ == '__main__':
    main()
