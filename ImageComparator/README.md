
# Image Comparator


ImageComparator is a Python project that serves as a wrapper for DHash, allowing users to compare images based on their perceptual similarity. This tool can identify similar images in a specified folder, copy them to a target folder, and rename them with a suffix or prefix indicating their Hamming distance. 
The purpose (simply explained) is to find an image needle inside of a directory haystack.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Grrr1337/Python-Projects.git
   ```
    ```bash
    cd ImageComparator
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

• Utilize DHash to compare the source image with all images in the specified folder based on perceptual similarity.

• Print the sorted results of image paths and their Hamming distances.

• Copy similar images to a target folder.

• Optionally, rename the copied images with a suffix or prefix indicating their Hamming distance.

## Example usages:


```bash
# Return only up to 3 results (AND boolean):
python main.py --top_results 3 --target_folder images_found_1

# Return only up to 5 results:
python main.py --top_results 5 --target_folder images_found_2

# Return all results from 'images_to_find':
python main.py --top_results None --target_folder images_found_3
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize it further as needed for your project.
