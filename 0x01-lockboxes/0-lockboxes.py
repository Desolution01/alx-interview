#!/usr/bin/python3
"""
Pascal's Triangle
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    :param boxes: A list of lists representing boxes and keys.
    :type boxes: List[List[int]]
    :return: True if all boxes can be opened, else False.
    :rtype: bool
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # Mark the first box as visited
    queue = [0]  # Start from the first box

    while queue:
        current_box = queue.pop(0)

        # Check if the keys in the current box can unlock other boxes
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # If all boxes are visited, return True; otherwise, return False
    return all(visited)
