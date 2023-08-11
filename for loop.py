#friends = ['mojeeb','edrees','ahmad','jawad','mahmod']
#numbers = ['1','2','3','4','5']
#for friend in friends:
   # for number in numbers:
   #      print('fuck you '+friend + ' '+number)
names=['ahmad','mahmod','mojeeb','rahman']
names1=['shambo','nasir','momo','monir']
mas='wellcome to the party my friend'
names.extend(names1)
for index in range(2):
    names.append(input("please enter friends name to invite"))
for name in names:
    msgs=f'{name}! {mas}'
    print(msgs)
   
