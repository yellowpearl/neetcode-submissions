class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    # neet
    # google google
    # 

    def __init__(self, homepage: str):
        self.now = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url, prev=self.now)
        self.now.next = node
        self.now = node

    def back(self, steps: int) -> str:
        while self.now.prev and steps:
            steps -= 1
            self.now = self.now.prev
        return self.now.val

    def forward(self, steps: int) -> str:
        while self.now.next and steps:
            steps -= 1
            self.now = self.now.next
        return self.now.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)