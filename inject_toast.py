import os
import re

app_file = 'E:/DrLoan/DoctorLoan_MVP/js/app.js'
with open(app_file, 'r', encoding='utf-8') as f:
    app_content = f.read()

toast_html = '''
window.showToast = function(message) {
    let toast = document.getElementById('global-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'global-toast';
        toast.className = 'fixed bottom-24 left-1/2 -translate-x-1/2 z-[200] bg-surface-container-high text-on-surface text-sm font-bold px-6 py-3 rounded-full shadow-2xl border border-outline-variant/30 flex items-center gap-2 transition-all duration-300 transform translate-y-10 opacity-0 pointer-events-none';
        document.body.appendChild(toast);
    }
    toast.innerHTML = <span class="material-symbols-outlined text-primary text-[18px]">info</span> ;
    
    // Animate in
    toast.style.display = 'flex';
    setTimeout(() => {
        toast.classList.remove('translate-y-10', 'opacity-0');
        toast.classList.add('translate-y-0', 'opacity-100');
    }, 10);
    
    // Animate out
    setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-10', 'opacity-0');
        setTimeout(() => toast.style.display = 'none', 300);
    }, 2500);
};
'''

if 'window.showToast' not in app_content:
    with open(app_file, 'a', encoding='utf-8') as f:
        f.write('\n' + toast_html)
    print("Added showToast to app.js")

# Now replace generic buttons across all files
html_files = [f for f in os.listdir('E:/DrLoan/DoctorLoan_MVP') if f.endswith('.html')]

changes_made = 0

for file in html_files:
    filepath = f'E:/DrLoan/DoctorLoan_MVP/{file}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
        
    # Pattern to find buttons without onclick
    # This is tricky with regex, we'll find <button ...> where ... doesn't have onclick
    
    def replacer(match):
        attrs = match.group(1)
        tag_content = match.group(2)
        lower_content = tag_content.lower()
        
        # Don't touch if already has onclick or form submit
        if 'onclick=' in attrs.lower() or 'type="submit"' in attrs.lower():
            return match.group(0)
            
        # Add to cart -> redirect to cart
        if 'thêm giỏ' in lower_content or 'thêm vào giỏ' in lower_content:
            return f'<button {attrs} onclick="showToast(\\\'Đã thêm vào giỏ hàng thành công!\\\')">{tag_content}</button>'
            
        if 'thanh toán' in lower_content:
            return f'<button {attrs} onclick="window.location.href=\\\'cart.html\\\'">{tag_content}</button>'
            
        if 'chi tiết' in lower_content or 'xem thêm' in lower_content or 'xem tất cả' in lower_content:
            # Maybe just a toast
            return f'<button {attrs} onclick="showToast(\\\'Tính năng xem chi tiết đang được hoàn thiện!\\\')">{tag_content}</button>'
            
        if 'xử lý ngay' in lower_content or 'gia hạn' in lower_content or 'lên kế hoạch' in lower_content:
            return f'<button {attrs} onclick="showToast(\\\'Đã gửi yêu cầu đến Luật sư Sở hữu trí tuệ!\\\')">{tag_content}</button>'
            
        if 'đánh dấu đã đọc' in lower_content:
            return f'<button {attrs} onclick="showToast(\\\'Đã đánh dấu tất cả thông báo!\\\')">{tag_content}</button>'
            
        return match.group(0)

    # regex to match <button [attrs]>[content]</button>
    content = re.sub(r'<button([^>]*)>(.*?)</button>', replacer, content, flags=re.DOTALL)
    
    # Also replace Dead Links <a href="#">
    content = content.replace('href="#"', 'href="javascript:void(0)" onclick="showToast(\\\'Tính năng nội dung đang cập nhật!\\\')"')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        changes_made += 1

print(f"Attached actions to buttons in {changes_made} files")

