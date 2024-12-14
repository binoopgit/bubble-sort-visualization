
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is fully sorted.

Bubble Sort is an inefficient algorithm for large datasets, with a time complexity of O(n²) in the average and worst cases, but it is easy to understand and implement.


## How it Works:

1)Start at the beginning of the list.

2)Compare each pair of adjacent elements:

If the current element is greater than the next element, swap them.

3)Continue this process until the end of the list, at which point the largest element "bubbles up" to the correct position at the end.

4)Repeat the above steps for the remaining elements, excluding the last sorted elements.

5)The process repeats until no swaps are needed, meaning the list is sorted.

## Example:
Suppose you have the list [5, 3, 8, 4, 2]:

First pass:
Compare 5 and 3, swap: [3, 5, 8, 4, 2]

Compare 5 and 8, no swap.

Compare 8 and 4, swap: [3, 5, 4, 8, 2]

Compare 8 and 2, swap: [3, 5, 4, 2, 8]

Largest element 8 is now at the end.

Subsequent passes repeat this process until the entire list is sorted.

# Bubble Sort Visualization

This project provides a simple visualization of the Bubble Sort algorithm using Python and Matplotlib. The visualization helps demonstrate how the algorithm works by showing the step-by-step comparison and swapping of elements in an array.


## Prerequisites

To run this code, you will need:

Python 3.x

Matplotlib library

You can install Matplotlib using pip:
 ```bash
   pip install matplotlib
   ```
## Running the Visualization 

The code generates a list of random integers and visualizes the sorting process. To run the visualization:

Save the script as bubblesort_visual.py.

Run the script using Python:
```bash
   python bubblesort_visual.py
   ```
## How the Visualization Works

The algorithm iteratively compares adjacent elements in the list.

If the element on the left is greater than the one on the right, they are swapped.

The visualization uses bars to represent the elements, and the bars being compared are highlighted in red.

The process continues until the entire list is sorted, which is then displayed in a final sorted visualization.

## Features

Step-by-step visualization of the Bubble Sort algorithm.

Comparisons are highlighted in red for better understanding.

The sorting process is intentionally slowed down for easier comprehension.

## Example

An array of 11 random elements is generated, and the sorting process is displayed in real time.

## Customization

You can change the number of elements in the list by modifying the line:
 ```bash
   arr = [random.randint(1, 100) for _ in range(11)]
   ```
You can also adjust the speed of the visualization by modifying the plt.pause() value.

## License
This project is open source and available under the [MIT](https://choosealicense.com/licenses/mit/).# bubble-sort-visualization
