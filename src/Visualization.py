import matplotlib.pyplot as plt
import matplotlib

def ShowGrapgh(crowd_dict: dict):
    values = [float(x) for x in crowd_dict.values()]
    str_values = [str(value) for value in list(crowd_dict.values())]

    plt.rcParams['font.family'] = 'Alibaba PuHuiTi 2.0'  # 替换为你选择的字体
    plt.yticks(values, str_values)
    bars = plt.bar(list(crowd_dict.keys()), list(crowd_dict.values()))
    #plt.bar_label(b1, labal_type = "center")

    count = 0
    values = list(crowd_dict.values())
    for bar in bars:
        #print(str(values[count].numerator) + "/" + str(values[count].denominator))
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height(), va = 'bottom', s = str(values[count]))
        count += 1
    plt.show()