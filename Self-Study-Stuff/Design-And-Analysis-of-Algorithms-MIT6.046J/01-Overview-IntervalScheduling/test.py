import random 

class Request: 
    def __init__(self, start, end): 
        self.start = start 
        self.end = end 
    def __str__(self):
        return f"""-----\nStart: {self.start} \nEnd: {self.end}\n-----"""

def requestsCompatible(req1, req2): 
    return req1.end <= req2.start or req2.end <= req1.start 

def visualizeIntervals(requests, min_val, max_val, width=50):
    scale = (max_val - min_val) / width
    for req in requests:
        line = [' '] * width
        start_idx = int((req.start - min_val) / scale)
        end_idx = int((req.end - min_val) / scale)
        for i in range(start_idx, min(end_idx + 1, width)):
            line[i] = '#'
        print(f"{req.start:3}-{req.end:3}: " + ''.join(line))

def createRandomRequests(num, earliestStarttime = 0, latestEndtime = 100): 
    req = []
    for _ in range(num): 
        startTime = random.randrange(earliestStarttime, latestEndtime) 
        endTime = random.randrange(startTime, latestEndtime)
        request = Request(startTime, endTime) 
        req.append(request)

    return req

        
def findLargestSubsetOfNonweightedCompatibleRequests(requests):
    sorted_requests = sorted(requests, key=lambda r: r.end)
    subset = []
    current_end = -1
    for req in sorted_requests:
        if req.start >= current_end:
            subset.append(req)
            current_end = req.end
    return subset

        
    

requests = createRandomRequests(10) 
visualizeIntervals(requests, 0, 100)
#for req in requests: 
 #   print(str(req))

largestSubset = findLargestSubsetOfNonweightedCompatibleRequests(requests)
print(len(largestSubset))
visualizeIntervals(largestSubset, 0, 100)
