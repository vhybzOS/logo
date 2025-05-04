# petal.py
import drawsvg as draw

def draw_single_petal(base_width=50, height=100, **kwargs):
    """
    Draws a single abstract petal shape using a Path element.

    The petal is drawn vertically, with its 'base' at (0, 0)
    and its 'tip' extending along the positive y-axis.

    Args:
        base_width (float): The approximate maximum width of the petal.
        height (float): The approximate height from the base to the tip.
        **kwargs: Additional keyword arguments passed to drawsvg.Path
                  (e.g., fill, stroke, stroke_width).

    Returns:
        drawsvg.Path: A drawsvg Path element representing the petal shape.
    """
    path = draw.Path(**kwargs)

    # Define the petal shape using cubic Bézier curves
    # This is an initial approximation and will likely need tuning.
    # The path starts at the base (0,0), goes up the right side,
    # to the tip (0, height), down the left side, and back to the base.

    path.M(0, 0) # Start at the base

    # Right side curve (base to widest point)
    path.C(base_width * 0.3, height * 0.1,
           base_width * 0.5, height * 0.3,
           base_width * 0.5, height * 0.5) # Widest point (base_width/2, height/2)

    # Right side curve (widest point to tip)
    path.C(base_width * 0.5, height * 0.7,
           base_width * 0.3, height * 0.9,
           0, height) # Tip (0, height)

    # Left side curve (tip to widest point)
    path.C(-base_width * 0.3, height * 0.9,
           -base_width * 0.5, height * 0.7,
           -base_width * 0.5, height * 0.5) # Widest point (-base_width/2, height/2)

    # Left side curve (widest point to base)
    path.C(-base_width * 0.5, height * 0.3,
           -base_width * 0.3, height * 0.1,
           0, 0) # Back to base (0, 0)

    path.Z() # Close the path

    return path

if __name__ == '__main__':
    # Example usage of the petal function
    d = draw.Drawing(200, 200, origin='center')

    # Draw one petal
    petal_shape = draw_single_petal(fill='skyblue', stroke='black')
    d.append(petal_shape)

    # Save and display
    d.save_svg('single_petal_example.svg')
    print("Generated single_petal_example.svg")

    # Example with scaling and rotation
    d_transformed = draw.Drawing(200, 200, origin='center')
    petal_shape_small = draw_single_petal(fill='lightgreen')
    d_transformed.append(draw.Use(petal_shape_small, 0, 0, transform='scale(0.5) rotate(90)'))
    d_transformed.save_svg('transformed_petal_example.svg')
    print("Generated transformed_petal_example.svg")
    