from multiprocessing import Pool
from task_distribution import distribute_tasks, process_tasks

def parallel_process(tasks, num_processes):
    task_chunks = distribute_tasks(tasks, num_processes)

    with Pool(processes=num_processes) as pool:
        results = pool.map(process_tasks, task_chunks)

    # Flatten the results if needed
    flat_results = [result for sublist in results for result in sublist]

    return flat_results

if __name__ == "__main__":
    # Example usage
    tasks_to_process = list(range(100))
    num_processes = 4

    processed_results = parallel_process(tasks_to_process, num_processes)
    print("Processed Results:", processed_results)
