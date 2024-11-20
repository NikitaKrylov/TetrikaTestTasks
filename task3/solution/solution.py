def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    # Функция для нахождения пересечения двух интервалов
    def intersection(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        return (start, end) if start < end else None  # Если нет пересечения, возвращаем None

    pupil_intervals = [(intervals['pupil'][i], intervals['pupil'][i + 1]) for i in range(0, len(intervals['pupil']), 2)]
    tutor_intervals = [(intervals['tutor'][i], intervals['tutor'][i + 1]) for i in range(0, len(intervals['tutor']), 2)]

    total_time = 0
    all_intervals = []

    # Для каждого интервала ученика, проверяем пересечение с уроком и учителем
    for p_start, p_end in pupil_intervals:
        for t_start, t_end in tutor_intervals:
            # Пересечение с уроком
            if intersection_with_lesson := intersection((lesson_start, lesson_end), (p_start, p_end)):
                # Пересечение ученика и учителя
                if intersection_with_both := intersection(intersection_with_lesson, (t_start, t_end)):
                    all_intervals.append(intersection_with_both)

    # Теперь вычисляем общее время присутствия, суммируя длительности всех уникальных интервалов
    if all_intervals:
        # Сортируем интервалы по времени начала
        all_intervals.sort()

        merged_intervals = []
        current_start, current_end = all_intervals[0]

        for start, end in all_intervals[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                merged_intervals.append((current_start, current_end))
                current_start, current_end = start, end

        # Добавляем последний интервал
        merged_intervals.append((current_start, current_end))
        total_time = sum(end - start for start, end in merged_intervals)

    return total_time


# Тесты
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

# Тестирование
if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
        print(f'{test_answer} {test['answer']}')
