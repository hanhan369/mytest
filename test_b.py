str1 = 'Python自学网'
for i in str1:
    # 当某些条件成立终止当前循环继而执行下次循环 ----continue----条件：当i取到字符自
    if i == '自':
        break
    print(i)
print("天黑了")