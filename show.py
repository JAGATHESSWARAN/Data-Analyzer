import pickletools
import pprint

def peek_pickle(file_path):
    print(f"Attempting to peek into contents of {file_path}:")
    print("=" * 50)
    
    with open(file_path, 'rb') as f:
        pickled_data = f.read()
    
    structure = []
    for opcode, arg, pos in pickletools.genops(pickled_data):
        if opcode.name == 'GLOBAL':
            module, name = arg.split(' ')
            structure.append(f"Global: {module}.{name}")
        elif opcode.name in ('NEWTRUE', 'NEWFALSE'):
            structure.append(f"Boolean: {opcode.name == 'NEWTRUE'}")
        elif opcode.name == 'LONG':
            structure.append(f"Integer: {arg}")
        elif opcode.name == 'FLOAT':
            structure.append(f"Float: {arg}")
        elif opcode.name == 'SHORT_BINUNICODE':
            structure.append(f"String: {arg}")
        elif opcode.name == 'EMPTY_LIST':
            structure.append("Empty List")
        elif opcode.name == 'EMPTY_DICT':
            structure.append("Empty Dict")
        elif opcode.name == 'APPEND':
            structure.append("List Append")
        elif opcode.name == 'SETITEM':
            structure.append("Dict SetItem")
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(structure)

if __name__ == "__main__":
    file_path = 'best_model.pkl'  # Replace with your file path if different
    peek_pickle(file_path)