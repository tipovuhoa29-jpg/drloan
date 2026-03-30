document.addEventListener('DOMContentLoaded', () => {
    initLayout();
    highlightActiveMenu();
});

const APP_NAME = "DOCTORLOAN";

function initLayout() {
    // Determine the current page for active states
    const path = window.location.pathname;
    const page = path.split('/').pop() || 'index.html';

    // Top App Bar
    const header = `
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
    `;
    // Bottom Navigation (Mobile)
    const bottomNav = `
    <nav class="bottom-nav fixed bottom-0 w-full rounded-t-[24px] z-50 bg-white shadow-[0px_-4px_16px_rgba(0,0,0,0.06)] flex justify-around items-center h-20 px-2 pb-safe md:hidden">
        <a class="nav-item flex flex-col items-center justify-center gap-1 w-1/5 text-[#8c7163]" href="index.html" data-page="index.html">
            <span class="material-symbols-outlined text-2xl">home</span>
            <span class="text-[11px] font-medium font-['Inter'] mt-1">Trang chủ</span>
        </a>
        <a class="nav-item flex flex-col items-center justify-center gap-1 w-1/5 text-[#8c7163]" href="products.html" data-page="products.html">
            <span class="material-symbols-outlined text-2xl">local_mall</span>
            <span class="text-[11px] font-medium font-['Inter'] mt-1">Sản phẩm</span>
        </a>
        <a class="nav-item flex flex-col items-center justify-center gap-1 w-1/5 text-[#8c7163]" href="cart.html" data-page="cart.html">
            <span class="material-symbols-outlined text-2xl">shopping_cart</span>
            <span class="text-[11px] font-medium font-['Inter'] mt-1">Đơn hàng</span>
        </a>
        <a class="nav-item flex flex-col items-center justify-center gap-1 w-1/5 text-[#8c7163]" href="chat-ai.html" data-page="chat-ai.html">
            <span class="material-symbols-outlined text-2xl">smart_toy</span>
            <span class="text-[11px] font-medium font-['Inter'] mt-1">Chat AI</span>
        </a>
        <a class="nav-item flex flex-col items-center justify-center gap-1 w-1/5 text-[#8c7163]" href="profile.html" data-page="profile.html">
            <span class="material-symbols-outlined text-2xl">person</span>
            <span class="text-[11px] font-medium font-['Inter'] mt-1">Tôi</span>
        </a>
    </nav>
    `;

    // Sidebar Navigation (Desktop)
    const sidebar = `
    <aside class="sidebar hidden md:flex flex-col fixed top-0 left-0 w-[250px] h-screen bg-surface-container-lowest border-r border-surface-variant z-[60] py-6 px-4 gap-2">
        <!-- Logo for Desktop inside Sidebar -->
        <div class="px-4 pb-8 pt-4">
            <img src="https://doctorloan.vn/img/logo/logo-header.svg" alt="DoctorLoan" class="h-9 w-auto object-contain">
        </div>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="index.html" data-page="index.html">
            <span class="material-symbols-outlined">home</span>
            <span class="font-semibold text-sm">Trang chủ</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="dashboard-ceo.html" data-page="dashboard-ceo.html">
            <span class="material-symbols-outlined">monitoring</span>
            <span class="font-semibold text-sm">CEO Dashboard</span>
        </a>
        <p class="px-4 pt-3 pb-1 text-[9px] font-black uppercase tracking-[0.15em] text-on-surface-variant/40">Kinh doanh</p>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="products.html" data-page="products.html">
            <span class="material-symbols-outlined">local_mall</span>
            <span class="font-semibold text-sm">Sản phẩm</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="orders.html" data-page="orders.html">
            <span class="material-symbols-outlined">receipt_long</span>
            <span class="font-semibold text-sm">Đơn hàng</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="customers.html" data-page="customers.html">
            <span class="material-symbols-outlined">groups</span>
            <span class="font-semibold text-sm">Khách hàng</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="analytics.html" data-page="analytics.html">
            <span class="material-symbols-outlined">bar_chart</span>
            <span class="font-semibold text-sm">Báo cáo</span>
        </a>
        <p class="px-4 pt-3 pb-1 text-[9px] font-black uppercase tracking-[0.15em] text-on-surface-variant/40">Vận hành</p>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="warehouse.html" data-page="warehouse.html">
            <span class="material-symbols-outlined">inventory_2</span>
            <span class="font-semibold text-sm">Quản lý kho</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="patent-manager.html" data-page="patent-manager.html">
            <span class="material-symbols-outlined">gavel</span>
            <span class="font-semibold text-sm">Bằng sáng chế</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="ai-xray.html" data-page="ai-xray.html">
            <span class="material-symbols-outlined">radiology</span>
            <span class="font-semibold text-sm">Trợ lý AI X-Quang</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="rd-workflow.html" data-page="rd-workflow.html">
            <span class="material-symbols-outlined">biotech</span>
            <span class="font-semibold text-sm">AI R&amp;D Workflow</span>
        </a>

        <p class="px-4 pt-3 pb-1 text-[9px] font-black uppercase tracking-[0.15em] text-on-surface-variant/40">Học tập</p>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="learning.html" data-page="learning.html">
            <span class="material-symbols-outlined">school</span>
            <span class="font-semibold text-sm">Học tập</span>
        </a>
        <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="chat-ai.html" data-page="chat-ai.html">
            <span class="material-symbols-outlined">smart_toy</span>
            <span class="font-semibold text-sm">Chat AI tư vấn</span>
        </a>
        
        <div class="mt-auto border-t border-surface-variant pt-4">
             <a class="nav-item-desktop flex items-center gap-4 px-4 py-3 rounded-xl text-on-surface-variant hover:bg-surface-container hover:text-primary-container transition-colors" href="profile.html" data-page="profile.html">
                <span class="material-symbols-outlined">person</span>
                <span class="font-semibold text-sm">Tài khoản của tôi</span>
            </a>
        </div>
    </aside>
    `;

    // Inject into body if not hidden
    if (!document.querySelector('header') && !document.body.hasAttribute('data-hide-header')) {
        document.body.insertAdjacentHTML('afterbegin', header);
    }
    if (!document.querySelector('.bottom-nav') && !document.body.hasAttribute('data-hide-bottom-nav')) {
        document.body.insertAdjacentHTML('beforeend', bottomNav);
    }
    if (!document.querySelector('.sidebar')) {
        document.body.insertAdjacentHTML('afterbegin', sidebar);
    }
}

