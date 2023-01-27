# Task1 Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
# համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։
import math


def task1(n1, n2, n):
    d = n2 - n1
    answer = n1 + d * (n - 1)
    return answer


# print(task1(2.5, 3, 5))


# Task2 CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
# չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
# ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
# ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
# որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
# հայտնված թվերի գումարը։


def numbers(string):
    summ = 0
    arr = string.split(" ")
    for n in arr:
        if n.isdigit():
            summ += int(n)
    return summ


# print(numbers("1 bread, 2 apples, 5 oranges, 7 snacks"))


# Task3 Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
# ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
# դեփքում:


def is_sorted(n1, n2, n3):
    if (n1 > n2 > n3) or (n1 < n2 < n3):
        print("sorted")
        return
    print("unsorted")


# is_sorted(1, 0.5, 0)


# Task4 Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
# կատարյալ թիվ է, թե ոչ։


def is_perfect(n):
    sum1 = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            sum1 += i
    if sum1 == n:
        print(n, "is a perfect numer")
    else:
        print(n, "is not a perfect numer")


# is_perfect(497)


# Task5 Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա
# էլեմենտների գումարը։

def list_sum(arr):
    summ = 0
    for i in arr:
        summ = summ + i
    return summ


# print(list_sum([1,2,4,10]))


# Task6 Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
# ցուցակի ամենամեծ էլեմենտը։

def max_of_array(arr):
    maxx = arr[0]
    for i in arr:
        if i > maxx:
            maxx = i
    return maxx


# print(max_of_array([1, 10, 4, 5, 12]))


# Task7 Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
# էլեմենտները։


def remove_items(arr, n):
    for i in arr:
        if i == n:
            arr.remove(i)
    return arr


# print(remove_items([1, 4, 5, 6, 4, 2, 3, 2, 4], 4))


# Task8 Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
# էլեմենտների արտադրյալը։


def mul(arr):
    m = 1
    for i in arr:
        m = m * i
    return m


# print(mul([1,2,3,4]))

# Task9 Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
# բազմապատիկ է։
def reveres_str(string):
    a = ""
    if len(string % 4 == 0):
        for i in range(len(string) - 1, -1, -1):
            a += string[i]
        return a
    return string


# print(reveres_str("abc"))


# Task10 fibonacci recursive

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(6))


# Task10 fibonacci iterative

def fib2(n):
    summ = 0
    n1 = 0
    n2 = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        while n > 2:
            summ = n1 + n2
            n1 = n2
            n2 = summ
            n -= 1
    return summ


# print(fib2(4))


# Task11 least common multiple

def lcm(n1, n2):
    if n1 > n2:
        a = n1
    else:
        a = n2
    # print(a, "aa")
    while True:
        if a % n2 == 0 and a % n1 == 0:
            break
        else:
            a += 1
    return a


# print(lcm(10, 6))


# Task12 Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
# Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է


def is_palindrome(n):
    a = n
    summ = 0
    while n != 0:
        rem = n % 10
        summ = summ * 10 + rem
        n = n // 10
    if summ == a:
        return True
    else:
        return False


def next_smallest_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n


# print(next_smallest_palindrome(123))


# 13 ?????????????????????????????

def coordinates(string):
    d = {"x0": 0, "y0": 0}
    for i in string:
        if i == "l":
            d["x0"] -= 1
        elif i == "r":
            d["x0"] += 1
        elif i == "u":
            d["y0"] += 1
        elif i == "d":
            d["y0"] -= 1
    return d


# print(coordinates("rrrd"))

# Task14  Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:

def one_cycle(list1, list2):
    length = len(list1)
    list3 = list1 * 2

    for x in range(0, len(list1)):
        a = 0
        for y in range(x, x + len(list1)):
            if list2[a] == list3[y]:
                a += 1
            else:
                break

        if a == len(list1):
            return True

    return False


# print(one_cycle([3, 1, 2], [1, 2, 3]))


# Task15 Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:


def biggest(n):
    num = 0
    string = str(n)
    for i in range(len(string)):
        s = string[0: i] + string[i + 1: len(string)]
        new_num = int(s)
        if new_num > num:
            num = new_num
    return num


# print(biggest(2505123))


# Task16 Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
# բաղկացած միայն առաջին tuple֊ի թվերից։


def tuple_of_numbers(t):
    new_t = ()
    for i in t:
        if type(i) == int or type(i) == float:
            new_t = new_t + (i,)
    return new_t


# print(tuple_of_numbers((1, "a", 5, [1, 2], 12, 5.2, -10)))

# Task17 Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
# է ստացած արժեքը tuple մեջ։


def tuple_item(t, item):
    sample_list = list(t)
    sample_list.append(item)
    tuple1 = tuple(sample_list)
    return tuple1


# print(tuple_item((0, 1, 2), 3))


# Task18 Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները
# ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։
def tuple_string(t1):
    string = ""
    for i in t1:
        string += str(i) + "-"
    return string


# print(tuple_string((1, 2, 3, 4)))


# Task19 Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
# len() ֆունկցիա֊ի օգտագորձմամբ։

def list_length(l):
    index = 0
    for i in l:
        index += 1
    return index


# print(list_length([1, 2, 3, 4, 5]))


# Task20

def is_lucky(n):
    temp = n
    index = 0
    sum1 = 0
    right = 0
    while n != 0:
        sum1 += n % 10
        index += 1
        n = n // 10
    index = math.ceil(index / 2)
    print(index)
    while index > 0:
        right += temp % 10
        temp = temp // 10
        index -= 1
    if right * 2 == sum1:
        return True
    return False


# print(is_lucky(12300061))


# Task21 Euler function

def euler(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count


def gcd(a, b):
    if a == 0 or b == 0:
        return False

    if a == b:
        return a

    if a > b:
        return gcd(a - b, b)

    return gcd(a, b - a)


# print(euler(11))


# Task22

def is_anagram(str1, str2):
    s1 = sorted(str1)
    s2 = sorted(str2)
    if s1 == s2:
        return True
    return False


def anagrams(l):
    new_list = []
    for i in range(len(l) - 1, 0, -1):
        if is_anagram(l[i], l[i - 1]):
            new_list.append(l[i])
    for i in new_list:
        l.remove(i)
    return l


print(anagrams(["z", "z", "z", "gsw", "gsw", "wsg", "gsw", "krptu"]))
print(anagrams(["abba", "baba", "bbaa", "cd", "cd"]))


# Task23

def names_and_hates(names, hates):
    d = {}
    for hate in hates:
        for name in names:
            d[hate] = name
            names.remove(name)
            break
    la = list(d)
    la.sort()
    la.reverse()
    sorted_d = {i: d[i] for i in la}
    print(sorted_d.values())


# names_and_hates(["m", "j", "a"], [120, 160, 170])


# Task24


def rank_teams(votes):
    answer = ""
    votes_dict = {}
    for vote in votes:
        for rank in range(len(vote)):
            team = vote[rank]
            if team not in votes_dict:
                votes_dict[team] = 0
            votes_dict[team] += rank
    votes_dict = dict(sorted(votes_dict.items(), key=lambda item: item[1]))
    for i in votes_dict.keys():
        answer += i
    return answer


# print(rank_teams(["HRSTUCX", "AB"]))
