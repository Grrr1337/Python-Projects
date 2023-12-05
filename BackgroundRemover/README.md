
# Background Remover


The Background Remover is a Python project that leverages the 'rembg' library. It enables users to eliminate backgrounds from multiple images within a specified folder. The processed images are then saved in an 'output' folder, resulting in images with removed backgrounds.
The sample input/output can be checked in the 'source_images' and 'out_images' folders.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Grrr1337/Python-Projects.git
   ```
    ```bash
    cd BackgroundRemover
    ```
2. Set up a virtual environment:
    ```bash
    python -m venv .venv
    ```

3. Activate the virtual environment:

    For Windows:

    ```bash
    .venv\Scripts\Activate
    ```

    For Linux/macOS:
    ```bash
    source .venv/bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script:

```bash
python main.py
```

This will perform the following tasks:

• Will create the specified target/output folder

• Will read every image from the source folder and will re-write it with a removed background to the output folder


## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize it further as needed for your project.
