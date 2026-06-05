blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


def display_inventory(inventory):

    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    print("--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("--------------------------------------------------------------")

    total_volume = 0

    for record in inventory:

        data = record.rsplit("-", 2)

        left_part = data[0]
        volume = data[1]
        expiry = data[2]

        info = left_part.split("-", 2)

        bag_id = info[0]
        donor = info[1]
        blood_group = info[2]

        total_volume += int(volume)

        print(
            f"{bag_id:<6} | "
            f"{donor:<16} | "
            f"{blood_group:<8} | "
            f"{volume} ml".ljust(9) + " | "
            f"{expiry}"
        )

    print("--------------------------------------------------------------")
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):

    print("\n--- NHẬP TÚI MÁU MỚI ---")

    bag_id = input("Nhập mã túi máu mới: ").strip().upper()

    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for record in inventory:
        if record.startswith(bag_id):
            print(f"\nLỗi: Mã túi máu {bag_id} đã tồn tại! Vui lòng nhập mã khác.")
            return

    donor = input("Nhập tên người hiến: ").strip().title()

    if donor == "":
        print("\nLỗi: Tên người hiến không được để trống!")
        return

    blood_group = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()

    if not volume.isdigit() or int(volume) <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_record = "-".join([
        bag_id,
        donor,
        blood_group,
        volume,
        expiry
    ])

    inventory.append(new_record)

    print(f"\nThành công: Đã nhập túi máu {bag_id} vào kho!")


def update_expiry(inventory):

    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    bag_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()

    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for index in range(len(inventory)):

        data = inventory[index].rsplit("-", 2)

        left_part = data[0]
        volume = data[1]

        info = left_part.split("-", 2)

        if info[0] == bag_id:

            new_expiry = input("Nhập ngày hết hạn mới: ").strip()

            new_record = "-".join([
                info[0],
                info[1],
                info[2],
                volume,
                new_expiry
            ])

            inventory[index] = new_record

            print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {bag_id}!")
            return

    print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")


def remove_blood_bag(inventory):

    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    bag_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()

    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for index in range(len(inventory)):

        data = inventory[index].split("-")

        if data[0] == bag_id:
            inventory.pop(index)

            print(f"\nThành công: Đã xuất túi máu {bag_id} khỏi kho!")
            return

    print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")


def main():

    while True:

        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")

        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
            continue

        if choice == 1:
            display_inventory(blood_inventory)

        elif choice == 2:
            add_blood_bag(blood_inventory)

        elif choice == 3:
            update_expiry(blood_inventory)

        elif choice == 4:
            remove_blood_bag(blood_inventory)

        elif choice == 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


main()


# Chương trình quản lý kho máu bằng List chứa các chuỗi. Mỗi chuỗi lưu thông tin
# túi máu theo định dạng Mã-Tên-NhómMáu-ThểTích-NgàyHếtHạn. Các chức năng được
# tách thành các hàm riêng gồm xem danh sách, thêm túi máu, cập nhật ngày hết hạn
# và xuất/hủy túi máu. Khi cập nhật ngày hết hạn, chương trình phải dùng split()
# để tách chuỗi thành List, thay đổi dữ liệu rồi dùng join() ghép lại vì String
# trong Python là immutable (không thể sửa trực tiếp). Chương trình cũng kiểm tra
# dữ liệu đầu vào như mã trùng, mã rỗng và thể tích không hợp lệ để đảm bảo tính
# chính xác của kho máu.