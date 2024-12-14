import matplotlib.pyplot as plt
import time
import random

# Visualization of Bubble Sort
def bubble_sort_visualization(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            plt.clf()
            colors = ['skyblue'] * len(arr)
            colors[j] = 'lightcoral'
            colors[j + 1] = 'lightcoral'
            plt.bar(range(len(arr)), arr, color=colors)
            plt.xticks(range(len(arr)), arr, rotation=0)
            plt.title(f"Bubble Sort Step: Comparing indices {j} and {j+1}")
            plt.pause(2.0)  # Slower visualization for better understanding
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.xticks(range(len(arr)), arr, rotation=90)
    plt.title("Bubble Sort Completed")
    plt.show()

# Example Bubble Sort visualization
arr = [random.randint(1, 100) for _ in range(11)]
bubble_sort_visualization(arr)
 