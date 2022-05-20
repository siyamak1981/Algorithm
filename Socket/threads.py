import time
import threading
import logging
x = logging.basicConfig(level=logging.DEBUG, format = '[%(levelname)s] (%(threadName)-10s) %(message)s')
# logging.basicConfig(level=logging.DEBUG)

# def foo():
#     print("hello japan")

# threads = []
# t = threading.Thread(target = foo)
# threads.append(t)
# t.start()

# import threading

# def bar():
#     print("hello siyamak")

# threads = []
# for i in range(0,5):
#     t = threading.Thread(bar)
#     threads.append(t)
#     t.start()



# def foo (a, b):
#     print(f" the first num is :{a} and secounf num is : {b}")
#     print(f"total of tow numbet is : {a} + {b} = {a + b}")
# threads = []
# for i in range(5):
#     t = threading.Thread(target = foo, args = [2,5])
#     threads.append(t)
    
#     t.start()


# import datetime
# def foo():
#     start = datetime.datetime.now()
#     print(threading.currentThread().getName(), "Starting" )
#     end = datetime.datetime.now()
#     print(threading.currentThread().getName(), "Ending" )
#     print(start-end)

# threds = []
# t = threading.Thread(target = foo)
# threds.append(t)
# t.start()


# def foo():
#     time.sleep(2)
#     print(threading.currentThread(), "Starting...")
#     time.sleep(2)
#     print(threading.currentThread(), "Ending...")

# def bar():
#     time.sleep(2)
#     print(threading.currentThread(), "Starting...")
#     time.sleep(2)
#     print(threading.currentThread(), "Ending...")

# f = threading.Thread(target = foo, name ="--->foo")
# b = threading.Thread(target = bar, name ="--->bar")
# t = threading.Thread(target = bar)
# f.start()
# b.start()
# t.start()

# def foo():
    
#     logging.debug("Starting ...")
#     time.sleep(3)
#     logging.debug("Ending...")
# threads = []

# t = threading.Thread(name = "--->foo name", target = foo)
# threads.append(t)
# """with setDeamon True line ending will not be acted"""
# t.setDaemon(True)
# t.start()
# """with join function the end line will be acted"""
# t.join()
# """ with number inside of join fun mean that thread will be end befor arrive to time.sleep()  """
# t.join(2)


# def foo():
#     logging.debug("Starting ... ")
#     time.sleep(4)
#     logging.debug("Exiting...")

# t = threading.Thread(target = foo, name = "foo name")
# t.setDaemon(True)
# t.start()
# t.join(2)
# print(t.is_alive())
# print(t.isDaemon())
# time.sleep(5)
# print(t.is_alive())
# print(t.isDaemon())

# def foo():
#     logging.debug("Starting ..")
#     time.sleep(10)
#     logging.debug("Exiting ..")


# t = threading.Thread(target = foo)
# t.setDaemon(True)
# t.start()

# main_thread = threading.currentThread()
# print(f"main_thread: {main_thread}")
# print(f"enumerate is: {threading.enumerate()}")
# for i in threading.enumerate():
#     print(i)
#     """enumerate: Return a list of all Thread objects currently active"""
#     if i is main_thread:
#         continue
#     logging.debug(f"joining is {t.getName()}")
#     i.join()



# def foo():
#     logging.debug("start..")
#     time.sleep(5)
#     logging.debug("exit..")

# for i in range(3):
#     t = threading.Thread(target = foo)
#     t.setDaemon(True)
#     t.start()

# main = threading.currentThread()
# for t in threading.enumerate():
#     if t is main:
#         continue
#     logging.debug( t.getName())
#     t.join()



# class N(threading.Thread):
#     def __init__(self, name= None, group=None, target = None, args = (), kwargs = None, verbose = None):
#         threading.Thread.__init__(self, name, target = target)
#         self.name = "siyamak"
#         self.group = 5
#         self.args = args
#         self.kwargs = kwargs
   

