def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    #左端と右端の初期設定
    left = 0
    right = len(sorted_array) - 1

    #二部探索
    while left <= right:
        mid_number = (left + right) // 2  #mid_numberはsorted_arrayの真ん中の値の番号
        if sorted_array[mid_number] == target_number:
            return sorted_array[mid_number]

        elif sorted_array[mid_number] < target_number:
            left = mid_number + 1

        else:
            right = mid_number - 1


    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()