class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)  # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert a node at the MRU position
    def insert_at_mru(self, node):
        prev_node = self.right.prev

        node.prev = prev_node
        node.next = self.right

        prev_node.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache.get(key)

        self.remove(node)

        self.insert_at_mru(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache.get(key)

            node.value = value

            self.remove(node)

            self.insert_at_mru(node)

            return

        if len(self.cache) == self.capacity:
            lru_node = self.left.next

            evicted_key = lru_node.key

            self.remove(lru_node)

            self.cache.pop(evicted_key)

        new_node = Node(key, value)

        self.cache[key] = new_node

        self.insert_at_mru(new_node)
