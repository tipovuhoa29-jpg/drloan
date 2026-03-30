import os
import re

xray_file = 'E:/DrLoan/DoctorLoan_MVP/ai-xray.html'
pm_file = 'E:/DrLoan/DoctorLoan_MVP/patent-manager.html'

with open(xray_file, 'r', encoding='utf-8') as f:
    xray_content = f.read()

# 1. Remove the tab button
btn_pattern = r'\s*<button id="tab-patent".*?>.*?Chiến Lược Patent\n\s*</button>'
xray_content = re.sub(btn_pattern, '', xray_content, flags=re.DOTALL)

# 2. Extract and remove the screen
screen_pattern = r'(<!-- ===== SCREEN: CHIẾN LƯỢC PATENT ===== -->.*?</div>\n    </div>)'
match = re.search(screen_pattern, xray_content, flags=re.DOTALL)

patent_html = ""
if match:
    patent_html = match.group(1)
    xray_content = xray_content.replace(patent_html, '')
    print("Found and removed patent screen from ai-xray.html")
else:
    print("Could not find patent screen in ai-xray.html!")

with open(xray_file, 'w', encoding='utf-8') as f:
    f.write(xray_content)

# 3. Adapt and insert into patent-manager.html
if patent_html:
    # Adapt HTML for patent-manager
    patent_html = patent_html.replace(' id="screen-patent"', '')
    patent_html = patent_html.replace(' class="screen space-y-5"', ' class="space-y-5"')
    patent_html = patent_html.replace('<!-- ===== SCREEN: CHIẾN LƯỢC PATENT ===== -->', '<!-- AI Tham Vấn Chiến Lược Patent -->')
    patent_html = patent_html.replace('''<button onclick="switchTab('consult')" class="text-xs font-bold text-primary hover:underline px-2">Xem lại phác đồ</button>''', 
        '''<button class="text-xs font-bold text-primary hover:underline px-2 flex items-center gap-1"><span class="material-symbols-outlined text-xs">search</span>Tra cứu khác</button>''')
    patent_html = patent_html.replace('bệnh nhân/đối tác này nằm trong vùng bảo hộ thương mại an toàn', 'khu vực này nằm trong vùng bảo hộ thương mại an toàn')
    patent_html = patent_html.replace('đính kèm hồ sơ điều trị', 'khi xúc tiến thương mại')
    
    with open(pm_file, 'r', encoding='utf-8') as f:
        pm_content = f.read()
        
    insertion_point = '    <!-- Patent List -->'
    if insertion_point in pm_content:
        new_pm_content = pm_content.replace(insertion_point, patent_html + '\n\n' + insertion_point)
        with open(pm_file, 'w', encoding='utf-8') as f:
            f.write(new_pm_content)
        print("Injected into patent-manager.html")
    else:
        print("Insertion point not found in patent-manager.html!")

