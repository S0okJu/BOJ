import sys 
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, l, r):
        # l, r inclusive
        l += self.size
        r += self.size
        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res

class TVPopularity:
    def __init__(self, n, intervals):
        self.n = n
        self.intervals = intervals
        self.diff = [0] * 86401
        for line in intervals:
            start_sec, end_sec = self.parse_interval(line)
            for s, e in self.normalize_interval(start_sec, end_sec):
                self.diff[s] += 1
                if e + 1 <= 86400:
                    self.diff[e + 1] -= 1
        self.viewers = [0] * 86400
        current = 0
        for i in range(86400):
            current += self.diff[i]
            self.viewers[i] = current

        self.seg_tree = SegmentTree(self.viewers)

    @staticmethod
    def time_to_seconds(t):
        h, m, s = map(int, t.split(':'))
        return h * 3600 + m * 60 + s

    @staticmethod
    def parse_interval(line):
        start_str, end_str = line.split(' - ')
        start_sec = TVPopularity.time_to_seconds(start_str)
        end_sec = TVPopularity.time_to_seconds(end_str)
        return start_sec, end_sec

    @staticmethod
    def normalize_interval(start_sec, end_sec):
        if end_sec < start_sec:
            return [(start_sec, 86399), (0, end_sec)]
        else:
            return [(start_sec, end_sec)]

    def popularity(self, start_sec, end_sec):
        norm_intervals = self.normalize_interval(start_sec, end_sec)
        total_popularity = 0
        total_length = 0
        for s, e in norm_intervals:
            length = e - s + 1
            total_length += length
            total_popularity += self.seg_tree.query(s, e)
        return total_popularity / total_length


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    N = int(input())
    intervals = [input().strip() for _ in range(N)]
    Q = int(input())

    tv = TVPopularity(N, intervals)
    for _ in range(Q):
        query = input().strip()
        s, e = TVPopularity.parse_interval(query)
        print(f'{tv.popularity(s, e):.10f}')
