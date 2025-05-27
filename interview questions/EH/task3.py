"""
Task 3
Write a function that receives an array of strings that represent friend connections along with the names of
two people and returns a number representing the degrees of separation between the two people.

The connections will be represented by an array of strings with each string taking the format name1:name2,
for examples alice:bob. You can assume that the strings representing the connections will always be lower case a-z only.

The names of the people to find the degrees of separation between will always be non-empty strings e.g. "alice" or "bob".

Your function will return the number of degrees of separation between the two people.
If no connection can be made through friends or friends of friends etc then return -1.

Example 1
connections = ["fred:joe", "joe:mary", "mary:fred", "mary:bill"]
name1 = "fred"
name2 = "bill"
Result = 2
The expected result is 2 because fred is friends with mary, and mary is friends with bill.
That is, bill is of distance 2 from fred.

Example 2
connections = ["fred:joe", "joe:mary", "kate:sean", "sean:sally"]
name1 = "fred"
name2 = "sally"
Result = -1

The expected result is -1 because there are no connections that link fred to sally through either his friends or friends of friends etc.
"""

from typing import List


class Solution:
    def task3(self, connections: List[str], name1: str, name2: str) -> int:
        if name1 == name2: return 0
        
        connection_hash = {}
        for connection in connections:
            n1, n2 = connection.split(":")
            if n1 not in connection_hash:
                connection_hash[n1] = [n2]
            else:
                connection_hash[n1].append(n2)

            if n2 not in connection_hash:
                connection_hash[n2] = [n1]
            else:
                connection_hash[n2].append(n1)
        print("connection_hash: ", connection_hash)

        if name1 not in connection_hash or name2 not in connection_hash:
            return -1
        
        queue = [(name1, 0)]
        visited = {name1}

        while queue:
            current, distance = queue.pop()
            print('current: ', current)
            print('hash: ', connection_hash[current])
            if current == name2:
                return distance
            for friend in connection_hash[current]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, distance + 1))
            print('distance: ', distance)
            print('visited: ', visited)
            print('queue: ', queue)
            print('============================')
        return -1



sol = Solution()
res = sol.task3(["fred:joe", "joe:mary", "mary:fred", "mary:bill"], "fred", "bill")
# res = sol.task3(["fred:joe", "joe:mary", "kate:sean", "sean:sally"], "fred", "sally")
print('res: ', res)