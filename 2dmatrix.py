ex = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
def check_for_target(t):
#Test Horizontal:
    for v in ex:
        testHorizontal = ""
        for h in v:
            testHorizontal = testHorizontal + str(h)
            if t in testHorizontal:
                return True
#Test Vertical:
    testVertical = ""
    for x in range(4):
        for v in ex:
            testVertical = testVertical + str(v[x])
            if t in testVertical:
                return True
    return False
target = "AB"
print("target:" + target)
print(check_for_target(target))

