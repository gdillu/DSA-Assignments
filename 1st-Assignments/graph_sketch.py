import sys
import ast
import matplotlib.pyplot as plt

def plot_execution(all_values, title):
    plt.figure(figsize=(10, 6))
    sizes = [100, 250, 500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000]
    
    if len(all_values) == 6:
        labels = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap','Radix']
    else:
        labels = ['Quick Sort', 'Quick Sort Median', 'Quick Sort Random']

    for i, execution_times in enumerate(all_values):
        plt.plot(sizes, execution_times, marker='o', linestyle='-', label=labels[i] if i < len(labels) else f'Algorithm {i+1}')
    
    plt.title(f'Execution Time vs. Input Size ({title})')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (ms)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'execution_time_plot_{title}.png')
    print("Plot saved as 'execution_time_plot.png'")
    plt.show()

if __name__ == "__main__":
    # Read the command-line argument
    if len(sys.argv) < 3:
        print("Usage: python graph_sketch.py '<list_of_lists>' '<title>'")
        sys.exit(1)
    
    try:
        exec_list = sys.argv[1]
        title = sys.argv[2]
        all_times = ast.literal_eval(exec_list)
        
        if not isinstance(all_times, list) or not all(isinstance(lst, list) for lst in all_times):
            raise ValueError("Data should be a list of lists.")
        
        plot_execution(all_times, title)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
