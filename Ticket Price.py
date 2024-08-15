name = input('Please Enter Your Name:- ')
age = int(input('Please Enter Your Age:- '))

if age<=0:
    print(f'Hello {name} please enter a valid age')
elif 0<age<=3:
    print(f'Congratulations {name} your ticket price is :- Free \U0001F642')
elif 3<age<=10:
    print(f'Hello {name} your ticket price is:- 150 RS')
elif 10<age<=60:
    print(f'Hello {name} your ticket price is:- 250 RS')
else:
    print(f'Hello {name} your ticket price is:- 200 RS')
