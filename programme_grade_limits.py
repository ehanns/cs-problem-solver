from collections import namedtuple

programme_grade_limits = []

ProgrammeGradeHourLimits = namedtuple('ProgrammeGradeHourMax', 'programme_type grade max_hour_limit_per_day min_hour_limit_per_day show_anytime')

programme_grade_limits.append(ProgrammeGradeHourLimits('FACTUAL', 0, 7, 5, True))
programme_grade_limits.append(ProgrammeGradeHourLimits('TRUE CRIME', 0, 5, 1, False))
programme_grade_limits.append(ProgrammeGradeHourLimits('REALITY', 0, 7, 5, True))
programme_grade_limits.append(ProgrammeGradeHourLimits('PARANORMAL', 0, 6, 5, False))
programme_grade_limits.append(ProgrammeGradeHourLimits('GAMESHOW/QUIZ', 0, 7, 5, True))
programme_grade_limits.append(ProgrammeGradeHourLimits('FACTUAL', 1, 7, 5, True,))
programme_grade_limits.append(ProgrammeGradeHourLimits('TRUE CRIME', 1, 6, 1, False))
programme_grade_limits.append(ProgrammeGradeHourLimits('REALITY', 1, 7, 5, True))
programme_grade_limits.append(ProgrammeGradeHourLimits('PARANORMAL', 1, 5, 1, False))
programme_grade_limits.append(ProgrammeGradeHourLimits('GAMESHOW/QUIZ', 1, 7, 1, True))
programme_grade_limits.append(ProgrammeGradeHourLimits('FACTUAL', 2, 7, 5, True))
programme_grade_limits.append(ProgrammeGradeHourLimits('TRUE CRIME', 2, 5, 1, False))
programme_grade_limits.append(ProgrammeGradeHourLimits('REALITY', 2, 7, 5, True))
programme_grade_limits.append(ProgrammeGradeHourLimits('PARANORMAL', 2, 5, 1, False))
programme_grade_limits.append(ProgrammeGradeHourLimits('GAMESHOW/QUIZ', 2, 7, 1, True))