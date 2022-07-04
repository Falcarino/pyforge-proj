import unittest
from urllib.request import urlopen
from pathlib import Path
from api_requests import get_compound_properties
  
class TestUserInput(unittest.TestCase):

    '''
    Keep in mind that the user input always gets capitalized
    in the
        @cli.command("get_compound")
            def get_compound():
    function inside manage.py
    '''

    def test_proper_input(self):
        function_result = get_compound_properties("ADP")

        # I actually HAVE TO pass the control value like this,
        # else it'll keep using escape characters
        self.assertEqual(function_result, {'name': "ADENOSINE-5'-DIPHOSPHATE", 'released': True, 'superseded_by': None, 'formula': 'C10 H15 N5 O10 P2', 'inchi': 'InChI=1S/C10H15N5O10P2/c11-8-5-9(13-2-12-8)15(3-14-5)10-7(17)6(16)4(24-10)1-23-27(21,22)25-26(18,19)20/h2-4,6-7,10,16-17H,1H2,(H,21,22)(H2,11,12,13)(H2,18,19,20)/t4-,6-,7-,10-/m1/s1', 'inchi_key': 'XTWYTFMLZFPYCI-KQYNXXCUSA-N', 'smiles': 'c1nc(c2c(n1)n(cn2)C3C(C(C(O3)COP(=O)(O)OP(=O)(O)O)O)O)N', 'ww_pdb_info': {'defined_at': '1999-07-08 00:00:00', 'modified': '2011-06-04 00:00:00', 'modification_flag': 'Y', 'polymer_type': 'NON-POLYMER', 'standard_parent': 'A'}, 'functional_annotations': [], 'cross_links': [{'resource': 'BindingDb', 'resource_id': '31995'}, {'resource': 'BRENDA', 'resource_id': '13'}, {'resource': 'BRENDA', 'resource_id': '13638'}, {'resource': 'Guide to Pharmacology', 'resource_id': '1712'}, {'resource': 'MetaboLights', 'resource_id': 'MTBLC16761'}, {'resource': 'BRENDA', 'resource_id': '215293'}, {'resource': 'BRENDA', 'resource_id': '2539'}, {'resource': 'ChEMBL', 'resource_id': 'CHEMBL14830'}, {'resource': 'KEGG LIGAND', 'resource_id': 'C00008'}, {'resource': 'BRENDA', 'resource_id': '58917'}, {'resource': 'BRENDA', 'resource_id': '7140'}, {'resource': 'BRENDA', 'resource_id': '23600'}, {'resource': 'BRENDA', 'resource_id': '91791'}, {'resource': 'ZINC', 'resource_id': 'ZINC000012360703'}, {'resource': 'PubChem', 'resource_id': '6022'}, {'resource': 'BRENDA', 'resource_id': '92424'}, {'resource': 'ChEBI', 'resource_id': '16761'}], 'synonyms': [], 'phys_chem_properties': {'crippen_mr': 81.535, 'num_atom_stereo_centers': 5, 'crippen_clog_p': -2.555, 'num_rings': 3, 'num_rotatable_bonds': 12, 'num_heteroatoms': 17, 'fraction_csp3': 0.5, 'num_aromatic_rings': 2, 'exactmw': 427.029, 'num_spiro_atoms': 0, 'num_heavy_atoms': 27, 'num_aliphatic_rings': 1, 'num_hbd': 6, 'num_saturated_heterocycles': 1, 'tpsa': 232.6, 'num_bridgehead_atoms': 0, 'num_aromatic_heterocycles': 2, 'labute_asa': 171.385, 'num_hba': 15, 'num_amide_bonds': 0, 'num_saturated_rings': 1, 'lipinski_hba': 15.0, 'num_unspec_atom_stereo_centers': 0, 'lipinski_hbd': 7.0, 'num_heterocycles': 3, 'num_aliphatic_heterocycles': 1}})
    
    def test_empty_string_input(self):
        self.assertRaises(ValueError, get_compound_properties, "")

    def test_illegal_compound_input(self):
        self.assertRaises(ValueError, get_compound_properties, "123532")

    def test_legal_compound_with_lowercase_input(self):
        # This case is pretty much guaranteed to never happen
        self.assertRaises(ValueError, get_compound_properties, "ADp")

if __name__ == '__main__': 
    unittest.main()