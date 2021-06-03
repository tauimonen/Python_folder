"""
The network is computed so that the network node IDs are
strings (course names). For this reason, the network is
computed as a hash table, where the keys are course names
and the values are side lists.
"""


class CoursePlan:
    def __init__(self):
        self.result = []
        self.error = False
        self.color = {}
        self.courses = []
        self.graph = {}

    def add_course(self, course):
        self.courses.append(course)
        self.graph[course] = []

    def add_requisite(self, course1, course2):
        self.graph[course1].append(course2)

    def dfs(self, course):
        if self.color[course] == 1:
            self.error = True
            return
        if self.color[course] == 2:
            return
        self.color[course] = 1
        for next in self.graph[course]:
            self.dfs(next)
        self.result.append(course)
        self.color[course] = 2

    def find(self):
        for course in self.courses:
            self.color[course] = 0
        for course in self.courses:
            if self.color[course] == 0:
                self.dfs(course)
        self.result.reverse()
        return None if self.error else self.result


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe","Ohja")
    c.add_requisite("Ohja","Tira")
    c.add_requisite("Jym","Tira")
    print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira","Tira")
    print(c.find()) # None