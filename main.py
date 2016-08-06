from PIL import Image, ImageFont, ImageDraw
import textwrap, time

def draw_text_and_border(border_colour, paragraph, expansion):
    width_text, height_text = draw.textsize(paragraph[0], font)
    current_width = (screen_width - width_text)/2
    current_height = (screen_height - height_text)/2 - (screen_height/4)
    # Making a black border around the text so that it is readable on any background, Thanks to Alec Bennet for the base code to do this https://mail.python.org/pipermail/image-sig/2009-May/005681.html
    for text_quotes in paragraph:
        width_text, height_text = draw.textsize(text_quotes, font)
        current_width = (screen_width - width_text)/2
        if current_width < 20:
            expansion += 5
            paragraph = textwrap.wrap(content[quote_location], int(screen_width / expansion))
            draw_text_and_border("black",paragraph,expansion)
            break

        else:
            draw.text((current_width-1, current_height), text_quotes, font=font, fill=border_colour)
            draw.text((current_width+1, current_height), text_quotes, font=font, fill=border_colour)
            draw.text((current_width, current_height-1), text_quotes, font=font, fill=border_colour)
            draw.text((current_width, current_height+1), text_quotes, font=font, fill=border_colour)
            draw.text((current_width-1, current_height-1), text_quotes, font=font, fill=border_colour)
            draw.text((current_width+1, current_height-1), text_quotes, font=font, fill=border_colour)
            draw.text((current_width-1, current_height+1), text_quotes, font=font, fill=border_colour)
            draw.text((current_width+1, current_height+1), text_quotes, font=font, fill=border_colour)
            draw.text((current_width, current_height), text_quotes, font=font)
            current_height += fontsize + dist_between_lines

# Opening the file with the quotes, this code is designed to work with a mass export of quotes from Moon Reader Plus for Android
# That being said, any text file with quotes will work if formatted correctly.
with open("Quotes.txt") as f:
    content = f.readlines()
f.close()

#Generating Each Background
for i in range(int(((len(content) - 3)/2))):
    # Handles the formatting of the text file that Moon Reader exports, the quotes start at line 6 then skip a line.
    quote_location = 6 + (2*i)
    # Opens the images stored in the "Wallpapers" folder. The imaages are simply named 1.jpg, 2.jpg, etc...
    im = Image.open("Wallpapers/{}.jpg".format(i+1))
    # Setting the width and height to the actual size of the image, allowing any size image to be used.
    screen_width, screen_height = im.size
    # Changes a large line of text into a list with the text broken 70 characters in.
    paragraph = textwrap.wrap(content[quote_location], int(screen_width / 35))
    # Takes the first line of the paragraph and makes it into a list.
    first = list(paragraph[0])
    # Deletes the second character until a letter comes up, that way the quote doesn't start with a space or comma.
    while first[1].isalpha() == False:
        first[1].pop()
    # Makes the first letter in the sentence upper case.
    first[1] = first[1].upper()
    # Turns the list back into a string.
    first = "".join(first)
    # Returns it to the paragraph, now grammatically correct.
    paragraph[0] = first
    # Makes the fontsize proportional to the screen height, this way even smaller images can be used.
    fontsize = int(screen_height /20)
    # Sets the font to arial, feel free to change this to something else.
    font = ImageFont.truetype("arial.ttf", fontsize)
    # Draws the image.
    draw = ImageDraw.Draw(im)
    # Sets the width and height of the text to be proportional to the size of the text at the line
    width_text, height_text = draw.textsize(content[quote_location], font)
    dist_between_lines =  10
    # Uses the function defined earlier to draw the text to the screen and add a black border to add readability.
    draw_text_and_border("black",paragraph, 35)
    # Displays the image
    im.save("Complete/{}.jpg".format(i))
