# TODO Найдите количество книг, которое можно разместить на дискете
information_on_disket = 1.44 * 1024 *1024
count_of_pages = 100
count_of_lines = 50
count_of_symbols_on_lines = 25
bytes_for_one_symbol = 4
bytes_for_book = bytes_for_one_symbol * count_of_symbols_on_lines * count_of_lines * count_of_pages
count_of_diskets = information_on_disket / bytes_for_book
print("Количество книг, помещающихся на дискету:", round(count_of_diskets))
