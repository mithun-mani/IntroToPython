'''
CS_100MidtermS_MIthunManivannan
October 10, 2018
'''
#1 - C
#2 - C
#3 - E
#4 - D
#5 - E
#6 - B
#7 - C
#8 - B
#9 - A
#10 - D
#11A
def stair(t, tread_size, riser_height):
    t.down()
    t.forward(tread_size)
    t.right(90)
    t.forward(riser_height)
    t.left(90)
#11B
def staircase(turt, num_stairs, tread_size, riser_height):
    for i in range(num_stairs):
        stair(turt, tread_size, riser_height)
#12
def vowel_tracker(words):
    vowelString = "aeiouAEIOU"
    startVowel = 0
    endVowel = 0
    for index in words:
        if index[0] in vowelString:
            startVowel += 1
        if index[-1] in vowelString:
            endVowel += 1
    newString = [startVowel, endVowel]
    return newString
#13
def month_info(medium_length):
    month = input("What month is it? ")
    days = int(input("How many days in " + month +": "))
    if days == medium_length:
        length = "medium"
    elif days > medium_length :
        length = "long"
    elif days < medium_length:
        length = "short"
    print (month + " is " + length)
    return month
