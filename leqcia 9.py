# ვიღაცამ ფრჩხილებით შედგენილი სტრინგი შემოიტანა, მაგრამ რამდენადენად დაბალანსებულია??? სტრინგი აწყობილია მხოლოდ ( და ) ებით, დაბალანსებულად ჩაითვლება სტრინგი რომელშიც ყველა გაღებული ფრჩხილი იხურება და არცერთი არ რჩება გახსნილი. მაგალითი: 
# ✅ Balanced:
# () → open one, close one.
# (()()) → open → open → close → open → close → close (everything matches).
# (())() → nesting and sequence are correct.
# ❌ Not balanced:
# )( → tries to close before opening.
# (() → opened more than closed.
# ())( → wrong order of closing.
# მინიშნება: გამოიყენე ფუნქცია და ერთ ერთი განვლილი data structure 
def is_balanced(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

s = input("enter string: ")
print("YES" if is_balanced(s) else "NO")
# გიოს ინგლისურის საკონტროლოზე საშლელის წაღება
#  დაავიწყდა=( არადა ციალა მასწავლებელი მართლწერის ყველა 
# შეცდომაზე აკლებს ქულას. ამის თავიდან ასარიდებლად გიომ მაგარი 
# ტაქტიკა მოიფიქრა: - ებს დაწერს რაც ნიშნავს რომ წინა ასო წასაშლელია. 
# დავეხმაროთ გიოს ჩვენი კოდით რომ ეს გეგმა განახორციელოს.
# მაგალითი: 
# abc--d → ad


def usashlelo(str):
    st = []
    for ch in str:
        if ch == '-':
            if st: st.pop()
        else:
            st.append(ch)
    return "".join(st)
s=input("enter text: ")
print(usashlelo(s))

