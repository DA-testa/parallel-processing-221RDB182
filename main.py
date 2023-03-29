# python3
import heapq

def parallel_processing(n, m, data):
output = []
# Initialize priority queue with first n jobs
pq = [(0, i) for i in range(n)]
heapq.heapify(pq)

for i in range(m):
    # Get next available thread
    t, thread = heapq.heappop(pq)
    # Calculate start time of current job
    start_time = t
    # Calculate finish time of current job
    finish_time = t + data[i]
    # Append result to output list
    output.append((thread, start_time))
    # Push next job onto priority queue with updated finish time
    heapq.heappush(pq, (finish_time, thread))

return output
def main():
# Get input from user
n, m = map(int, input().split())
data = list(map(int, input().split()))

# Call parallel_processing function
result = parallel_processing(n, m, data)

# Print results
for thread, start_time in result:
    print(thread, start_time)

if __name__ == "__main__":
    main()
