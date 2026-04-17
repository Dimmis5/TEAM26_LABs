# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:21:41 2026

@author: turet
"""

import random
from typing import List, Tuple


def midpoint_displacement(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    roughness: float,
    depth: int
) -> List[Tuple[float, float]]:
    if depth < 0:
        raise ValueError("depth must be >= 0")
    if roughness < 0:
        raise ValueError("roughness must be >= 0")

    if depth == 0:
        return [(x1, y1), (x2, y2)]

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    mx += roughness * random.uniform(-1, 1)
    my += roughness * random.uniform(-1, 1)

    left_points = midpoint_displacement(x1, y1, mx, my, roughness / 2, depth - 1)
    right_points = midpoint_displacement(mx, my, x2, y2, roughness / 2, depth - 1)

    return left_points[:-1] + right_points


def generate_terrain(width: int, height: int, roughness: float, depth: int) -> List[List[float]]:
    if width < 2 or height < 2:
        raise ValueError("width and height must be >= 2")
    if depth < 0:
        raise ValueError("depth must be >= 0")
    if roughness < 0:
        raise ValueError("roughness must be >= 0")

    grid = [[0.0 for _ in range(height)] for _ in range(width)]

    grid[0][0] = 0.0
    grid[0][height - 1] = 0.0
    grid[width - 1][0] = 0.0
    grid[width - 1][height - 1] = 0.0

    diamond_square(grid, 0, 0, width - 1, height - 1, roughness, depth)
    return grid


def diamond_square(
    grid: List[List[float]],
    x: int,
    y: int,
    width: int,
    height: int,
    roughness: float,
    depth: int
) -> None:
    if width <= 1 or height <= 1 or depth == 0:
        return

    widthhalf = width // 2
    heighthalf = height // 2

    if widthhalf == 0 or heighthalf == 0:
        return

    center_x = x + widthhalf
    center_y = y + heighthalf

    grid[center_x][center_y] = (
        grid[x][y]
        + grid[x + width][y]
        + grid[x][y + height]
        + grid[x + width][y + height]
    ) / 4 + random.uniform(-roughness, roughness)

    grid[center_x][y] = (
        grid[x][y] + grid[x + width][y]
    ) / 2 + roughness * random.uniform(-1, 1)

    grid[x][center_y] = (
        grid[x][y] + grid[x][y + height]
    ) / 2 + roughness * random.uniform(-1, 1)

    grid[x + width][center_y] = (
        grid[x + width][y] + grid[x + width][y + height]
    ) / 2 + roughness * random.uniform(-1, 1)

    grid[center_x][y + height] = (
        grid[x][y + height] + grid[x + width][y + height]
    ) / 2 + roughness * random.uniform(-1, 1)

    diamond_square(grid, x, y, widthhalf, heighthalf, roughness / 2, depth - 1)
    diamond_square(grid, center_x, y, widthhalf, heighthalf, roughness / 2, depth - 1)
    diamond_square(grid, x, center_y, widthhalf, heighthalf, roughness / 2, depth - 1)
    diamond_square(grid, center_x, center_y, widthhalf, heighthalf, roughness / 2, depth - 1)


def detect_artifacts(terrain_grid: List[List[float]], threshold: float) -> List[Tuple[int, int]]:
    if not terrain_grid or not terrain_grid[0]:
        return []
    if threshold < 0:
        raise ValueError("threshold must be >= 0")

    width = len(terrain_grid)
    height = len(terrain_grid[0])

    for row in terrain_grid:
        if len(row) != height:
            raise ValueError("terrain_grid must be rectangular")

    tab = []

    for i in range(width - 1):
        for j in range(height - 1):
            if abs(terrain_grid[i][j] - terrain_grid[i + 1][j]) > threshold:
                tab.append((i, j))
            elif abs(terrain_grid[i][j] - terrain_grid[i][j + 1]) > threshold:
                tab.append((i, j))

    return tab


if __name__ == "__main__":
    random.seed(42)

    print("EDGE CASES midpoint_displacement")
    print(midpoint_displacement(0, 0, 10, 10, 0, 0))
    print(len(midpoint_displacement(0, 0, 10, 0, 1, 1)))
    print(len(midpoint_displacement(5, 5, 5, 5, 1, 3)))

    try:
        midpoint_displacement(0, 0, 10, 10, -1, 3)
    except ValueError as e:
        print(e)

    try:
        midpoint_displacement(0, 0, 10, 10, 1, -1)
    except ValueError as e:
        print(e)

    print("\nEDGE CASES generate_terrain")
    t1 = generate_terrain(2, 2, 0, 0)
    print(t1)

    t2 = generate_terrain(5, 5, 0, 3)
    print(t2)

    try:
        generate_terrain(1, 5, 1, 3)
    except ValueError as e:
        print(e)

    try:
        generate_terrain(5, 5, -1, 3)
    except ValueError as e:
        print(e)

    try:
        generate_terrain(5, 5, 1, -1)
    except ValueError as e:
        print(e)

    print("\nEDGE CASES detect_artifacts")
    print(detect_artifacts([], 1))
    print(detect_artifacts([[0]], 1))
    print(detect_artifacts([[0, 0], [0, 10]], 5))
    print(detect_artifacts([[1, 1], [1, 1]], 0))

    try:
        detect_artifacts([[1, 2], [3]], 1)
    except ValueError as e:
        print(e)

    try:
        detect_artifacts([[1, 2], [3, 4]], -1)
    except ValueError as e:
        print(e)