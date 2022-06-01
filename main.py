
answer= input ('select 1 2 or 3 ').lower()
while True:
  if answer == '1' :
    import file1
  elif answer == '2':
    import file2
  elif answer == '3':
    import file3
  else:
    answer = input('1,2 or 3?')