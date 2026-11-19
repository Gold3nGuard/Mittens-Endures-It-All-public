import re


def extractPy(source_filepath: str, test_destination_folder: str):
    """Extracts Python code from .rpy files

    Args:
        source_filepath (str): Path to source file
        test_destination_folder (str): Path to folder that contains the Python 
            portion of each source file.
    """

    dst_path: str = test_destination_folder + '/' + source_filepath.split('/')[-1]
    dst_path = dst_path[:-4] + '.py'
    init_line_pat = r"init\s+(?:-?\d*\s+)?python\:"
    with open(source_filepath, 'r') as src, open(dst_path, 'w+') as dst:
        
        # Scan source for init
        init_found: bool = False
        indent_found: bool = False
        for line in src:

            # Find init
            init_search = re.search(init_line_pat, line)
            if (init_found == False) and (init_search is not None):
                init_found = True
                continue
            
            # Detect indent: defined as the first line that isn't all whitespace
            if init_found and (indent_found == False):
                indent_search = re.search(r"^\s*$", line)
                indent_found = indent_search is None
                if indent_found == False: continue
                line_code = re.search(r"^\s+", line)
                if line_code is None: continue
                indent = line_code.span()[1]

            # Extract all text that is indented with init
            if indent_found:
                if len(line) >= indent:
                    if (re.search(r"^\s$", line[0]) is None): 
                        break
                    line = line[indent:]
                    dst.write(line)
                elif re.search(r"^\s*$", line) is not None:
                    dst.write(line)

if __name__ == "__main__":
    extractPy('game/src/py/inventory/InventorySystem.rpy', 'tests/src')
    extractPy('game/src/py/inventory/InventoryItems.rpy', 'tests/src')
    # extractPy('game/src/py/Girlfriend.rpy', 'tests/src')
    # extractPy('game/src/py/utils/RandomNumberGenerator.rpy', 'tests/src')
    extractPy('game/src/py/Time.rpy', 'tests/src')
    extractPy('game/src/py/LocationFlags.rpy', 'tests/src')
