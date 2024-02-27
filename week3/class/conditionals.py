#if
num = 20
if num >= 20:
    print('number is twenty')

bill = 2500
discount = 100

if bill > 2000:
    print('bill is greater than 2000')
    final_bill = bill - discount
print('final bill: ' + str(final_bill))

#if...else
#if weekday:
#   print('wake up early')
#else:
#   print('sleep in')

#if...elif...else
grade = 83

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

#match case
number = '9'

match number:
    case '1':
        print('one')
    case '2':
        print('two')
    case _:
        print('unknown')

http_status = 501

if http_status == 200 or http_status == 201:
    print('success')
elif http_status == 400:
    print('bad request')
elif http_status == 404:
    print('not found')
elif http_status == 500 or http_status == 501:
    print('server error')
else:
    print('unknown')

#match refactor
match http_status:
    case 200 | 201:
        print('success')
    case 400:
        print('bad request')
    case 404:
        print('not found')
    case 500 | 501:
        print('server error')
    case _:
        print('uknown')
