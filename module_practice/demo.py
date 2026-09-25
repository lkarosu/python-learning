import summary_tools

if __name__ == "__main__":
    results = [
        {"source": "a.txt", "status": "preview"},
        {"source": "a.txt", "status": "moved"},
        {"source": "a.txt", "status": "skipped"},
    ]

    summary = summary_tools.summarize(results)
    print(summary)