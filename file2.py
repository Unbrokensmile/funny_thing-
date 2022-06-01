while True:
  typing=input('are you typing?').lower()
  if typing== 'yes' or typing=='yeah':
    print('you touch your keyboard')
    break
  elif typing=='no' or typing=='nope':
    print('you are not touching your keyboard')
    break
  else:
    print('yes or no?')
