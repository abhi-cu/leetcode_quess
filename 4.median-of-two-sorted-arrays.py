def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    length = len(merged)
    mid = length // 2
    if length % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2.0
    else:
        return float(merged[mid])
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))