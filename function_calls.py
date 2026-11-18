# -*- coding: utf-8 -*-29
"""
Created on Mon Jun 28 15:26:21 2021

"""

new_linked_list = DoublyLinkedList()
new_linked_list.insert_in_emptylist(50)
new_linked_list.traverse_list()
new_linked_list.insert_at_start(10)
new_linked_list.insert_at_start(5)
new_linked_list.insert_at_start(18)
new_linked_list.traverse_list()
new_linked_list.insert_at_end(29)
new_linked_list.insert_at_end(39)
new_linked_list.insert_at_end(49)
new_linked_list.delete_element_by_value(5)
new_linked_list.traverse_list()
new_linked_list.insert_after_item(50, 65)
new_linked_list.traverse_list()
new_linked_list.insert_before_item(29, 100)
new_linked_list.traverse_list()
new_linked_list.delete_at_start()
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
new_linked_list.traverse_list()
new_linked_list.reverse_linked_list()
new_linked_list.traverse_list()

# for testing swap using first element
new_linked_list.swap_element(18,50)
new_linked_list.traverse_list()

# for testing swap using any element
new_linked_list.swap_element(18,29)
new_linked_list.traverse_list()