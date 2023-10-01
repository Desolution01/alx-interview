#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row as a list of lists.

    :param n: The number of rows to generate.
    :return: A list of lists representing Pascal's triangle.
    """
    pascal_triangle = []

    if n <= 0:
        return []

    for row_num in range(n):
        if row_num == 0:
            pascal_triangle.append([1])
        else:
            current_row = []
            for j in range(row_num + 1):
                if j == 0 or j == row_num:
                    current_row.append(1)
                else:
                    current_row.append(pascal_triangle[row_num - 1][j - 1] +
                                       pascal_triangle[row_num - 1][j])

            pascal_triangle.append(current_row)

    return pascal_triangle

if __name__ == "__main__":
    n = 5  # Number of rows
    result = pascal_triangle(n)
    for row in result:
        print("[{}]".format(",".join([str(x) for x in row])))
