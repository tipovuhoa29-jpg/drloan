import os
import re

html_files = [f for f in os.listdir('E:/DrLoan/DoctorLoan_MVP') if f.endswith('.html')]

issues = []

for file in html_files:
    with open(f'E:/DrLoan/DoctorLoan_MVP/{file}', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all buttons
    buttons = re.findall(r'<button[^>]*>.*?</button>', content, flags=re.DOTALL)
    for b in buttons:
        lower_b = b.lower()
        if 'xem t' in lower_b or 'tất cả' in lower_b or 'chi tiết' in lower_b or 'thêm giỏ' in lower_b or 'đặt hàng' in lower_b:
            if 'onclick' not in lower_b and 'type="submit"' not in lower_b:
                # Is it wrapped in <a>? We can't easily check wrap with regex, but if it has no onclick it's suspicious.
                issues.append(f"{file}: Suspicious button without onclick: {b[:50]}...")
                
    # Find all <a> tags
    links = re.findall(r'<a\s+[^>]*>', content)
    for l in links:
        if 'href="#"' in l or 'href=""' in l or 'href' not in l:
            if 'class' in l and ('phương thức' not in l.lower()):
                issues.append(f"{file}: Dead link: {l}")

for issue in set(issues):
    print(issue)
