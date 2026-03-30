import os

# 1. Update app.js
appjs_path = 'E:/DrLoan/DoctorLoan_MVP/js/app.js'
with open(appjs_path, 'r', encoding='utf-8') as f:
    appjs_content = f.read()

target_appjs = '''        if (!document.body.hasAttribute('data-hide-bottom-nav')) {
             mainContent.classList.add('pb-24', 'lg:pb-10');
        }
    }
}'''

new_appjs = '''        if (!document.body.hasAttribute('data-hide-bottom-nav')) {
             mainContent.classList.add('pb-24', 'lg:pb-10');
        }
    }

    // Inject Share Modal globally
    const shareModalHTML = 
    <div id="global-share-modal" class="fixed inset-0 z-[100] hidden">
        <div class="absolute inset-0 bg-black/40 backdrop-blur-sm" onclick="closeShareModal()"></div>
        <div class="absolute bottom-0 left-0 right-0 md:top-1/2 md:left-1/2 md:right-auto md:w-[400px] md:-translate-x-1/2 md:-translate-y-1/2 bg-white rounded-t-[32px] md:rounded-[32px] p-6 shadow-2xl animate-[slideUp_0.3s_ease-out] border border-outline-variant/20">
            <div class="w-12 h-1.5 bg-outline-variant/30 rounded-full mx-auto mb-6 md:hidden"></div>
            <div class="flex justify-between items-center mb-5">
                <h3 class="font-black text-lg text-on-surface flex items-center gap-2"><span class="material-symbols-outlined text-primary">campaign</span>Chia sẻ Affiliate</h3>
                <button onclick="closeShareModal()" class="w-8 h-8 bg-surface-container rounded-full flex items-center justify-center text-on-surface-variant hover:bg-surface-container-high transition-colors">
                    <span class="material-symbols-outlined text-sm">close</span>
                </button>
            </div>
            
            <div class="bg-surface-container-low border border-primary/20 rounded-2xl p-4 mb-5 shadow-inner">
                <p class="text-[10px] font-black text-tertiary mb-2 uppercase tracking-widest leading-relaxed">Link bán hàng trực tiếp của bạn<br><span class="text-primary font-medium normal-case tracking-normal">Gửi bạn bè, chia sẻ group để nhận ngay hoa hồng</span></p>
                <div class="flex gap-2 relative">
                    <input id="share-link-input" type="text" readonly class="flex-1 bg-white border border-outline-variant/30 rounded-xl px-3 py-2 text-xs text-on-surface font-medium focus:outline-none focus:border-primary shadow-sm" onclick="this.select()">
                    <button id="copy-share-btn" onclick="copyShareLink()" class="px-3 md:px-4 py-2 brand-gradient text-white font-bold text-sm rounded-xl shadow-[0_4px_12px_rgba(255,117,0,0.3)] hover:opacity-90 active:scale-95 transition-all flex items-center gap-1">
                        <span class="material-symbols-outlined text-[16px]">content_copy</span>Copy
                    </button>
                </div>
            </div>

            <div class="grid grid-cols-4 gap-3 text-center mb-2">
                <div>
                    <button class="w-12 h-12 bg-[#0068FF] rounded-2xl text-white flex items-center justify-center mx-auto shadow-sm hover:-translate-y-1 hover:shadow-md transition-all active:scale-95">
                        <span class="material-symbols-outlined text-xl">chat</span>
                    </button>
                    <p class="text-[10px] font-bold mt-2 text-on-surface-variant">Zalo</p>
                </div>
                <div>
                    <button class="w-12 h-12 bg-[#1877F2] rounded-2xl text-white flex items-center justify-center mx-auto shadow-sm hover:-translate-y-1 hover:shadow-md transition-all active:scale-95">
                        <span class="material-symbols-outlined text-xl">thumb_up</span>
                    </button>
                    <p class="text-[10px] font-bold mt-2 text-on-surface-variant">Facebook</p>
                </div>
                <div>
                    <button class="w-12 h-12 bg-surface-container rounded-2xl text-on-surface flex items-center justify-center mx-auto shadow-sm hover:-translate-y-1 hover:shadow-md transition-all active:scale-95">
                        <span class="material-symbols-outlined text-xl">qr_code_2</span>
                    </button>
                    <p class="text-[10px] font-bold mt-2 text-on-surface-variant">Mã QR</p>
                </div>
                <div>
                    <button class="w-12 h-12 bg-surface-container rounded-2xl text-on-surface flex items-center justify-center mx-auto shadow-sm hover:-translate-y-1 hover:shadow-md transition-all active:scale-95">
                        <span class="material-symbols-outlined text-xl">more_horiz</span>
                    </button>
                    <p class="text-[10px] font-bold mt-2 text-on-surface-variant">Khác</p>
                </div>
            </div>
        </div>
    </div>
    ;
    if (!document.getElementById('global-share-modal')) {
        document.body.insertAdjacentHTML('beforeend', shareModalHTML);
    }
}

window.openShareModal = function(productId) {
    const modal = document.getElementById('global-share-modal');
    const input = document.getElementById('share-link-input');
    // Demo affiliate generation
    const mockRefId = 'dl_015452_thanh'; 
    input.value = https://doctorloan.vn/p/?ref=;
    
    // Reset copy button
    const btn = document.getElementById('copy-share-btn');
    btn.innerHTML = '<span class="material-symbols-outlined text-[16px]">content_copy</span>Copy';
    btn.classList.remove('bg-green-600', 'shadow-[0_4px_12px_rgba(22,163,74,0.3)]');
    btn.classList.add('brand-gradient', 'shadow-[0_4px_12px_rgba(255,117,0,0.3)]');
    
    modal.classList.remove('hidden');
};

window.closeShareModal = function() {
    document.getElementById('global-share-modal').classList.add('hidden');
};

window.copyShareLink = function() {
    const input = document.getElementById('share-link-input');
    input.select();
    document.execCommand('copy');
    
    const btn = document.getElementById('copy-share-btn');
    btn.innerHTML = '<span class="material-symbols-outlined text-[16px]">check</span>Đã copy';
    btn.classList.remove('brand-gradient', 'shadow-[0_4px_12px_rgba(255,117,0,0.3)]');
    btn.classList.add('bg-green-600', 'shadow-[0_4px_12px_rgba(22,163,74,0.3)]');
};'''

