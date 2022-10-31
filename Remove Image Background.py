from rembg import remove
from PIL import Image

input_path = 'Abdul Rahman.jpg'
output_path = 'Abdul Rahman.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)