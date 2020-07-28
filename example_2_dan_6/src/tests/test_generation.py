
import unittest
from code_generation.generator import CodeGen

from functions.function_spec import functions

class TestCodeGen(unittest.TestCase):    

    def setUp(self):
        """
        Setting up test
        """
        self.code_gen = CodeGen("Pera Petrovic")

    def test_generate (self):
        """
        Testing code generation
        """    
        generated = self.code_gen.generate("main.c", functions)
        generated = self.code_gen.generate1("func.c", functions)
        generated = self.code_gen.generate2("func.h", functions)
        self.assertEqual(generated, True)      
