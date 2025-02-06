import os
import shutil
import math
from PIL import Image
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QVBoxLayout, QPushButton, QCheckBox,QLineEdit, QSpinBox, \
    QLabel, QWidget
# 多行字符串，去除多余的空格和换行
hex_str_RGB565A_green = """
0000 0000 2000 2000 2000 2000 4000 4000 4000 4000 6000 6000 6000 6000 8000 8000 8000 8000 A000 A000 A000 A000 C000 C000 C000 C000 E000 E000 E000 E000
0001 0001 0001 0001 2001 2001 2001 2001 4001 4001 4001 4001 6001 6001 6001 6001 8001 8001 8001 8001 A001 A001 A001 A001 C001 C001 C001 C001 E001 E001 E001 E001
0002 0002 0002 0002 2002 2002 2002 2002 4002 4002 4002 4002 6002 6002 6002 6002 8002 8002 8002 8002 A002 A002 A002 A002 C002 C002 C002 C002 E002 E002 E002 E002
0003 0003 0003 0003 2003 2003 2003 2003 4003 4003 4003 4003 6003 6003 6003 6003 8003 8003 8003 8003 A003 A003 A003 A003 C003 C003 C003 C003 E003 E003 E003 E003
0004 0004 0004 0004 2004 2004 2004 2004 4004 4004 4004 4004 6004 6004 6004 6004 8004 8004 8004 8004 A004 A004 A004 A004 C004 C004 C004 C004 E004 E004 E004 E004
0005 0005 0005 0005 2005 2005 2005 2005 4005 4005 4005 4005 6005 6005 6005 6005 8005 8005 8005 8005 A005 A005 A005 A005 C005 C005 C005 C005 E005 E005 E005 E005
0006 0006 0006 0006 2006 2006 2006 2006 4006 4006 4006 4006 6006 6006 6006 6006 8006 8006 8006 8006 A006 A006 A006 A006 C006 C006 C006 C006 E006 E006 E006 E006
0007 0007 0007 0007 2007 2007 2007 2007 4007 4007 4007 4007 6007 6007 6007 6007 8007 8007 8007 8007 A007 A007 A007 A007 C007 C007 C007 C007 E007 E007 E007 E007 E007 E007
"""
hex_list_RGB565A_green = hex_str_RGB565A_green.split()
hex_str_RGB565A_blue = """
0000 0000 0000 0000 0100 0100 0100 0100 0100 0100 0100 0100 0200 0200 0200 0200 0200 0200 0200 0200
0300 0300 0300 0300 0300 0300 0300 0300 0400 0400 040 0400 0400 0400 0400 0400 0500 0500 0500 0500 0500 05
00 0500 0500 0600 0600 0600 0600 0600 0600 0600 0600 0700 0700 0700 0700 0700 0700 0700 0700 0800 0800 0800
 0800 0800 0800 0800 0800 0900 0900 0900 0900 0900 0900 0900 0900 0A00 0A00 0A00 0A00 0A00 0A00 0A00 0A00 
0B00 0B00 0B00 0B00 0B00 0B00 0B00 0B00 0C00 0C00 0C00 0C00 0C00 0C00 0C00 0C00 0D00 0D00 0D00 0D00 0D00 0D00 0D00 0D00 0E00 0E00 0E00 0E00 0E00 0E00 0E00 0E00 
0F00 0F00 0F00 0F00 0F00 0F00 0F00 0F00 1000 1000 1000
 1000 1000 1000 1000 1000 1100 1100 1100 1100 1100 1100 1100 1100 1200 1200 1200 1200 1200 1200 1200 1200 
1300 1300 1300 1300 1300 1300 1300 1300 1400 1400 1400
 1400 1400 1400 1400 1400 1500 1500 1500 1500 1500 1500 1500 1500 1600 1600 1600 1600 1600 1600 1600 1600 
1700 1700 1700 1700 1700 1700 1700 1700 1800 1800 1800
 1800 1800 1800 1800 1800 1900 1900 1900 1900 1900 1900 1900 1900 1A00 1A00 1A00 1A00 1A00 1A00 1A00 1A00 
1B00 1B00 1B00 1B00 1B00 1B00 1B00 1B00 1C00 1C00 1C00
 1C00 1C00 1C00 1C00 1C00 1D00 1D00 1D00 1D00 1D00 1D00 1D00 1D00 1E00 1E00 1E00 1E00 1E00 1E00 1E00 1E00 
1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00
 1F00 
"""
hex_list_RGB565A_blue = hex_str_RGB565A_blue.split()
hex_str_RGB565A_red  = """
0000 0000 0000 0000 0100 0100 0100 0100 0100 0100 0100 0100 0200 0200 0200 0200 0200 0200 0200 0200
0300 0300 0300 0300 0300 0300 0300 0300 0400 0400 040 0400 0400 0400 0400 0400 0500 0500 0500 0500 0500 05
00 0500 0500 0600 0600 0600 0600 0600 0600 0600 0600 0700 0700 0700 0700 0700 0700 0700 0700 0800 0800 0800
 0800 0800 0800 0800 0800 0900 0900 0900 0900 0900 0900 0900 0900 0A00 0A00 0A00 0A00 0A00 0A00 0A00 0A00 
0B00 0B00 0B00 0B00 0B00 0B00 0B00 0B00 0C00 0C00 0C00 0C00 0C00 0C00 0C00 0C00 0D00 0D00 0D00 0D00 0D00 0D00 0D00 0D00 0E00 0E00 0E00 0E00 0E00 0E00 0E00 0E00 
0F00 0F00 0F00 0F00 0F00 0F00 0F00 0F00 1000 1000 1000
 1000 1000 1000 1000 1000 1100 1100 1100 1100 1100 1100 1100 1100 1200 1200 1200 1200 1200 1200 1200 1200 
1300 1300 1300 1300 1300 1300 1300 1300 1400 1400 1400
 1400 1400 1400 1400 1400 1500 1500 1500 1500 1500 1500 1500 1500 1600 1600 1600 1600 1600 1600 1600 1600 
1700 1700 1700 1700 1700 1700 1700 1700 1800 1800 1800
 1800 1800 1800 1800 1800 1900 1900 1900 1900 1900 1900 1900 1900 1A00 1A00 1A00 1A00 1A00 1A00 1A00 1A00 
1B00 1B00 1B00 1B00 1B00 1B00 1B00 1B00 1C00 1C00 1C00
 1C00 1C00 1C00 1C00 1C00 1D00 1D00 1D00 1D00 1D00 1D00 1D00 1D00 1E00 1E00 1E00 1E00 1E00 1E00 1E00 1E00 
1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00 1F00
 1F00 """