#     def foo(self):
#         logging.debug(f"this is name:{self.name}, args is: {self.args}, kwargs is:{self.kwargs} group is : {self.group}")
    
# t = N(args=(1,2,5), kwargs ={"a":1, "b": 2, "c":3})
# t.foo()
# t.start()




# def foo(e):
#     logging.debug("start to event resulting..")
#     event_is_set = e.wait()
#     logging.debug(f"event set:{event_is_set}")

# e = threading.Event()
# t = threading.Thread(target = foo, name = "event name", args=(e,))
# t.start()
# logging.debug("waiting befor call event .set")
# time.sleep(3)
# e.set()
# logging.debug("event is set")



# def foo(s, t):
#     logging.debug("user function waiting for event ..")
#     event_is_wait = e.wait(t)
#     logging.debug(f"event set is: {event_is_wait}")
#     if event_is_wait:
#         logging.debug("proccessing event..")
#     else:
#         logging.debug("doing other work...")

# e = threading.Event()
# t = threading.Thread(target = foo, name = "event foo", args = (e,5))

# t.start()
# logging.debug("waiting befor call event .set")
# time.sleep(2)
# e.set()
# logging.debug("event is set")



# """کتابخانه threading عملکردی برای قفل کردن نخ‌ها دارد. عملیات قفل کردن به ما این امکان را می‌دهد تا حافظه مشترک را مدیریت و از خراب شدن داده‌ها جلوگیری کنیم.

# برای قفل کردن از متد Lock استفاده می‌کنیم. سپس با استفاده از متد acquire قفل را فعال و با متد release آزاد می‌کنیم.

# """
# class Counter(object):
#     def __init__(self, start = 0):
#         self.lock = threading.Lock()
#         self.value = start
#     def increment(self):
#         logging.debug(f"waiting for lock {self.lock}")
#         self.lock.acquire()
#         try:
#             logging.debug(f"Acquired lock {self.value}")
#             self.value = self.value + 1
#         finally:
#             self.lock.release()
#             logging.debug(f"Acquired lock ")

# def userfunction(c):
#     logging.debug("Starting")
#     time.sleep(3)
#     c.increment()
#     logging.debug("exiting")

# counter = Counter()
# for i in range(2):
#     t = threading.Thread(target=userfunction, args = (counter,))
#     t.start()

# logging.debug("waiting for userfunction threads")
# main_thread = threading.currentThread()
# for t in threading.enumerate():
#     if t is not main_thread:
#         t.join()



# def thread_using_with(lock):
#     with lock:
#         logging.debug("lock axqired via with")

# def thread_notusing_with(lock):
#     lock.acquire()
#     try:
#         logging.debug("lock acquired directly")
#     finally:
#         lock.release()
# lock = threading.Lock()
# w = threading.Thread(target = thread_using_with, args = (lock,))
# nw = threading.Thread(target = thread_notusing_with, args = (lock,))
# w.start()
# nw.start()


# def consumer_thread(cond):
#     logging.debug("Starting consumer_thread thread")
#     t = threading.currentThread()
#     with cond:
#         cond.wait()
#         logging.debug("resouce is available to consumer_threadd")

# def producer_thread(cond):
#     logging.debug("Starting producer_thread thread")
#     with cond:
#         logging.debug("Making resource available")
#         cond.notifyAll()

# condition = threading.Condition()
# c1 = threading.Thread(target = consumer_thread, args = (condition,))
# c2 = threading.Thread(target = producer_thread, args = (condition,))
# c1.start()
# c2.start()


# def foo(data):
#     try:
#         val = data.value
#     except AttributeError:
#         logging.debug("No value yet")
#     else:
#         logging.debug(f"val")

# def thread_function(data):
#     foo(data)
#     data.value = random.randint(1,100)
#     foo(data)

# local_data = threading.local()
# for i in range(2):
#     t = threading.Thread(target = foo, args = (local_data,))
#     t.start()



