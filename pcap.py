"""
该工具依赖wireshark，linux需要执行安装命令：yum install -y wireshark-devel
"""
import os
import subprocess

work_dir = os.path.dirname(os.path.realpath(__file__))


class PackageTools(object):
    def __init__(self):
        self.work_dir = os.path.dirname(os.path.realpath(__file__))
        self.temp_dir = os.path.join(self.work_dir, "pcap_temp")
        self.temp_file = os.path.join(self.temp_dir, "hex_interval.txt")
        self.check_and_mkdir_temp()
        self.column_len = 2
        self.line_len = 16 * 2
        self.pkg_pre_len = 6

    def check_and_mkdir_temp(self):
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)

    def change_hex_to_pcap(self, hex_list, file_pcap):
        self.change_hex_interval(hex_list)
        cmd = "text2pcap {} {}".format(self.temp_file, file_pcap)
        subprocess.call(cmd, shell=True)

    def change_hex_interval(self, text_hex_list):
        """
        输入二进制列表，输出标准二进制文件（临时）
        :param text_hex_list:c
        :return:
        """
        with open(self.temp_file, "w") as f2:
            for line in text_hex_list:
                if line:
                    f2.write(self.hex_change_txt(line))

    def hex_change_txt(self, text):
        index = 0
        s = ""
        for i in self.cut(text, self.line_len):
            line = " ".join([j for j in self.cut(i, self.column_len)])
            s = "{}{} {}{}".format(s, self.index_to_change(index), line, "\n")
            index += 10
        return s

    def index_to_change(self, index):
        return str(index).rjust(self.pkg_pre_len, "0")

    @staticmethod
    def cut(l, line_len):
        return [l[i : i + line_len] for i in range(0, len(l), line_len)]

    def main(self, pkt_list, name_of_pcap):
        file_pcap = os.path.join(self.temp_dir, name_of_pcap)
        PackageTools().change_hex_to_pcap(pkt_list, file_pcap)

        return file_pcap


if __name__ == "__main__":
    list_t = [
        "88860383d20300e04cd4013f08004500004e001a00008011f273c0a863a7c0a8631900890089003aef9388890000000100000000000020434b4141414141414141414141414141414141414141414141414141414141410000210001"
    ]
    PackageTools().main(list_t, "ts.pcap")
