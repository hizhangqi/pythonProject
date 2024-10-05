import matplotlib.pyplot as plt


def showPlt():
    dot = [3, 4, 2, 1]
    plt.plot(dot)
    plt.ylabel('The name of the Y axis')
    plt.xlabel(' The name of the X axis')
    plt.title("The name of the image's Theme")
    plt.show()
    plt.savefig('hehe.jpg')


if __name__ == '__main__':
    showPlt()
