import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_numbers(count, upper_limit):
    return random.sample(range(1, upper_limit + 1), count)

def counting_sort(numbers, exp, bar_container):
    n = len(numbers)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (numbers[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (numbers[i] // exp) % 10
        output[count[index] - 1] = numbers[i]
        count[index] -= 1

    for i in range(n):
        numbers[i] = output[i]
        bar_container.patches[i].set_height(numbers[i])
        yield numbers

def radix_sort_visualization(numbers, bar_container):
    max_num = max(numbers)
    exp = 1
    while max_num // exp > 0:
        yield from counting_sort(numbers, exp, bar_container)
        exp *= 10

def main():
    count = int(input("Enter the number of bars to sort (e.g., 50): "))
    upper_limit = min(int(input("Enter the maximum value for the numbers (up to 20 million): ")), 20_000_000)
    numbers = generate_numbers(count, upper_limit)
    fig, ax = plt.subplots()
    ax.set_title("Progressive Sorting Visualization (Radix Sort)")
    bar_container = ax.bar(range(len(numbers)), numbers, align="edge", width=1.0)

    def on_complete():
        print("finished")

    anim = animation.FuncAnimation(
        fig,
        func=lambda frame: None,
        frames=radix_sort_visualization(numbers, bar_container),
        repeat=False,
        blit=False,
        interval=1  # Adjust this for smoother or faster animations
    )

    def check_animation_complete():
        if not anim.event_source.running:
            on_complete()

    anim._stop = check_animation_complete
    plt.show()

if __name__ == "__main__":
    main()