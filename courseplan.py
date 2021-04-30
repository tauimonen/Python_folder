from collections import defaultdict

class CoursePlan:
    def __init__(self):
        self.courses = {}
        self.count = -1
        self.num_name = {}
        self.name_num = {}

    def add_course(self, course):
        self.count += 1
        c = self.count
        self.courses[c] = []
        self.num_name[c] = course
        self.name_num[course] = c

    def add_requisite(self, course1, course2):
        key = self.name_num[course1]
        self.courses[key].append(course2)

    def topohelp(self, x, visited, stack):
        visited[x] = True
        for i in range(len(self.courses[x])):
            if visited[x]:
                self.topohelp(i, visited, stack)
        stack.insert(0, x)
        print(stack)

    def find(self):
        n = len(self.courses)
        result = []
        visited = [False] * n
        stack = []
        for i in range(n):
            if not visited[i]:
                self.topohelp(i, visited, stack)
        for i in stack:
            result.append(self.num_name[i])
        return result


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