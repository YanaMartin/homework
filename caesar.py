import argparse

parser = argparse.ArgumentParser(description='argparse changing text in one file into another')
parser.add_argument("input_file", default=None, help=("Input file to read"))
parser.add_argument("output_file", default=None, help=("output file with the changes"))
parser.add_argument('-s', '--shift', help='The shift value of the cypher', required=True, type=int)
parser.add_argument('--capital', action="store_true", help='changes all the letters to capitals')
args = parser.parse_args()


def caesar_cypher(text, shift):
    """Function that encrypting a text using a Caesar Cypher."""
    result = ''
    for character in text:
        if character.isalpha():
            number = ord(character)
            number += shift
            if character.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            elif character.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
            character = chr(number)
        result += character

    return result


def caesar(input_file, output_file, shift, capital=False):
    """reading the command line arguments"""
    with open(args.input_file, encoding='utf-8') as input_file:
        text = input_file.read()
        shift=args.shift
        capital=args.capital
        cyphertext = caesar_cypher(text, shift)
        with open(args.output_file, mode='w', encoding='utf-8') as output_file:
            if capital: 
                upper_case=cyphertext.upper()
                return output_file.write(upper_case)
            else:
                return output_file.write(cyphertext)
            

            
caesar(args.input_file, args.output_file, args.shift, args.capital)
