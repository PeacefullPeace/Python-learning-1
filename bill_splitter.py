running_total = 0

num_of_friends = int(input('How many friends? '))

appetizers = float(input('How much for appetizers? '))
main_courses = float(input('How much for main courses? '))
desserts = float(input('How much for desserts? '))
drinks = float(input('How much for drinks? '))

running_total += appetizers + main_courses + desserts + drinks

print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends

print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)