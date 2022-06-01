while True:
  time= input('what time is it? day/afternoon/evening/night ').lower()
  if time == 'day':
    print ('you eat breakfast')
    break
  elif time == 'afternoon':
    print('you eat lunch')
    break
  elif time =='evening':
    print('you eat snacks and watch movies' )
    break
  elif time=='night':
    print ('you eat dinner')
    break
  elif time == 'i dont know'or time=='idk':
    print ('okay')
    import main
    break
  else:
    print('day afternoon or evening')