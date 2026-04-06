fs = frozenset([1, 2,2, 3, 4, 5])
print(fs)  # Output: frozenset({1, 2, 3, 4, 5})

# fs.add(6)  # This will raise an AttributeError because frozensets are immutable
# fs.remove(3)  # This will also raise an AttributeError for the same reason

