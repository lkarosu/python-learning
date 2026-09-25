def summarize(results:list[dict]):
    results_summary = {
        'preview': 0,
        'moved': 0,
        'skipped': 0,
        'error': 0,
    }
    for result in results:
        status = result.get("status")
        if status in results_summary:
            results_summary[status] += 1
    return results_summary
