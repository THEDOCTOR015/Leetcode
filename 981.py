"""
Answer:
"""
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, []) + [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            values = self.map[key]
            left, right = 0, len(values)
            while left < right:
                mid = (left + right) // 2
                if values[mid][1] <= timestamp:
                    left = mid + 1
                else:
                    right = mid
            return "" if right == 0 else values[right-1][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
"""
Tests:
"""
timemap = TimeMap()
timemap.set("foo", "bar", 1)
print(timemap.get("foo", 1))
print(timemap.get("foo", 3))
timemap.set("foo", "bar2", 4)
print(timemap.get("foo", 4))
print(timemap.get("foo", 5))
print(timemap.get("foo", 3))
print(timemap.get("foo", 0))
timemap.set("foo", "bar3", 10000)
print(timemap.get("foo", 1000000))