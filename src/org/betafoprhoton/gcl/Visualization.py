import matplotlib.pyplot as plt
import matplotlib

def ShowGrapgh(crowd_dict: dict, font: str = "Alibaba PuHuiTi 2.0"):
    values = [float(x) for x in crowd_dict.values()]
    str_values = [str(value) for value in list(crowd_dict.values())]

    plt.rcParams["font.family"] = font
    plt.yticks(values, str_values)
    bars = plt.bar(list(crowd_dict.keys()), list(crowd_dict.values()))

    count = 0
    values = list(crowd_dict.values())
    for bar in bars:
        #print(str(values[count].numerator) + "/" + str(values[count].denominator))
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height(), va = "bottom", s = str(values[count]))
        count += 1
    plt.show()