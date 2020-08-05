
import unittest
import os
import pickle
#Both xml modules need to be run before code generation
from xml import xml_parser
from xml import xml_sort

from generator import CodeGen
from functions.function_spec import functions
from functions.function_spec import user_defined


class TestCodeGen(unittest.TestCase):    

    def setUp(self):
        """
        Setting up test
        """
        self.code_gen = CodeGen("Igor Ilic")

    def test_generate (self):
        """
        Testing code generation
        """    
        generated = self.code_gen.generate("main.c", functions)
        generated = self.code_gen.generate1("block_functions.c", functions)
        generated = self.code_gen.generate2("block_functions.h", functions)
        generated = self.code_gen.generate_user_defined("user_defined.c", user_defined)
        generated = self.code_gen.generate_user_defined_h("user_defined.h", user_defined)
        self.assertEqual(generated, True)
    
    #test if number of source edges for all nodes is <= than 1
    def test_edges(self):
        for item in xml_parser.elem:
            assert len(item[4]) <= 1
    
    #test if all nodes have at least one source or target
    def test_connection(self):
        for item in xml_parser.elem:
            assert  ( len(item[4]) >= 1 ) or ( len(item[5]) >= 1 )
    
    #test if there is only one input block
    def test_one_input(self):
        iter = 0
        for item in xml_parser.elem:
            if item[1] == "ulaz":
                iter = iter + 1
        assert iter == 1
        
    #test if there is at least one output
    def test_at_least_one_output(self):
        iter = 0
        for item in xml_parser.elem:
            if "izlaz" in item[3]:
                iter = iter + 1
        print(iter)
        assert iter >= 1
        
    #test if there is a loop:
    def test_loop(self):
        for item in xml_parser.elem:
            for node in item[5]:
                if len(item[4]) > 0:
                    assert not (item[4][0] == node)
                    
    #test execution order
    def test_execution(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\xml\\xml_pickle_sorted', 'rb') as f:
            graph_info = pickle.load(f)
        assert graph_info[0][0] == "n0"
        assert graph_info[2][0] == "n3"
        assert graph_info[7][0] == "n9"
        assert graph_info[11][0] == "n6"
        assert graph_info[4][0] == "user_defined1"
