from collections import defaultdict

class CoursePlan:
    def __init__(self):
        self.courses = []
        self.requirements = defaultdict(list)
        self.visited = {}
        self.cycle = False

    def add_course(self,course):
        self.courses.append(course)

    def add_requisite(self,course1,course2):
        self.requirements[course1].append(course2)

    def dfs(self, c):
        if self.visited[c] == 2:
            return
        if self.visited[c] == 1:
            self.cycle = True
            return

        self.visited[c] = 1
        for neighbour in self.requirements[c]:
            self.dfs(neighbour)
        self.visited[c] = 2
        self.order.append(c)

    def find(self):
        self.order = []
        for c in self.courses:
            self.visited[c] = 0
        for c in self.courses:
            if self.visited[c] == 0:
                self.dfs(c)
            if self.cycle:
                return None
        self.order.reverse()

        return self.order


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course('course1')
    c.add_course('course2')
    c.add_requisite('course1', 'course2')
    c.add_course('course3')
    c.add_requisite('course1', 'course3')
    print(c.find()) # ['course1', 'course3', 'course2']
    print(c.find()) # ['course1', 'course3', 'course2']
    c.add_course('course4')
    c.add_course('course5')
    c.add_requisite('course4', 'course5')