function highlightActiveMenu() {
    let path = window.location.pathname;
    let page = path.split('/').pop() || 'index.html';
    
    // For local dev, if it's empty, default to index.html
    if (page === '') page = 'index.html';

    // Highlight mobile bottom nav
    const mobileItems = document.querySelectorAll('.nav-item');
    mobileItems.forEach(item => {
        if (item.getAttribute('data-page') === page) {
            item.classList.remove('text-[#8c7163]');
            item.classList.add('text-[#ff7500]');
            // Add background to the icon container if needed based on the design
            const iconWrapper = item.querySelector('.material-symbols-outlined');
            if (iconWrapper) {
                // To match original design, wrap icon in a div
                const currentHtml = iconWrapper.outerHTML;
                item.innerHTML = `
                <div class="bg-[#ffdbcb] text-[#ff7500] rounded-2xl px-5 py-1 flex items-center justify-center">
                    ${currentHtml.replace('text-2xl', 'text-2xl').replace('class="material-symbols-outlined', 'style="font-variation-settings: \\\'FILL\\\' 1;" class="material-symbols-outlined')}
                </div>
                <span class="text-[11px] font-bold text-[#ff7500] font-['Inter'] mt-1">${item.querySelector('span:last-child').innerText}</span>
                `;
            }
        }
    });

    // Highlight desktop sidebar nav
    const desktopItems = document.querySelectorAll('.nav-item-desktop');
    desktopItems.forEach(item => {
        if (item.getAttribute('data-page') === page) {
             item.classList.remove('text-on-surface-variant');
             item.classList.add('bg-secondary-fixed', 'text-primary-container', 'font-black');
             const icon = item.querySelector('.material-symbols-outlined');
             if (icon) {
                 icon.style.fontVariationSettings = "'FILL' 1";
             }
        }
    });

    const mainContent = document.querySelector('main');
    if (mainContent) {
        if (!mainContent.hasAttribute('data-custom-layout')) {
            mainContent.classList.add('desktop-content-area');
        }
        mainContent.classList.add('transition-all', 'duration-300');
        if (!document.body.hasAttribute('data-hide-header')) {
             mainContent.classList.add('pt-20');
        }
        if (!document.body.hasAttribute('data-hide-bottom-nav')) {
             mainContent.classList.add('pb-24', 'lg:pb-10');
        }
    }

    // Inject Share Modal globally
    const shareModalHTML = `
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
    `;
    if (!document.getElementById('global-share-modal')) {
        document.body.insertAdjacentHTML('beforeend', shareModalHTML);
    }
}

window.openShareModal = function(productId) {
    const modal = document.getElementById('global-share-modal');
    const input = document.getElementById('share-link-input');
    // Demo affiliate generation
    const mockRefId = 'dl_015452_thanh'; 
    input.value = `https://doctorloan.vn/p/${productId}?ref=${mockRefId}`;
    
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
};


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


window.showToast = function(message) {
    let toast = document.getElementById('global-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'global-toast';
        toast.className = 'fixed bottom-24 left-1/2 -translate-x-1/2 z-[200] bg-surface-container-high text-on-surface text-sm font-bold px-6 py-3 rounded-full shadow-2xl border border-outline-variant/30 flex items-center gap-2 transition-all duration-300 transform translate-y-10 opacity-0 pointer-events-none';
    }
    toast.innerHTML = `<span class="material-symbols-outlined text-primary text-[18px]">info</span> ${message}`;
    
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
