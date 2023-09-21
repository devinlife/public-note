import asyncio
from typing import Callable, Any, Awaitable


class EventHandler:
    def __init__(self):
        self.handlers = {}

    def register(self, event_name: str, handler: Callable[..., Any]):
        if event_name not in self.handlers:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)

    async def handle_event(self, event_name: str, *args, **kwargs):
        if event_name not in self.handlers:
            print(f"No handlers registered for {event_name}")
            return

        tasks = []
        for handler in self.handlers[event_name]:
            if asyncio.iscoroutinefunction(handler):
                task = asyncio.ensure_future(handler(*args, **kwargs))
                tasks.append(task)
            # else:
            #     result = handler(*args, **kwargs)
            #     print(f"Sync result for {event_name}: {result}")

        if tasks:
            await asyncio.gather(*tasks)


# Define some example handlers
async def async_handler1(*args, **kwargs):
    print("Async handler 1 execute!!")
    await asyncio.sleep(4)
    print("Async handler 1 executed")


async def async_handler2(*args, **kwargs):
    print("Async handler 2 execute!!")
    await asyncio.sleep(5)
    print("Async handler 2 executed")


def sync_handler1(*args, **kwargs):
    print("Sync handler 1 executed")


def sync_handler2(*args, **kwargs):
    print("Sync handler 2 executed")


# Create an event handler instance
event_handler = EventHandler()

# Register handlers
event_handler.register("event1", async_handler1)
event_handler.register("event1", sync_handler1)
event_handler.register("event2", async_handler2)
event_handler.register("event2", sync_handler2)


# Trigger events
async def main():
    await event_handler.handle_event("event1", "some_arg", key="value")
    await event_handler.handle_event("event2")


asyncio.run(main())
