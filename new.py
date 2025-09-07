import nbformat
import os

# Loop from day11 to day21
for i in range(11, 22):   # 22 because range is exclusive
    nb_file = f"day{i}.ipynb"
    fixed_file = f"fixed_day{i}.ipynb"
    
    if not os.path.exists(nb_file):
        print(f"❌ {nb_file} does not exist, skipping.")
        continue
    
    try:
        with open(nb_file, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        nbformat.validate(nb)
        
        with open(fixed_file, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        
        print(f"✅ {nb_file} repaired → {fixed_file}")
    
    except nbformat.reader.NotJSONError:
        print(f"❌ {nb_file} is not valid JSON. Check for corruption.")
    except Exception as e:
        print(f"❌ {nb_file} error: {e}")
