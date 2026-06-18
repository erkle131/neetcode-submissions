class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        search_list = self.time_map[key]
        L, R = 0, len(search_list) - 1

        res = ""
        while L <= R:
            mid = L + (R - L) // 2

            if search_list[mid][1] <= timestamp:
                res = search_list[mid][0]
                L = mid + 1
            else:
                R = mid - 1

        return res
