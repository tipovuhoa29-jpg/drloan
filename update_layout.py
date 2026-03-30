import os
import glob

html_files = glob.glob('E:/DrLoan/DoctorLoan_MVP/*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # Update sidebar margin for tablet
    content = content.replace('lg:ml-[250px]', 'md:ml-[250px]')
    content = content.replace('lg:ml-64', 'md:ml-64')
    
    # Update top/bottom paddings for layout shifts
    content = content.replace('lg:pb-8', 'md:pb-8')
    content = content.replace('lg:pt-24', 'md:pt-24')
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Updated {count} HTML files with tablet margins.')
