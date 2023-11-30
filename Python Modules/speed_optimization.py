import time

def time_function_execution(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
    return result

if __name__ == "__main__":
    # Example usage
    from parallel_processing import parallel_process, tasks_to_process, num_processes

    # Measure the execution time of parallel processing
    parallel_execution_time = time_function_execution(parallel_process, tasks_to_process, num_processes)

    # Replace the following function with the actual non-parallelized task processing logic
    def sequential_process(tasks):
        results = []
        for task in tasks:
            result = task * 2  # Example task processing
            results.append(result)
        return results

    # Measure the execution time of sequential processing
    sequential_execution_time = time_function_execution(sequential_process, tasks_to_process)

    speedup_factor = sequential_execution_time / parallel_execution_time
    print(f"Speedup Factor: {speedup_factor:.2f}")
