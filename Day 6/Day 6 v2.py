# Viết chương trình tính chỉ số BMI, và đánh giá BMI của các học viên phòng Gym.
# - Người dùng tạo ra một danh sách học viên phòng gym, gồm các thông tin: MãHV, Họ và tên, Cân nặng (kg), Chiều cao (m).
# - Chương trình sẽ hiển thị chỉ số BMI kèm theo đánh giá cho từng học viên của phòng gym.

# Cách tính chỉ số BMI như sau:
#    BMI = Cân nặng / (Chiều cao * Chiều cao)
#    Bảng đánh giá BMI:
#          •  Gầy:  <18.5
#          •  Bình thường:  18.5 – 24.99
#          •  Thừa cân:  >=25


'''
Created on October 17, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

import math

# Tạo danh sách học viên phòng gym
Danh_sach_HV_phong_gym = {'HV01': ['Dương Thu Thủy', 68, 1.65], 'HV02': ['Nguyễn Văn Hưng', 75, 1.81], 'HV03': ['Lê Thái Châu', 98, 1.85], 'HV04': ['Nguyễn Trọng Hoàng', 67, 1.69], 'HV05': ['Nguyễn Tú Trinh', 51.5, 1.58], 'HV06': [
    'Đào Thùy Linh', 62, 1.60], 'HV07': ['Lê Văn Linh', 67, 1.78], 'HV08': ['Nguyễn Phúc Ngân', 55, 1.80], 'HV09': ['Trần Nhựt Khánh', 45, 1.56], 'HV10': ['Trịnh Duy Thắng', 65, 1.68], 'HV11': ['Thiều Thu Nga', 49, 1.52]}
result_list = ["Gầy", "Bình thường", "Thừa cân"]

# Xây dựng hàm tính và đánh giá BMI


def tinh_danh_gia_bmi(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao**2)
    if bmi >= 25:
        result = result_list[2]
    elif bmi >= 18.5:
        result = result_list[1]
    else:
        result = result_list[0]
    return bmi, result


# In kết quả của từng học viên phòng gym
print('---Kết quả của từng học viên phòng gym---')
print('Mã HV \t Họ và tên \t \t Chỉ số BMI \t Đánh giá BMI')
for key, value in Danh_sach_HV_phong_gym.items():
    print('{:5s} \t {:20s} \t {:.2f} \t \t {:10s}'.format(key, value[0], tinh_danh_gia_bmi(
        value[1], value[2])[0], tinh_danh_gia_bmi(value[1], value[2])[1]))


#      ---Kết quả của từng học viên phòng gym---
#  Mã HV    Họ và tên       Chỉ số BMI      Đánh giá BMI
#  HV01 Dương Thu Thủy (24.977043158861342, 'bình thường')
#  HV02 Nguyễn Văn Hưng (22.89307408198773, 'bình thường')
#  HV03 Lê Thái Châu (28.634039444850252, 'thừa cân')
#  HV04 Nguyễn Trọng Hoàng (23.458562375266975, 'bình thường')
#  HV05 Nguyễn Tú Trinh (20.62970677775997, 'bình thường')
#  HV06 Đào Thùy Linh (24.218749999999996, 'bình thường')
#  HV07 Lê Văn Linh (21.146319909102385, 'bình thường')
#  HV08 Nguyễn Phúc Ngân (16.975308641975307, 'gầy')
#  HV09 Trần Nhựt Khánh (18.49112426035503, 'gầy')
#  HV10 Trịnh Duy Thắng (23.030045351473927, 'bình thường')
#  HV11 Thiều Thu Nga (21.208448753462605, 'bình thường')
