# Texttoimage

Texttoimage is a Python library for converting text to a transparent image.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install texttoimage.

```bash
pip install texttoimage
```

## Usage

```python
import texttoimage

texttoimage.convert('Hello World') # generate an image named "helloworld.png"

# if you want to create a multiple line text image you can use `\n` in your text
text = 'Hello World\n This is a multiple line text'
# It'll generate an image which the font size is 48 and color is red.
texttoimage.convert(text, image_file='test.png', font_size=100, color='red')
```
## Examples

![](hello.png)
![](test.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)