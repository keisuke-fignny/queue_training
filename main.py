from myQueue import MyQueue

queue = MyQueue()

print(f'queued {queue.push("hello")}')
print(f'queued {queue.push("good-evening")}')
print(f'queued {queue.push("zzzzz")}')

print(f'-----------------------------------')

print(f'shifted {queue.pop()}')
print(f'shifted {queue.pop()}')
print(f'shifted {queue.pop()}')

