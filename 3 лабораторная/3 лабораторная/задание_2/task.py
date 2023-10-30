participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(participants_first_group, participants_second_group, separator=","):
    gr_1 = participants_first_group.split(separator)
    gr_2 = participants_second_group.split(separator)

    set_gr_1 = set(gr_1)
    set_gr_2 = set(gr_2)

    both_gr = set_gr_1.intersection(set_gr_2)
    straight_gr = sorted(list(both_gr))
    return straight_gr