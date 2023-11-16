import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def lenght(point) :
            x = point[0]
            y = point[1]
            return pow(x, 2) + pow(y, 2)
        mappoint = {}
        for point in points :
            longueur = lenght(point)
            if longueur in mappoint :
                mappoint[longueur] = mappoint[longueur] + [point]
            else :
                mappoint[longueur] = [point]
        heap = list(mappoint.keys())
        heapq.heapify(heap)
        output = []
        while len(output) < k :
            res = heapq.heappop(heap)
            output = output + mappoint[res]
        return output

    