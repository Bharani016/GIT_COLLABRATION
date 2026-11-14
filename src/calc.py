import re
import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
}

def calc(exp):
    lst = [float(x) if x not in operations else x for x in exp]

    for priority in ({"*", "/", "%"}, {"+", "-"}):
        i = 1

        while i < len(lst):
            if lst[i] in priority:
                lst[i - 1:i + 2] = [
                    operations[lst[i]](lst[i - 1], lst[i + 1])
                ]
                i = max(1, i - 2)
            else:
                i += 2

    result = lst[0]
    return int(result) if result.is_integer() else result
     

if __name__ == "__main__":
     
   inp=input("Enter Expression ONLY WITH (+, -, *, /, %)")
   exp=re.split(r"([+*/%-])",inp)
   print(calc(exp))

