import multiprocessing

def distribute_tasks(task_list, num_processes):
    chunk_size = len(task_list) // num_processes
    chunks = [task_list[i:i + chunk_size] for i in range(0, len(task_list), chunk_size)]
    return chunks

def process_tasks(task_chunk):
    # Replace this function with the actual task processing logic
    results = []
    for task in task_chunk:
        result = task * 2  # Example task processing
        results.append(result)
    return results
