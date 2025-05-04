# vhybZ OS Logo

This project aims to create our "propeller" logo image using the `drawsvg` Python library.

## Project Structure

*   `main.py`: The main script to generate the SVG drawing. It sets up the canvas, arranges the different parts of the logo, applies styles (colors, opacity, filters), and saves the output.
*   `petal.py`: Contains functions for drawing the individual "petal" or "blade" shapes that make up the logo's structure.
*   `README.md`: This file, explaining the project.
*   `robot.md`: Provides detailed context and instructions for an AI assistant to continue working on the project.

## Approach (v0.1)

The logo is visually composed of four overlapping, translucent, colored petal shapes arranged in an 'X'. This initial version implements this interpretation:

1.  **Petal Shape:** A single, abstract petal shape is defined in `petal.py` using a `drawsvg.Path` element with cubic Bézier curves. It's drawn with its base at the origin (0,0) and tip along the positive y-axis for easy rotation.
2.  **Composition:** In `main.py`, the `draw_single_petal` function is used to create the base shape. This shape is then included in a `drawsvg.Group` which applies a global scale to make the petal a reasonable size. This scaled shape definition is then referenced four times using `drawsvg.Use`.
3.  **Arrangement:** Each `drawsvg.Use` element is rotated around the center of the drawing to form the 'X' shape.
4.  **Color and Blending:** Each petal `Use` element is given a distinct fill color and a `fill_opacity` less than 1.0 to create the overlapping color blending effect seen in the original image.
5.  **Shadow:** A basic SVG drop shadow filter is defined in `main.py` using `drawsvg.Filter` and `feGaussianBlur`/`feOffset`/`feMerge`. This filter is applied to the bottom two petals to simulate the shadow.
6.  **Background:** A simple colored rectangle is added as the background.

## Getting Started

1.  Install `drawsvg` (and optional rasterization dependencies if needed):
    ```bash
    python3 -m pip install "drawsvg[all]~=2.0"
    ```
    You might also need to install Cairo separately depending on your OS (see drawsvg documentation for details).
2.  Save the code above into `petal.py` and `main.py` in a `drawsvg_logo` directory.
3.  Run `main.py` from your terminal:
    ```bash
    cd drawsvg_logo
    python main.py
    ```
    This will generate `logo_v0_1.svg` in the same directory.

## Next Steps

*   **Refine Petal Shape:** The Bézier control points in `petal.py` need tuning to precisely match the curves of the original image's petals.
*   **Refine Colors/Gradients:** The current implementation uses solid colors with opacity for simplicity. The original image shows subtle gradients within each petal. These should be added.
*   **Refine Shadow:** Adjust the filter parameters (blur amount, offset) and potentially opacity/color of the shadow effect to better match the original.
*   **Implement Texture:** Investigate methods to add the subtle grainy texture, possibly using SVG filters (`feTurbulence`) or other techniques.

This initial version provides the structural foundation for recreating the logo.
