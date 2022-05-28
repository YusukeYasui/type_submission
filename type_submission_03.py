def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
  # 要素が一つの場合はソートの必要がないので、そのまま返却
  if len(array) == 1:
    return array

  # 配列の先頭を基準値とする
  pivot = array[0]

  # ここから記述


  #一回のソートの処理
  def one_sort(array, beginning, ending):
    #基準値の定義
    pivot = array[beginning]
    #どこまで探索したかを記録する変数を定義
    i_now = beginning
    j_now = ending
    #ループしてソートを行う
    for i in range(i_now, j_now):
      if pivot <= array[i]:
        i_now = i
        for j in reversed(range(i_now, j_now)):
          if pivot > array[j] and i < j :
            array[i], array[j] = array[j], array[i]
            j_now = j
            break
    #ソートした配列を返す
    return array
    

  #分ける境界の番号を返す関数を定義
  def partition(array, beginning, ending):
    pivot = array[beginning]
    for i in range(beginning, ending):
      if array[i] >= pivot:
        return i
        
    
  def quick_sort(array, beginning, ending):
    if beginning < ending :
      array = one_sort(array, beginning, ending)
      pivot_index = partition(array, beginning, ending)
      quick_sort(array, beginning, pivot_index)
      quick_sort(array, pivot_index+1, ending)
        
    return array
  
  #実効して値を返す
  return quick_sort(array, 0, len(array)-1)

            

    # ここまで記述

if __name__ == '__main__':
    main()