hex_list_RGB565A_red = hex_str_RGB565A_red.split()

class ImageToCConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Image to C File Converter")
        self.setStyleSheet("background-color: #f7f7f7;")  # Set background color
        layout = QVBoxLayout()

        title_label = QLabel("Image to C File Converter")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2d89ef;")  # Set title color
        layout.addWidget(title_label)

        self.select_folder_btn = QPushButton("Select Image Folder")
        self.select_folder_btn.setFont(QFont("Arial", 12))
        self.select_folder_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        self.select_folder_btn.clicked.connect(self.select_folder)
        layout.addWidget(self.select_folder_btn)

        self.single_bin_checkbox = QCheckBox("Output individual image bin files")
        self.single_bin_checkbox.setFont(QFont("Arial", 12))
        self.single_bin_checkbox.setStyleSheet("margin: 10px;")
        layout.addWidget(self.single_bin_checkbox)

        self.offset_label = QLabel("Offset Address (e.g., 0x90100000):")
        self.offset_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.offset_label)

        self.offset_input = QLineEdit("0x90100000")
        self.offset_input.setFont(QFont("Arial", 12))
        self.offset_input.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px;")
        layout.addWidget(self.offset_input)

        self.generate_btn = QPushButton("Generate C File")
        self.generate_btn.setFont(QFont("Arial", 12))
        self.generate_btn.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")
        self.generate_btn.clicked.connect(self.generate_c_file)
        layout.addWidget(self.generate_btn)

        self.setLayout(layout)

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if self.folder_path:
            QMessageBox.information(self, "Folder Selected", f"Selected folder: {self.folder_path}")

    def delete_existing_output(self, bin_folder, output_c_file):
        if os.path.exists(bin_folder):
            shutil.rmtree(bin_folder)
        if os.path.exists(output_c_file):
            os.remove(output_c_file)


    def calculate_r5(self, input_value):
        if 0 <= input_value < len(hex_list_RGB565A_red):
            hex_value = hex_list_RGB565A_red[input_value]  # 获取 16 进制字符串
            bin_value = bin(int(hex_value, 16))[2:].zfill(16)  # 确保转换为 16 位二进制
            middle_five = bin_value[3:8]  # 取中间 5 位（二进制索引 3~7）
            return int(middle_five, 2)  # 转换为整数返回

    def calculate_b5(self, input_value):
        if 0 <= input_value < len(hex_list_RGB565A_blue):
            hex_value = hex_list_RGB565A_blue[input_value]  # 获取 16 进制字符串
            bin_value = bin(int(hex_value, 16))[2:].zfill(16)  # 确保转换为 16 位二进制
            middle_five = bin_value[3:8]  # 取中间 5 位（二进制索引 3~7）
            return int(middle_five, 2)  # 转换为整数返回

    def calculate_g6(self, input_value):
            """ 获取索引对应的 16 进制数的二进制前三位和后三位 """
            if 0 <= input_value < len(hex_list_RGB565A_green):
                hex_value = hex_list_RGB565A_green[input_value]  # 获取 16 进制字符串
                bin_value = bin(int(hex_value, 16))[2:].zfill(16)  # 转换为 16 位二进制
                first_three = int(bin_value[:3], 2)  # 前三位转换为整数
                last_three = int(bin_value[-3:], 2)  # 后三位转换为整数
                g6 = (first_three << 3) | last_three  # 组合 g1g2g3 和 g4g5g6
                return g6
    def image_to_bin(self, image_path):
        """Convert an image to custom binary format."""
        with Image.open(image_path) as img:
            img = img.convert("RGBA")
            width, height = img.size
            custom_data = bytearray()

            for pixel in img.getdata():
                r, g, b, a = pixel
                # 计算 R5/G6/B5
                R5 = self.calculate_r5(r)
                G6 = self.calculate_g6(g)
                B5 = self.calculate_b5(b)

                # 分离绿色的高 3 位 (g1g2g3) 和低 3 位 (g4g5g6)
                G_high = (G6 >> 3) & 0b111  # g1g2g3
                G_low = G6 & 0b111  # g4g5g6

                # # 打印调试信息
                # print(f"Pixel R={r}, G={g}, B={b}, A={a}")
                # print(f"Calculated R5={R5:05b}, G6={G6:06b}, B5={B5:05b}")
                # print(f"G_high (g1g2g3)={G_high:03b}, G_low (g4g5g6)={G_low:03b}")

                # 组装字节数据
                byte0 = (G_high << 5) | B5  # Byte 0: G4G5G6 和 B1B2B3B4B5
                byte1 = (R5 << 3) | G_low  # Byte 1: R1R2R3R4R5 和 G1G2G3
                byte2 = a  # Byte 2: Alpha

                # 添加到最终数据
                custom_data.extend([byte0, byte1, byte2])

            return custom_data, width, height, len(custom_data)

    def generate_c_file(self):
        if not hasattr(self, 'folder_path') or not self.folder_path:
            QMessageBox.warning(self, "Error", "Please select a folder first!")
            return

        bin_folder = os.path.join(self.folder_path, "bin")
        output_c_file = os.path.join(self.folder_path, "images_all.c")

        # Delete existing outputs if they exist
        self.delete_existing_output(bin_folder, output_c_file)

        # Create the bin folder
        os.makedirs(bin_folder, exist_ok=True)

        merged_bin_path = os.path.join(bin_folder, "images_all.bin")
        offset_address = self.offset_input.text().strip()

        try:
            int(offset_address, 16)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid offset address! Please enter a valid hexadecimal value.")
            return
        c_file_content =f"""#include <lvgl.h>
#define IMG_ADD_FLASH  {offset_address}

"""

        #header_size = self.header_size_spinbox.value() * 1024 * 1024  # Convert MB to bytes
        header_size = 0
        current_address = header_size

        with open(merged_bin_path, "wb") as merged_bin:
            # Add the header filled with 0xFF
            merged_bin.write(bytearray([0xFF] * header_size))

            for image_name in os.listdir(self.folder_path):
                image_path = os.path.join(self.folder_path, image_name)
                if os.path.isfile(image_path) and image_name.lower().endswith(('.png', '.jpg', '.bmp')):
                    # Convert image to custom binary format
                    base_name = os.path.splitext(image_name)[0]
                    custom_data, width, height, data_size = self.image_to_bin(image_path)

                    # Write custom data to merged binary file
                    merged_bin.write(custom_data)

                    # Output individual bin files if checkbox is checked
                    if self.single_bin_checkbox.isChecked():
                        single_bin_path = os.path.join(bin_folder, f"{base_name}.bin")
                        with open(single_bin_path, "wb") as single_bin:
                            single_bin.write(custom_data)

                    # Write struct to C file
                    c_file_content += f"const lv_img_dsc_t ui_img_{base_name}_png = {{\n"
                    c_file_content += f"    .header.always_zero = 0,\n"
                    c_file_content += f"    .header.w = {width},\n"
                    c_file_content += f"    .header.h = {height},\n"
                    c_file_content += f"    .data_size = {data_size},\n"
                    c_file_content += f"    .header.cf = LV_IMG_CF_TRUE_COLOR_ALPHA,\n"
                    c_file_content += f"    .data = (const uint8_t *)(0x{current_address:08X}UL+IMG_ADD_FLASH)\n"
                    c_file_content += "};\n\n"

                    current_address += data_size

        # Save to output C file
        with open(output_c_file, "w") as c_file:
            c_file.write(c_file_content)

        QMessageBox.information(self, "Success",
                                f"C file and merged binary generated: {output_c_file}, {merged_bin_path}")


if __name__ == "__main__":
    app = QApplication([])
    converter = ImageToCConverter()
    converter.show()
    app.exec_()
