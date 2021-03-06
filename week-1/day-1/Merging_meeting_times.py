import unittest


def merge_ranges(meetings):

   meeting_times = sorted(meetings)
   merged_range = [meeting_times[0]]

   for start, end in meeting_times[1:]:
       last_start, last_end = merged_range[-1]

       if last_end >= start:
           merged_range[-1] = (last_start, max(last_end, end))
       else:
           merged_range.append((start, end))

   return merged_range



TESTCASES

print(merge_ranges([(1, 3), (2, 4)]))         expected = [(1, 4)]
print(merge_ranges([(5, 6), (6, 8)]))         expected = [(5, 8)]
print(merge_ranges([(1, 8), (2, 5)]))         expected = [(1, 8)]
print(merge_ranges([(1, 3), (4, 8)]))         expected = [(1, 3), (4, 8)]
print(merge_ranges([(1, 4), (2, 5), (5, 8)])) expected = [(1, 8)]
