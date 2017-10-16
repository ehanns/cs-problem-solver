from collections import namedtuple

programme_grade_limits = []

ProgrammeGradeHourLimits = namedtuple('ProgrammeGradeHourMax', 'programme_type grade max_hour_limit min_hour_limit '
                                                               'index_ref')

programme_grade_limits.append(ProgrammeGradeHourLimits('FACTUAL', 1, 100, 20, 0))
programme_grade_limits.append(ProgrammeGradeHourLimits('TRUE CRIME', 1, 30, 20, 1))
programme_grade_limits.append(ProgrammeGradeHourLimits('REALITY', 1, 50, 20, 2))
programme_grade_limits.append(ProgrammeGradeHourLimits('PARANORMAL', 1, 70, 20, 3))
programme_grade_limits.append(ProgrammeGradeHourLimits('GAMESHOW/QUIZ', 1, 40, 20, 4))
programme_grade_limits.append(ProgrammeGradeHourLimits('FACTUAL', 2, 100, 200, 0))
programme_grade_limits.append(ProgrammeGradeHourLimits('TRUE CRIME', 2, 30, 20, 1))
programme_grade_limits.append(ProgrammeGradeHourLimits('REALITY', 2, 50, 20, 2))
programme_grade_limits.append(ProgrammeGradeHourLimits('PARANORMAL', 2, 70, 20, 3))
programme_grade_limits.append(ProgrammeGradeHourLimits('GAMESHOW/QUIZ', 2, 40, 20, 4))
programme_grade_limits.append(ProgrammeGradeHourLimits('FACTUAL', 3, 100, 20, 0))
programme_grade_limits.append(ProgrammeGradeHourLimits('TRUE CRIME', 3, 30, 20, 1))
programme_grade_limits.append(ProgrammeGradeHourLimits('REALITY', 3, 50, 20, 2))
programme_grade_limits.append(ProgrammeGradeHourLimits('PARANORMAL', 3, 70, 20, 3))
programme_grade_limits.append(ProgrammeGradeHourLimits('GAMESHOW/QUIZ', 3, 40, 20, 4))