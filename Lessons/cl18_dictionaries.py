"""Examples of dictionary syntax with Ice Cream Show order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evalutates to the number of entries
print(len(ice_cream))  # Prints 3

# add a key-value entry by directly assigning to a key
ice_cream["mint"] = 3

# access entries by their key
print(ice_cream["chocolate"])  # Prints 12

# test if "pbj" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream

# to remove, we use the pop method and give it a key (if printed it evaluates to the value associated to the key)
ice_cream.pop("strawberry")

# to iterate over every key in a loop, use for in
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} order")
