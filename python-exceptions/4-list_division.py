#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.
    :param my_list_1: First list of elements
    :param my_list_2: Second list of elements
    :param list_length: Number of elements to divide
    :return: A new list with the result of the divisions
    """
    result_list = []
    for i in range(list_length):
        try:
            # Essayer de diviser les éléments correspondants des deux listes
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
