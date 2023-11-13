import math


def distance(point, centroid):
    x1, y1 = point
    x2, y2 = centroid
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def converged(old_centroids, new_centroids):
    return old_centroids == new_centroids


def k_means(data_points, initial_centroids):
    num_clusters = len(initial_centroids)

    centroids = initial_centroids
    clusters = [[] for _ in range(num_clusters)]

    epochs = 0
    flag = True
    while flag:
        epochs += 1
        print(f"================ Epoch {epochs} ================")

        # Clearing clusters
        for cluster in clusters:
            cluster.clear()

        # Assigning each point to the closest cluster
        for name, point in data_points.items():
            distances = [distance(point, centroid) for centroid in centroids]
            closest_centroid = distances.index(min(distances))

            # Assigning each point to the closest cluster
            clusters[closest_centroid].append(name)

        # Saving old centroids
        old_centroids = centroids.copy()

        # Updating centroids
        for cluster in clusters:
            x = sum(data_points[name][0] for name in cluster) / len(cluster)
            y = sum(data_points[name][1] for name in cluster) / len(cluster)
            centroids[clusters.index(cluster)] = (x, y)

        # Print clusters and centroids
        for i in range(num_clusters):
            print(f"Cluster {i + 1}: {clusters[i]} at {centroids[i]}")

        if converged(old_centroids, centroids):
            flag = False

    print(f"\nFinal Summary: {epochs} epochs")
    for i in range(num_clusters):
        print(f"Cluster {i + 1}: {clusters[i]} at {centroids[i]}")


data_points = {
    "A1": (2, 10),
    "A2": (2, 5),
    "A3": (8, 4),
    "A4": (5, 8),
    "A5": (7, 5),
    "A6": (6, 4),
    "A7": (1, 2),
    "A8": (4, 9),
}

print("Task 1: Question 1 & 2... Initial Centroids: A1, A4, A7")
k_means(data_points, [data_points["A1"], data_points["A4"], data_points["A7"]])

print("\nTask 1: Question 3... Initial Centroids: A2, A5, A6")
k_means(data_points, [data_points["A3"], data_points["A5"], data_points["A6"]])
