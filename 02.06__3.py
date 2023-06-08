jam= int(input("Nerka jam@  ( 1-12): "))
am_pm = int(input("am (1) te pm (2)? "))
qanak = int(input("Qani jam araj? "))
nor_jam = (jam + qanak)
if am_pm == 1:
    nor_am_pm = "am"
    nor_jam = nor_jam % 12
else:
    nor_am_pm = "pm"
print("Nor jam@:", nor_jam, nor_am_pm)
