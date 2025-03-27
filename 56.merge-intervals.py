def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:  
            merged[-1][1] = max(last_end, end)  
        else:
            merged.append([start, end]) 
    return merged
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  