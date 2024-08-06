#!/usr/bin/env python3
"""
   Write a coroutine called async_generator that takes no arguments.

   The coroutine will loop 10 times,
   each time asynchronously wait 1 second,
   then yield a random number between 0 and 10.

   Use the random module.
"""
from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """Using generator"""

    for _ in range(10):
        await asyncio.sleep(1)
        random_value = random.random() * 10
        yield random_value
