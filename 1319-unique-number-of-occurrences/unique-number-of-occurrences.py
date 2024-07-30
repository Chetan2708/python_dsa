class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}

        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        occurrence_set = set()

        for occurrence in count.values():
            if occurrence in occurrence_set:
                return False
            occurrence_set.add(occurrence)

        return True
