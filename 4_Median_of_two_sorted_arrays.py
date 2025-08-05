def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    merged_array = [0] * (m + n)
    i, j, k = 0, 0, 0

    # Merging two sorted arrays
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            merged_array[k] = nums1[i]
            i += 1
        else:
            merged_array[k] = nums2[j]
            j += 1
        k += 1

    # Appending remaining elements
    while i < m:
        merged_array[k] = nums1[i]
        i += 1
        k += 1

    while j < n:
        merged_array[k] = nums2[j]
        j += 1
        k += 1

    # Finding median
    total = m + n
    if total % 2 == 0:
        mid1 = merged_array[total // 2]
        mid2 = merged_array[total // 2 - 1]
        return (mid1 + mid2) / 2.0
    else:
        return merged_array[total // 2]


if __name__ == '__main__':
    print("Enter elements of first sorted array (space-separated):")
    nums1 = list(map(int, input().split()))

    print("Enter elements of second sorted array (space-separated):")
    nums2 = list(map(int, input().split()))

    median = findMedianSortedArrays(nums1, nums2)
    print(f"The median is: {median}")
