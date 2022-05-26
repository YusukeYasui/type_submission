for num in range(1, 101):
    string = ''

    # ここから記述
#3かつ5の倍数の時の出力
    if num % 15 == 0:
      string = 'FizzBuzz'

#3の倍数の出力
    elif num % 3 == 0:
      string = 'Fizz'

#3の倍数の出力
    elif num % 5 == 0:
      string = 'Buzz'

#3でも5でも無い数字の出力
    else:
      string =  str(num)

    # ここまで記述
    print(string)