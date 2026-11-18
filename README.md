# Doubly Linked List Exercise

## Assignment 1 - PS4: Name Chain

This project is based on the Data Structures and Algorithms Design assignment
for the M.Tech (Data Science and Engineering) Work Integrated Learning
Programmes Division, Academic Year 2020-2021. The assignment is worth 12%.

### Problem

Represent a line of people with a doubly linked list, using one node per
person. Read commands from `inputPS4.txt`, apply them in order, and write the
space-separated state of the line after every command to `outputPS4.txt`.
Positions are one-based. An insertion position beyond the current line adds
the person at the end.

Supported command formats:

| Command | Meaning |
| --- | --- |
| `add_at_start::NAME` | Add `NAME` at the beginning |
| `add_at_end::NAME` | Add `NAME` at the end |
| `add_at_pos::POSITION::NAME` | Insert `NAME` at the specified position |
| `remove_people::COUNT::POSITION` | Remove `COUNT` people from the specified position |
| `flip_order::COUNT::POSITION` | Reverse the order of `COUNT` people from the specified position |

### Example

Input:

```text
add_at_start::Dave
add_at_end::Ricky
add_at_pos::2::Harry
add_at_pos::7::Adam
add_at_pos::1::Jerry
add_at_pos::2::Rob
flip_order::2::3
remove_people::2::1
```

Output:

```text
Dave
Dave Ricky
Dave Harry Ricky
Dave Harry Ricky Adam
Jerry Dave Harry Ricky Adam
Jerry Rob Dave Harry Ricky Adam
Jerry Rob Harry Dave Ricky Adam
Harry Dave Ricky Adam
```

### Requirements

- Implement the data structure and operations in Python 3.7.
- Use a doubly linked list; do not use Python dictionaries or external
  libraries for the implementation.
- Read and write the input and output files in the project root.
- Include basic error handling and an asymptotic runtime analysis in terms of
  the list size `n`.
- The assignment deliverables also include a design document, a contribution
  spreadsheet, the test input and output, and a single Python source file.

For a doubly linked list without a tail pointer, inserting at the start is
`O(1)`. Insertion at the end or at a position is `O(n)` due to traversal.
Removing `k` people or reversing `k` people from a given position is
`O(n + k)` when the list must first be traversed to that position.

### Files

- `DLL_code.py` and `DLL_code_ver001.py` contain doubly linked list code.
- `function_calls.py` contains example operation calls.
