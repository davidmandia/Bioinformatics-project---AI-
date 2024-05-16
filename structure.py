from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import AllChem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw

# Convert SMILES to RDKit molecule object

def smile_to_image(smile):

    mol = Chem.MolFromSmiles(smile)

    # Generate 3D coordinates
    mol = Chem.AddHs(mol)  # Add hydrogens for a more accurate 3D structure
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())  # Generate 3D coordinates using ETKDG method

    # Visualize in 3D (optional)
    from rdkit.Chem import Draw
    Draw.MolToImage(mol)
    # Generate 3D coordinates
    rdDepictor.Compute2DCoords(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())

    # Visualize in 3D
    return mol
