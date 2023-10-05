#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start from the first box

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        # Check if the keys in the current box can unlock other boxes
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                stack.append(key)

    # If all boxes are visited, return True; otherwise, return False
    return all(visited)

