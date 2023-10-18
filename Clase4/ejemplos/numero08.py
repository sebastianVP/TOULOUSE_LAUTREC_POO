import collections

q= collections.deque([10,20,30,40,50])

q.appendleft(0)
print(q)

q.append(60)
print(q)


print(q.pop())
print(q)

print(q.popleft())
print(q)
