# Học viên bổ sung ngoại lệ cho phần xử lý bài toán sau:
# - Cho một list, bao gồm cả số và ký tự
# - Chương trình sẽ duyệt qua list cho đến khi tìm những số nguyên hợp lệ để thực hiện phép toán:   r = 1/(int)(giá trị của list)

lst = [1,2.35,'sdf','abc',3,4,1.2,-5,-4,0,'mnb']
lst_valid = []
for i in lst:
    try:
        if isinstance(i,int) == True:
            r = 1/i
            lst_valid.append(i)
    except Exception:
        pass
print(lst_valid)
