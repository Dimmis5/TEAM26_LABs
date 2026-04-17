# 1. Implementation of split_region
def split_region(x, y, width, height, min_size):
    if width <= min_size or height <= min_size:
        return
    
    half_w = width / 2
    half_h = height / 2
    
    split_region(x, y, half_w, half_h, min_size)
    split_region(x + half_w, y, half_w, half_h, min_size)
    split_region(x, y + half_h, half_w, half_h, min_size)
    split_region(x + half_w, y + half_h, half_w, half_h, min_size)

# 2. Implementation of count_points_in_region
def count_points_in_region(points, region):
    count = 0
    rx, ry = region['x'], region['y']
    rw, rh = region['width'], region['height']
    
    for px, py in points:
        if rx <= px < rx + rw and ry <= py < ry + rh:
            count += 1
    return count

# 3. Implementation of find_dense_regions
def find_dense_regions(points, x, y, width, height, min_size, density_threshold):
    current_region = {'x': x, 'y': y, 'width': width, 'height': height}
    num_points = count_points_in_region(points, current_region)
    
    area = width * height
    density = num_points / area if area > 0 else 0

    if width <= min_size or height <= min_size:
        if density > density_threshold:
            return [current_region]
        return []
    
    half_w = width / 2
    half_h = height / 2
    dense_regions = []

    dense_regions += find_dense_regions(points, x, y, half_w, half_h, min_size, density_threshold)
    dense_regions += find_dense_regions(points, x + half_w, y, half_w, half_h, min_size, density_threshold)
    dense_regions += find_dense_regions(points, x, y + half_h, half_w, half_h, min_size, density_threshold)
    dense_regions += find_dense_regions(points, x + half_w, y + half_h, half_w, half_h, min_size, density_threshold)
    
    return dense_regions

# Test avec des données manuelles
my_points = [
    (5, 5), (2, 3), (8, 7), (1, 1), (4, 4),
    (80, 80), (90, 90),                     
    (50, 10)                               
]

results = find_dense_regions(my_points, 0, 0, 100, 100, 10, 0.04)

print(f"Regions denses trouvées : {len(results)}")
for r in results:
    print(f"Zone dense détectée à : x={r['x']}, y={r['y']} (Taille {r['width']}x{r['height']})")