# ----------------------------------HOMEWORK--------------------------------

# 149
# def counter(filname):
#     try:
#         with open(filname, 'r') as file:
#             res = file.readlines()
#             for i in range(min(10, len(res))):
#                 print(res[i])
#     except FileNotFoundError:
#         return 'No file'
# print(counter(input('Enter file name: ')))   

# 153
# with open('myfile.txt', 'r') as file: 
#     data = file.read()
#     data = data.split('\n')
# data.sort(key = len)
# print(data[-1])


# # 155
# def counter(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#         res = res.replace('\n', ' ')
#         res = res.split(' ')
#         mydict = {}
#         for i in res:
#             mydict[i] = res.count(i)
#             key = sorted(mydict, key=mydict.get)[-1]
#             return mydict
#     except FileNotFoundError:
#             return 'No file'
# print(counter(input('Enter file name: ')))

# 156
# count = 0
# while True:
#     number = input('Enter number: ')
#     if number =="":
#         break
#     try:
#         numbers = float(number)
#         count += numbers
#         print(count)
#     except ValueError:
#         print('Xndrum enq mutqagfreq tiv')


        
# i = 1 
# value = 0 
 
# while i < 32: 
#     for j in range(1,i): 
#       value = value + 1 
#     i = i * 2 
#     print(value) 



# -------------------------------Test--------------------
# 
#  1 - 
# 2 - 
# def bin(n):
#     if n ==1:
#         return '1'
#     else:
#         return bin(n // 2) + str(n % 2)
# print(bin(45))

# 4 - Համակարգիչը էլեկտրոնային սարք է, որը շահարկում է տեղեկատվությունը կամ տվյալները: Այն ունի տվյալների պահպանման, առբերման և մշակման հնարավորություն


# 5 -  Teksty tvin linum e menak bazmapatkel  texsty texstin  menak gumarel

# 6- E
# 7 - B,D
# 8 - C
# 9 - A,D
# 10 - C
# 11 - 0
# 12 - 1
# 13 - 4
# 14 - 5
# 15 - Xosqy veraberum e loxacox tverin, erb menq  mutqagrum enq 0.1 tivy, 0.1i erkuakat patkery jshgrit che hamakargchi hishoxutyaN mej , hetevabar
#  Հետևաբար, երբ մի քանի անգամ գումարում եք 0,1-ը, փոքր կլորացման սխալները կարող են կուտակվել, ինչը հանգեցնում է նրան, որ գումարը շատ փոքր է զիջում 1,0-ի ճշգրիտ արժեքին

# 16 - Nman xndiry lucelu hamar anhrajesht e mer hashvarkvac gumary hamematel ayl gumari het ; Ev aydpes karox enq stugel ardyoq arjeqneri minvhev tarberutyunty gtnvum e ymduneli mijakayqum te voch:
# 17 - E
# 18 - 8 pre-tested - stuguma nor ashxtatum
    #post - tested - gone mek angam ashxatum e nor e tpum
# 19 -some_function
# 20 - z, x, y
# 21 - a, b, c
# 22 - [10,5]
# 23-
# 24-
# 25-
# 26
# 30-
# 31 - Տվյալների կառուցվածքը տվյալների կազմակերպման և պահպանման միջոց է՝ գործողություններ արդյունավետ իրականացնելու համար:
# 32 - list, dict
# 33-
# 34 - D
# 35 - Տեքստային ֆայլերը տվյալները պահում են որպես մարդու կողմից ընթեռնելի տեքստ: Դրանք պարունակում են նիշեր, որոնք կոդավորված են հատուկ նիշերի կոդավորման միջոցով (օրինակ՝ ASCII կամ UTF-8)
    #  Երկուական ֆայլերը տվյալները պահում են մարդու կողմից ընթեռնելի ձևաչափով: Դրանք կարող են պարունակել բայթերի ցանկացած հաջորդականություն, ներառյալ թվային տվյալներ, պատկերներ, գործարկվող կոդ կամ ցանկացած այլ տեսակի տեղեկատվություն: 
# 36 - A
# 37 -
# 38 - E 
# 39 'a' - karoxanum eq texti vra popoxutyunner  anenq inch vor ba avelacnenq kam jnjenq
#     'w-amboxjutyamb poxum e texti parunakutyuny nor ban grelov ev henc qo nor gracn etpum filum naxkiny jnjelov

# 40  1  Bubble Sort  2 Merge Sort 3 Quick Sort
# 41 -E
# 42 - D
# 43 - ֆունկցիայի միջև որոշիչ տարբերությունը կայանում է նրանում, որ  տարբեր ձեվ են խնդիրը հաշվարկում եվ լուծում :

# 1. Ռեկուրսիվ ֆունկցիա։
#    - Ռեկուրսիվ ֆունկցիան այն ֆունկցիան է, որն իրեն կանչում է իր կատարման ընթացքում։
# Ոչ ռեկուրսիվ (Իտերատիվ) ֆունկցիա
# Ոչ ռեկուրսիվ կամ կրկնվող ֆունկցիան օգտագործում է օղակներ (ինչպես օրինակ՝ for կամ while օղակները)՝ մի քանի հրահանգներ կատարելու համարվ


# data = [5, 4, 3, 1, 2, 0, 1]

# for i in range(0, len(data)):
#     print(data)