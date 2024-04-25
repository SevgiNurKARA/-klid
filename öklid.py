# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:08:33 2024

@author: sevgi
"""
        

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
# İki nokta arasındaki Öklid mesafesini hesaplayan bir fonksiyon tanımlayın
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

# Tüm nokta çiftleri için mesafeleri hesaplayın ve 'distances' adında bir listede saklayın
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulun ve yazdırın
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance:.2f}")
