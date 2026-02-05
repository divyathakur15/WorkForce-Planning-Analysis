"""Quick fix for indentation issues"""
with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
for i, line in enumerate(lines, 1):
    # Line 647 and similar - reduce extra indentation
    if line.startswith('        with '):  # 8 spaces
        fixed_lines.append(line[4:])  # Remove 4 spaces
        print(f"Fixed line {i}: reduced indentation")
    elif line.startswith('        col') and '= st.columns' in line:  # 8 spaces
        fixed_lines.append(line[4:])  # Remove 4 spaces
        print(f"Fixed line {i}: reduced indentation")
    else:
        fixed_lines.append(line)

with open('streamlit_app.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("\n✅ Fixed indentation issues!")
