import matplotlib.pyplot as plt


def return_chart(chart_data):
    name = "ffile.png"
    exception_name = "Error"

    try:
        plt.plot(list(map(int, chart_data.split(' '))))
        plt.savefig(name)
        return open(name, "rb")
    except ValueError:
        return open("Error.png", "rb")