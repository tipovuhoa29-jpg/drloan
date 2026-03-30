import os

filepath = 'E:/DrLoan/DoctorLoan_MVP/js/app.js'
with open(filepath, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace header
header_start = js_content.find('const header = ')
header_end = js_content.find(';', header_start) + 2

new_header = '''const header = 
    <!-- Top App Bar -->
    <header class="fixed top-0 w-full md:w-[calc(100%-250px)] md:ml-[250px] z-[40] bg-white/95 dark:bg-slate-900/95 backdrop-blur-md flex justify-between items-center px-4 md:px-6 h-16 shadow-sm border-b border-outline-variant/10">
        <!-- Left: Hamburger (Mobile) -->
        <div class="flex items-center w-1/3 md:hidden">
            <button onclick="toggleMobileMenu()" class="w-10 h-10 -ml-2 text-on-surface-variant hover:bg-surface-container rounded-full flex items-center justify-center transition-colors">
                <span class="material-symbols-outlined text-[26px]">menu</span>
            </button>
        </div>
        
        <!-- Center: Logo (Mobile) -->
        <div class="flex flex-1 items-center justify-center md:hidden">
            <img src="https://doctorloan.vn/img/logo/logo-header.svg" alt="DoctorLoan" class="h-6 w-auto object-contain">
        </div>
        
        <!-- Right: Actions -->
        <div class="flex items-center justify-end gap-3 w-1/3 md:w-full">
            <a href="notifications.html" class="relative active:scale-95 transition-transform hover:opacity-80 cursor-pointer flex items-center justify-center w-9 h-9 md:w-10 md:h-10 rounded-full bg-surface-container-lowest border border-outline-variant/20 shadow-sm">
                <span class="material-symbols-outlined text-on-surface-variant text-[20px] md:text-[22px]">notifications</span>
                <span class="absolute top-1.5 right-2 w-2 h-2 bg-error rounded-full border border-white"></span>
            </a>
            <a href="profile.html" class="w-9 h-9 md:w-10 md:h-10 rounded-full overflow-hidden border border-primary/30 active:scale-95 transition-transform cursor-pointer shadow-sm">
                <img class="w-full h-full object-cover" src="https://ui-avatars.com/api/?name=Minh+Tuan&background=ff7500&color=fff" alt="Profile">
            </a>
        </div>
    </header>
    
    <!-- Mobile Navigation Drawer -->
    <div id="mobileDrawerOverlay" onclick="toggleMobileMenu()" class="fixed inset-0 bg-black/60 z-[60] hidden opacity-0 transition-opacity duration-300 backdrop-blur-sm"></div>
    <aside id="mobileDrawer" class="fixed top-0 left-0 w-[280px] h-full bg-surface-container-lowest z-[70] transform -translate-x-full transition-transform duration-300 flex flex-col shadow-2xl">
        <div class="flex-shrink-0 p-5 flex items-center justify-between border-b border-outline-variant/10">
            <img src="https://doctorloan.vn/img/logo/logo-header.svg" alt="DoctorLoan" class="h-7 w-auto object-contain">
            <button onclick="toggleMobileMenu()" class="w-8 h-8 flex items-center justify-center bg-surface-container-low hover:bg-surface-variant rounded-full text-on-surface-variant transition-colors">
                <span class="material-symbols-outlined text-[18px]">close</span>
            </button>
        </div>
        <div class="flex-1 overflow-y-auto px-4 py-4 space-y-1 disable-scrollbars pb-24">
            <a href="profile.html" class="flex items-center gap-3 p-3 mb-4 rounded-2xl bg-primary/5 border border-primary/10">
                <img class="w-10 h-10 rounded-full border border-primary/30 shadow-sm" src="https://ui-avatars.com/api/?name=Minh+Tuan&background=ff7500&color=fff" alt="Profile">
                <div>
                    <p class="font-bold text-sm text-on-surface">Minh Tuấn</p>
                    <p class="text-[10px] font-bold text-primary">Xem tài khoản</p>
                </div>
            </a>
        
            <p class="px-3 pt-2 pb-1 text-[10px] font-black uppercase tracking-[0.15em] text-primary">Kinh doanh</p>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="index.html"><span class="material-symbols-outlined">home</span> Trang chủ</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="dashboard-ceo.html"><span class="material-symbols-outlined">monitoring</span> CEO Dashboard</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="products.html"><span class="material-symbols-outlined">local_mall</span> Sản phẩm</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="orders.html"><span class="material-symbols-outlined">receipt_long</span> Đơn hàng</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="customers.html"><span class="material-symbols-outlined">groups</span> Khách hàng</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="analytics.html"><span class="material-symbols-outlined">bar_chart</span> Báo cáo</a>
            
            <p class="px-3 pt-4 pb-1 text-[10px] font-black uppercase tracking-[0.15em] text-on-surface-variant/50">Vận hành & Đào tạo</p>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="learning.html"><span class="material-symbols-outlined">school</span> Học tập</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="warehouse.html"><span class="material-symbols-outlined">inventory_2</span> Quản lý kho</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="patent-manager.html"><span class="material-symbols-outlined">gavel</span> Bằng sáng chế</a>
            
            <p class="px-3 pt-4 pb-1 text-[10px] font-black uppercase tracking-[0.15em] text-on-surface-variant/50">Trí tuệ nhân tạo (AI)</p>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="rd-workflow.html"><span class="material-symbols-outlined">science</span> AI R&D Workflow</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="ai-xray.html"><span class="material-symbols-outlined">body_system</span> Phân tích X-quang</a>
            <a class="flex items-center gap-4 px-3 py-3 rounded-xl text-on-surface-variant active:bg-primary/10 transition-colors font-medium" href="chat-ai.html"><span class="material-symbols-outlined">smart_toy</span> Trợ lý AI</a>
        </div>
    </aside>
    ;'''
js_content = js_content[:header_start] + new_header + js_content[header_end:]

# Replace sidebar lg: -> md:
js_content = js_content.replace('sidebar hidden lg:flex', 'sidebar hidden md:flex')
# Replace bottom-nav lg:hidden -> md:hidden
js_content = js_content.replace('pb-safe lg:hidden', 'pb-safe md:hidden')

# Add toggleMobileMenu function if not exists
if 'function toggleMobileMenu' not in js_content:
    js_content += '''\n
window.toggleMobileMenu = function() {
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('mobileDrawerOverlay');
    if (!drawer || !overlay) return;
    if (drawer.classList.contains('-translate-x-full')) {
        drawer.classList.remove('-translate-x-full');
        overlay.classList.remove('hidden');
        setTimeout(() => overlay.classList.remove('opacity-0'), 10);
    } else {
        drawer.classList.add('-translate-x-full');
        overlay.classList.add('opacity-0');
        setTimeout(() => overlay.classList.add('hidden'), 300);
    }
};
'''

# Now let's adjust the global layout margins in initLayout 
# The main content wrappers in many HTML files currently use lg:ml-[250px]. Let's update all html files
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updated app.js")
