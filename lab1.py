import numpy as np
import matplotlib.pyplot as plt

# Choose number of chords to draw in the simulation:
num_chords = 10000


def draw_circle_and_triangle(ax):
    """Draw the circle and equilateral triangle inscribed in the circle."""
    circle = plt.Circle((0, 0), 1, color='w', linewidth=2, fill=False)
    ax.add_patch(circle)  # Draw the circle
    # Plot triangle sides
    ax.plot([np.cos(np.pi / 2), np.cos(7 * np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(np.pi / 2), np.cos(- np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(- np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(- np.pi / 6), np.cos(7 * np.pi / 6)],
            [np.sin(- np.pi / 6), np.sin(7 * np.pi / 6)], linewidth=2, color='g')


def chord_length(x1, y1, x2, y2):
    """Calculate the length of a chord given its endpoints."""
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def bertrand2():

    r = np.random.uniform(0, 1)
    theta = np.random.uniform(0, 2 * np.pi)

    x0 = r * np.cos(theta)
    y0 = r * np.sin(theta)

    d = np.sqrt(1 - r ** 2)  # Half-length of the chord (Pythagoras)

    # Endpoints of the chord
    x1 = x0 + d * np.sin(theta)
    y1 = y0 - d * np.cos(theta)
    x2 = x0 - d * np.sin(theta)
    y2 = y0 + d * np.cos(theta)

    return x1, y1, x2, y2


def bertrand_simulation(method_number=2):
    """Run the simulation for Bertrand's paradox using 'Method 2'."""
    triangle_side = np.sqrt(3)  # Length of each side of the inscribed equilateral triangle
    count = 0

    # Figure initialization
    plt.style.use('dark_background')  # Use dark background
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1, 1))  # Set x-axis limits
    ax.set_ylim((-1, 1))  # Set y-axis limits

    # Run the simulation for the specified number of chords
    for i in range(num_chords):
        # Step 1: Generate chord using Method 2
        x1, y1, x2, y2 = bertrand2()

        # Step 2: Compute the length of the chord and compare it with triangle side
        length = chord_length(x1, y1, x2, y2)
        if length > triangle_side:
            count += 1  # Increment count if chord is longer than the triangle side

        # Plot the first 1000 chords
        if i < 1000:
            color = 'r' if length > triangle_side else 'b'
            ax.plot([x1, x2], [y1, y2], color=color, alpha=0.1)

    # Draw the circle and the triangle on the plot
    draw_circle_and_triangle(ax)
    plt.show()

    # Display the probability
    probability = count / num_chords
    print(f"Probability of chord being longer than triangle side: {probability:.3f}")


# Run the simulation using only Method 2
bertrand_simulation()
