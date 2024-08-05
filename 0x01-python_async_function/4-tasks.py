#!/usr/bin/env python3
"""
   Take the code from wait_n and
   alter it into a new function
   task_wait_n. The code is nearly
   identical to wait_n except
   task_wait_random is being called
"""
from typing import List
import asyncio
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
       Use heapq is well suited for
       managing an orederd collection of items
    """

    delayed = []

    my_heap = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        heapq.heappush(my_heap, delay)

    while my_heap:
        delayed.append(heapq.heappop(my_heap))

    task = task_wait_random(max_delay)
    await task

    return delayed
