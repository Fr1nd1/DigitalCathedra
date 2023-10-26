# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    part_1 = set(participants_first_group.split(delimiter))
    part_2 = set(participants_second_group.split(delimiter))
    common = list(part_1.intersection(part_2))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))