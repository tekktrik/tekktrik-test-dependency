from typing import Any

def printaroo(thing: Any) -> None:
    print("thing:", thing)
    print("type:", type(thing))
    
def printyprinty(thing: Any) -> None:
    for _ in range(2):
        print(thing)
