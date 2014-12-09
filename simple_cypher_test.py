import unittest
from simpleCipher import *
import simpleCipher

class TestSimpleCipher(unittest.TestCase):
    
    def test_create_encode_dictionary(self):
        encode_dictionary = create_encode_dictionary('blueberry')
        self.assertEqual(encode_dictionary.get('a'), 'b')
        self.assertEqual(encode_dictionary.get('f'), 'y')
        self.assertEqual(encode_dictionary.get('g'), 's')
        self.assertEqual(encode_dictionary.get('l'), 'z')
        self.assertEqual(encode_dictionary.get('m'), 'a')
        self.assertEqual(encode_dictionary.get('z'), 'q')

    def test_create_decode_dictionary(self):
        decode_dictionary = create_decode_dictionary('blueberry')
        self.assertEqual(decode_dictionary.get('b'), 'a')
        self.assertEqual(decode_dictionary.get('y'), 'f')
        self.assertEqual(decode_dictionary.get('s'), 'g')
        self.assertEqual(decode_dictionary.get('z'), 'l')
        self.assertEqual(decode_dictionary.get('a'), 'm')
        self.assertEqual(decode_dictionary.get('q'), 'z')
       
    def test_encipher(self):
        self.assertEqual(encipher('blueberry', 'Hello world!'), 'Trzzd ndhze!')
        self.assertEqual(encipher('blueberry', 'Attack at dawn!'), 'Bjjbux bj ebnc!')

    def test_decipher(self):
        self.assertEqual(decipher('blueberry', 'Hello world!'), 'Rdbbx jxebo!')
        self.assertEqual(decipher('blueberry', 'Bjjbux bj ebnc!'), 'Attack at dawn!')                                  

    def test_get_cipher_list(self):
        cipher_list = get_cipher_list('blueberry')
        self.assertEqual(cipher_list[3], 'e')
        self.assertEqual(cipher_list[25], 'q')
        self.assertEqual(cipher_list[9], 'w')

unittest.main()