# import threading, queue

# q = queue.Queue()

# def worker():
#     while True:
#         item = q.get()
#         print(f'Working on {item}')
#         print(f'Finished {item}')
#         q.task_done()

# # Turn-on the worker thread.
# threading.Thread(target=worker, daemon=True).start()

# # Send thirty task requests to the worker.
# for item in range(30):
#     q.put(item)

# # Block until all tasks are done.
# q.join()
# print('All work completed')


import asyncio

# async def foo():
#    print("hello async")

# async def bar():
#     await foo()

# asyncio.run(bar())



# async def foo():
#    await asyncio.sleep(1)
#    return 1

# coro = foo()
# print(asyncio.run(foo()))



# async def bar(n):
#    while n != 0:
#       print("from async countdown: ", n)
#       n -=1
#       await asyncio.sleep(1)

# coro = bar(5)
# # asyncio.run(coro)
# loop = asyncio.get_event_loop()

# task = loop.create_task(bar(6))
# # loop.create_task(bar(6))
# # loop.run_forever()
# # result = loop.run_until_complete(task)
# # print(result)
# pending = asyncio.all_tasks(loop = loop)
# # print(pending)
# # group = asyncio.gather(foo(5), bar(5))
# group = asyncio.gather(*pending, loop = loop)
# print(group)
# result = loop.run_until_complete(group)
# loop.close()
# # print(task)


# async def foo():
#    print("hello japan")

# async def bar():
#    await foo()

# asyncio.run(bar())



# import asyncio
# import datetime
# import random

# async def my_sleep_func():
#     await asyncio.sleep(random.randint(0, 5))

# async def display_date(num, loop):
#     end_time = loop.time() + 50.0    
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop.time() + 1.0) >= end_time:
#                 break
#         await my_sleep_func()
        
# loop = asyncio.get_event_loop()

# asyncio.ensure_future(display_date(1, loop))
# asyncio.ensure_future(display_date(2, loop))

# loop.run_forever()


# import asyncio
# import time

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     print("******************************")
#     print(f"started at {time.strftime('%X')}")
#     await say_after(5, 'hello')
#     await say_after(2, 'world')
#     print(f"finished at {time.strftime('%X')}")
#     print("******************************")

# asyncio.run(main())

# نتایج 
# ******************************
# started at 17:10:50
# hello
# world
# finished at 17:10:57
# ******************************




# import asyncio
# import time

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     task1 = asyncio.create_task(say_after(5, 'hello'))
#     task2 = asyncio.create_task(say_after(2, 'world'))
#     print(f"started at {time.strftime('%X')}")
#     # Wait until both tasks are completed (should take around 2 seconds.)
#     await task1
#     await task2
#     print(f"finished at {time.strftime('%X')}")
# نتایج
# ****************************** 
# started at 17:20:30
# world
# hello
# finished at 17:20:35
# ******************************



# import asyncio
# import concurrent.futures

# def blocking_io():
#     # File operations (such as logging) can block the
#     # event loop: run them in a thread pool.
#     with open('/dev/urandom', 'rb') as f:
#         return f.read(100)

# def cpu_bound():
#     # CPU-bound operations will block the event loop:
#     # in general it is preferable to run them in a
#     # process pool.
#     return sum(i * i for i in range(10 ** 7))

# async def main():
#     loop = asyncio.get_running_loop()
#     ## Options:
#     # 1. Run in the default loop's executor:
#     result = await loop.run_in_executor(None, blocking_io)
#     print('default thread pool', result)
#     # 2. Run in a custom thread pool:
#     with concurrent.futures.ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, blocking_io)
#         print('custom thread pool', result)
#     # 3. Run in a custom process pool:
#     with concurrent.futures.ProcessPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, cpu_bound)
#         print('custom process pool', result)

# asyncio.run(main())





import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

# Expected output:
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(4)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24