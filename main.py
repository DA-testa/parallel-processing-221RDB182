import heapq

def parallel_processing(n, m, data):
    output = []
    pq = [(0, i) for i in range(n)]
    heapq.heapify(pq)

    for i in range(m):
        t, thread = heapq.heappop(pq)
        start_time = t
        finish_time = t + data[i]
        output.append((thread, start_time))
        heapq.heappush(pq, (finish_time, thread))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread, start_time in result:
        print(thread, start_time)
    
if __name__ == "__main__":
    main()
