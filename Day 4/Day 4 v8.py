# Học viên viết chương trình xử lý ngày, tháng, năm bằng cách sử dụng hàm thư viện Datetimes.
# - Người dùng nhập vào ngày, tháng, năm (hợp lệ) 
# - Chương trình sẽ xử lý ngày, tháng, năm, và in kết quả theo các yêu cầu sau:
#              + Xuất ngày theo định dạng ngày – tháng - năm 
#              + Cho biết năm được nhập vào có phải là năm nhuận hay không? 
#              + Cho biết ngày/tháng/năm nhập vào là thứ mấy? 
#              + Cho biết tháng nhập vào có bao nhiêu ngày?

from datetime import datetime
import calendar

ngay = int(input("Ngay: "))
thang = int(input("Thang: "))
nam = int(input("Nam: "))

x = datetime(nam,thang,ngay)
print("Xuất theo định dạng ngày - tháng - năm: ", x.strftime("%d-%m-%Y"))

if calendar.isleap(nam):
    print("Năm " + str(nam) + " không phải là năm nhuận")
else:
    print("Năm " + str(nam) + " là năm nhuận")

ngay_trong_tuan = ["Thứ 2","Thứ 3","Thứ 4","Thứ 5","Thứ 6","Thứ 7","Chủ nhật"]
print("Ngày "+ x.strftime("%d-%m-%Y") + " là "  + ngay_trong_tuan[calendar.weekday(nam,thang,ngay)])

print("Tháng " + str(thang) + " của năm " + str(nam) + " có " + str(calendar.monthrange(nam,thang)[1]) + " ngày")

