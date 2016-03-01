import Lesson1 as f

for i in range(1, 9):
    print 'Task ' + str(i)
    f.__dict__['task' + str(i)]()
    print '-'*60