if target_appjs in appjs_content and 'openShareModal' not in appjs_content:
    appjs_content = appjs_content.replace(target_appjs, new_appjs)
    with open(appjs_path, 'w', encoding='utf-8') as f:
        f.write(appjs_content)
    print("Updated app.js")

# 2. Update product-detail.html
pd_path = 'E:/DrLoan/DoctorLoan_MVP/product-detail.html'
with open(pd_path, 'r', encoding='utf-8') as f:
    pd_content = f.read()

pd_top_bar_old = '''        <div class="flex gap-2">
            <button class="w-10 h-10 flex items-center justify-center text-primary hover:opacity-80 transition-opacity active:scale-95 duration-200">
                <span class="material-symbols-outlined">share</span>
            </button>'''

pd_top_bar_new = '''        <div class="flex gap-2">
            <button onclick="openShareModal('ghe-135-pro')" class="w-10 h-10 flex items-center justify-center text-primary hover:opacity-80 transition-opacity active:scale-95 duration-200">
                <span class="material-symbols-outlined">share</span>
            </button>'''

if pd_top_bar_old in pd_content:
    pd_content = pd_content.replace(pd_top_bar_old, pd_top_bar_new)

pd_link_btn_old = '''                <button class="w-full flex items-center justify-center gap-2 py-3 bg-white/60 hover:bg-white rounded-2xl border border-primary-container/20 text-primary font-semibold text-sm active:scale-95 transition-all cursor-pointer">
                    <span class="material-symbols-outlined text-[20px]">link</span>
                    Link bán của tôi
                    <span class="material-symbols-outlined text-[18px] text-tertiary">content_copy</span>
                </button>'''

pd_link_btn_new = '''                <button onclick="openShareModal('ghe-135-pro')" class="w-full flex items-center justify-center gap-2 py-3 bg-white/60 hover:bg-white rounded-2xl border border-primary-container/20 text-primary font-semibold text-sm shadow-[0_4px_12px_rgba(255,117,0,0.1)] active:scale-95 transition-all cursor-pointer group">
                    <span class="material-symbols-outlined text-[20px]">link</span>
                    Link bán của tôi (Hoa hồng 10%)
                    <span class="material-symbols-outlined text-[18px] text-primary/60 group-hover:text-primary transition-colors">share</span>
                </button>'''

if pd_link_btn_old in pd_content:
    pd_content = pd_content.replace(pd_link_btn_old, pd_link_btn_new)

with open(pd_path, 'w', encoding='utf-8') as f:
    f.write(pd_content)
print("Updated product-detail.html")

# 3. Update products.html
p_path = 'E:/DrLoan/DoctorLoan_MVP/products.html'
with open(p_path, 'r', encoding='utf-8') as f:
    p_content = f.read()

# Add share icons inside the image tags for products
# We will do regex replace to add the share button right after <div class="absolute top-2 left-2 flex flex-col gap-1">...</div>
import re
pattern = r'(<div class="absolute top-2 left-2 flex flex-col gap-1">.*?</div>\n\s*)(</a>)'

replacement = r'''\1
                        <button onclick="event.preventDefault(); openShareModal('item-id')" class="absolute top-2 right-2 w-8 h-8 rounded-xl bg-white/90 backdrop-blur border border-outline-variant/20 shadow-sm flex items-center justify-center text-on-surface-variant hover:text-primary hover:border-primary/50 active:scale-95 transition-all z-10">
                            <span class="material-symbols-outlined text-[18px]">share</span>
                        </button>
                    \2'''

p_content = re.sub(pattern, replacement, p_content, flags=re.DOTALL)
with open(p_path, 'w', encoding='utf-8') as f:
    f.write(p_content)

print("Updated products.html")

