import re

file_path = 'E:/DrLoan/DoctorLoan_MVP/patent-manager.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's fix the structure completely by manually doing string surgery

# 1. Strip out the flawed structural tags we added:
text = text.replace('<div id="screen-list" class="screen space-y-6">\n\n\n    </div>', '')
text = text.replace('    </div>\n\n    <div id="screen-ai" class="screen hidden">\n<!-- AI Tham Vấn Chiến Lược Patent -->', '<!-- AI Tham Vấn Chiến Lược Patent -->')

# Now it looks like:
# <!-- Tabs Navigation --> ... 
# <!-- AI Tham Vấn Chiến Lược Patent --> ...
# <!-- Patent List --> ...
# </div>\n</main>

# 2. Extract the AI block
ai_pattern = r'(<!-- AI Tham Vấn Chiến Lược Patent -->.*?)\n    <!-- Patent List -->'
match_ai = re.search(ai_pattern, text, flags=re.DOTALL)
if match_ai:
    ai_html = match_ai.group(1)
    text = text.replace(ai_html + '\n', '')
else:
    print("Could not find AI block")

# 3. Extract the Patent List block
list_pattern = r'(<!-- Patent List -->.*?</section>)'
match_list = re.search(list_pattern, text, flags=re.DOTALL)
if match_list:
    list_html = match_list.group(1)
    text = text.replace(list_html, '')
else:
    print("Could not find Patent List block")

# Now text ends with:
# <!-- Tabs Navigation --> ... </div>\n\n    </div>\n</main>
# We need to insert the reconstructed blocks exactly where the Tabs Navigation ends
reconstructed = f'''    <div id="screen-list" class="screen space-y-6">
{list_html}
    </div>

    <div id="screen-ai" class="screen hidden">
{ai_html}
    </div>'''

# Find the end of tabs navigation
tabs_pattern = r'(<!-- Tabs Navigation -->.*?    </div>\n)'
match_tabs = re.search(tabs_pattern, text, flags=re.DOTALL)
if match_tabs:
    tabs_html = match_tabs.group(1)
    text = text.replace(tabs_html, tabs_html + '\n' + reconstructed + '\n')
    
    # Clean up any trailing broken divs before </main>
    text = re.sub(r'\s*</div>\n</main>', '\n</main>', text)
else:
    print("Could not find Tabs block")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("DOM structure repaired")
