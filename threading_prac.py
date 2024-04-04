print("Hello Thread for Threading")

import threading
import concurrent.futures
import time

def do_something(seconds):
    print(f"Sleep for {seconds} second")
    time.sleep(seconds)
    print(f"Done Sleeping... {seconds}")

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    results = executor.map(do_something, secs)
    for result in results:
        result
# # Thread way
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         f.result()
# Thread way

# threads = []
# for _ in range(10):
#
#     t = threading.Thread(target=do_something, args=[_])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

end = time.perf_counter()

print(f"Finished in {end-start} seconds")