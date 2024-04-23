#!/usr/bin/env python3

""" 0. Async Generatr """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generatr

    Args:
    None

    Returns:
        Generator: A list containing float | None
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
