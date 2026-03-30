import re

file_pm = 'E:/DrLoan/DoctorLoan_MVP/patent-manager.html'
with open(file_pm, 'r', encoding='utf-8') as f:
    content = f.read()

# Add tabs right after Stats Alert Search blocks
# The Search block ends with </div> just before <!-- AI Tham Vấn Chiến Lược Patent -->
tab_html = '''
    <!-- Tabs Navigation -->
    <div class="flex border-b border-outline-variant/30 mb-6 sticky top-[60px] md:top-0 bg-surface z-40 pt-2">
        <button id="tab-list" onclick="switchTab('list')" class="px-5 py-3 text-sm font-bold border-b-2 border-primary text-primary transition-colors hover:bg-surface-container">Danh sách bằng cấp (62)</button>
        <button id="tab-ai" onclick="switchTab('ai')" class="px-5 py-3 text-sm font-medium text-on-surface-variant border-b-2 border-transparent hover:text-primary hover:bg-surface-container transition-colors relative">
            AI Tư vấn Chiến lược
            <span class="absolute top-2 right-2 flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-primary"></span>
            </span>
        </button>
    </div>

    <div id="screen-list" class="screen space-y-6">
'''

# We need to inject tab_html right after the <!-- Search --> div block.
# Let's find <!-- Search --> and its end.
search_block = re.search(r'(<!-- Search -->.*?</select>\n    </div>)', content, flags=re.DOTALL)
if search_block:
    sb = search_block.group(0)
    content = content.replace(sb, sb + '\n' + tab_html)

# Now wrap the AI block
ai_start = '<!-- AI Tham Vấn Mới Nhất -->' # Wait, what was the exact comment? Let me check previous block text
# Earlier my script used '<!-- AI Tham Vấn Chiến Lược Patent -->'
content = content.replace('<!-- AI Tham Vấn Chiến Lược Patent -->', '    </div>\n\n    <div id="screen-ai" class="screen hidden">\n<!-- AI Tham Vấn Chiến Lược Patent -->')

# And close the AI block before </main>
content = content.replace('</main>', '    </div>\n</main>')

# Now add switchTab logic at bottom
script_html = '''
<script>
    function switchTab(tabId) {
        document.querySelectorAll('.screen').forEach(el => el.classList.add('hidden'));
        document.getElementById('screen-' + tabId).classList.remove('hidden');
        
        const tabList = document.getElementById('tab-list');
        const tabAi = document.getElementById('tab-ai');
        
        tabList.className = "px-5 py-3 text-sm font-medium text-on-surface-variant border-b-2 border-transparent hover:text-primary hover:bg-surface-container transition-colors";
        tabAi.className = "px-5 py-3 text-sm font-medium text-on-surface-variant border-b-2 border-transparent hover:text-primary hover:bg-surface-container transition-colors relative";
        
        if (tabId === 'list') {
            tabList.className = "px-5 py-3 text-sm font-bold border-b-2 border-primary text-primary transition-colors hover:bg-surface-container";
        } else {
            tabAi.className = "px-5 py-3 text-sm font-bold border-b-2 border-primary text-primary transition-colors hover:bg-surface-container relative";
        }
    }
</script>
'''
content = content.replace('</body>', script_html + '\n</body>')

with open(file_pm, 'w', encoding='utf-8') as f:
    f.write(content)
print("Wrapped patent manager with tabs")
