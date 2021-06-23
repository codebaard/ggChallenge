import requests
import matplotlib.pyplot as plt

def main():
    results = []
    t1 = []
    t2 = []
    t3 = []

    for i in range(1000):
        response = requests.get('https://gg.juliusneudecker.com/troops?size=1000')
        results.append(response.json())

    for r in results:
        t1.append(r.get('troops')[0].get('count'))
        t2.append(r.get('troops')[1].get('count'))
        t3.append(r.get('troops')[2].get('count'))

    data = [t1, t2, t3]

    fig = plt.figure(figsize = (10,7))
    ax = fig.add_axes([0, 0, 1, 1])
    bp = ax.boxplot(data)
    plt.show()

if __name__ == '__main__':
    main()