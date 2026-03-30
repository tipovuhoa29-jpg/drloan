import re

file_path = 'E:/DrLoan/DoctorLoan_MVP/chat-ai.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add ID to chat messages container
text = text.replace(
    '<div class="flex flex-col gap-6 max-w-3xl mx-auto h-full justify-end min-h-[max-content] pb-6">',
    '<div id="chat-messages" class="flex flex-col gap-6 max-w-3xl mx-auto h-full justify-end min-h-[max-content] pb-6">'
)

# 2. Add IDs to Input and Send button
text = re.sub(
    r'<input class="w-full bg-transparent border-none focus:ring-0 text-sm md:text-base py-2.5 placeholder:text-on-surface-variant/60 outline-none"(.*?)>',
    r'<input id="chat-input" class="w-full bg-transparent border-none focus:ring-0 text-sm md:text-base py-2.5 placeholder:text-on-surface-variant/60 outline-none"\1 onkeypress="if(event.key === \'Enter\') sendChatMessage()">',
    text
)

send_btn_pattern = r'<button (.*?)>\s*<span class="material-symbols-outlined ml-1" style="font-variation-settings: \'FILL\' 1;">send</span>\s*</button>'
text = re.sub(
    send_btn_pattern,
    r'<button onclick="sendChatMessage()" \1>\n                <span class="material-symbols-outlined ml-1" style="font-variation-settings: \'FILL\' 1;">send</span>\n            </button>',
    text,
    flags=re.DOTALL
)

# 3. Replace quick reply chips
chip_container = r'<div class="flex overflow-x-auto gap-2 px-4 py-3 hide-scrollbar flex-nowrap max-w-3xl mx-auto">(.*?)</div>'
match = re.search(chip_container, text, flags=re.DOTALL)
if match:
    chips_html = '''
            <button onclick="sendQuickReply(this.innerText)" class="whitespace-nowrap px-4 py-2 rounded-full border border-primary text-primary text-xs md:text-sm font-semibold bg-white hover:bg-primary-fixed hover:border-transparent transition-colors active:scale-95 cursor-pointer">Đau mỏi vai gáy</button>
            <button onclick="sendQuickReply(this.innerText)" class="whitespace-nowrap px-4 py-2 rounded-full border border-primary text-primary text-xs md:text-sm font-semibold bg-white hover:bg-primary-fixed hover:border-transparent transition-colors active:scale-95 cursor-pointer">Chọn gối phù hợp</button>
            <button onclick="sendQuickReply(this.innerText)" class="whitespace-nowrap px-4 py-2 rounded-full border border-primary text-primary text-xs md:text-sm font-semibold bg-white hover:bg-primary-fixed hover:border-transparent transition-colors active:scale-95 cursor-pointer">Hỏi giá đệm</button>
            <button onclick="sendQuickReply(this.innerText)" class="whitespace-nowrap px-4 py-2 rounded-full border border-primary text-primary text-xs md:text-sm font-semibold bg-white hover:bg-primary-fixed hover:border-transparent transition-colors active:scale-95 cursor-pointer">Tư vấn kinh doanh</button>
'''
    text = text.replace(match.group(0), f'<div class="flex overflow-x-auto gap-2 px-4 py-3 hide-scrollbar flex-nowrap max-w-3xl mx-auto">{chips_html}        </div>')


# 4. Inject JavaScript Simulation Script
script_html = '''
<script>
    const responses = {
        'đau mỏi vai gáy': 'Tình trạng đau mỏi vai gáy thường do thoái hóa đốt sống cổ hoặc căng cơ do sai tư thế. Gối F4/09 của DoctorLoan được thiết kế để nắn chỉnh lại đường cong sinh lý quanh cổ. Bạn có muốn xem thêm chi tiết không?',
        'chọn gối phù hợp': 'Với dân văn phòng/người hay lái xe, bộ đôi Gối Cổ F4/09 và Đệm ngồi DoctorLoan là kết hợp tối ưu nhất để cân bằng cột sống. Bạn muốn tôi hướng dẫn cách mua hàng luôn chứ?',
        'hỏi giá đệm': 'Đệm thiền DoctorLoan hiện đang có giá 1.200.000đ. Đệm giúp định hình xương chậu, hỗ trợ ngồi lâu không bị thoái hóa đốt sống lưng.',
        'tư vấn kinh doanh': 'Với tư cách Đại lý, bạn sẽ nhận được chiết khấu từ 10% đến 25% tùy theo gói sản phẩm phân phối. Tôi có thể hỗ trợ bạn tư vấn quy trình tạo mã QR Affiliate nhé!',
        'default': 'Cảm ơn bạn đã quan tâm. Tính năng siêu trí tuệ AI Tư Vấn Bệnh Lý Chuyên Sâu hiện đang được đào tạo với hơn 1 triệu mẫu dữ liệu y khoa từ bác sĩ DoctorLoan và sẽ hoàn thiện ở phiên bản tới!'
    };

    function appendUserMessage(msg) {
        const chat = document.getElementById('chat-messages');
        const userHtml = 
            <div class="flex items-end justify-end gap-2 ml-auto max-w-[90%] md:max-w-[75%] animate-[slideUp_0.3s_ease-out]">
                <div class="brand-gradient text-white p-4 rounded-2xl user-bubble shadow-[0px_8px_16px_rgba(156,69,0,0.2)]">
                    <p class="text-sm md:text-base leading-relaxed"></p>
                </div>
            </div>;
        chat.insertAdjacentHTML('beforeend', userHtml);
        scrollToBottom();
    }

    function appendBotTyping() {
        const chat = document.getElementById('chat-messages');
        const typingId = 'typing-' + Date.now();
        const typingHtml = 
            <div id="" class="flex items-end gap-2 max-w-[90%] md:max-w-[75%] animate-[slideUp_0.3s_ease-out]">
                <div class="bg-surface-container-highest text-on-surface py-4 px-5 rounded-2xl bot-bubble shadow-sm flex items-center gap-1.5">
                    <div class="w-1.5 h-1.5 bg-primary/60 rounded-full animate-bounce" style="animation-delay: 0s"></div>
                    <div class="w-1.5 h-1.5 bg-primary/60 rounded-full animate-bounce" style="animation-delay: 0.15s"></div>
                    <div class="w-1.5 h-1.5 bg-primary/60 rounded-full animate-bounce" style="animation-delay: 0.3s"></div>
                </div>
            </div>;
        chat.insertAdjacentHTML('beforeend', typingHtml);
        scrollToBottom();
        return typingId;
    }

    function appendBotMessage(msg, typingId) {
        const chat = document.getElementById('chat-messages');
        const botHtml = 
            <div class="flex items-end gap-2 max-w-[90%] md:max-w-[75%] animate-[slideUp_0.3s_ease-out]">
                <div class="bg-surface-container-highest text-on-surface p-4 rounded-2xl bot-bubble shadow-sm">
                    <p class="text-sm md:text-base leading-relaxed"></p>
                </div>
            </div>;
        
        const typingEl = document.getElementById(typingId);
        if (typingEl) typingEl.remove();
        
        chat.insertAdjacentHTML('beforeend', botHtml);
        scrollToBottom();
    }

    function scrollToBottom() {
        const mainEl = document.querySelector('main');
        if (mainEl) {
            setTimeout(() => {
                mainEl.scrollTo({
                    top: mainEl.scrollHeight,
                    behavior: 'smooth'
                });
            }, 50);
        }
    }

    function sendQuickReply(text) {
        processMessage(text);
    }

    window.sendChatMessage = function() {
        const input = document.getElementById('chat-input');
        if (!input) return;
        const text = input.value.trim();
        if (!text) return;
        
        input.value = '';
        processMessage(text);
    };

    function processMessage(text) {
        appendUserMessage(text);
        
        const typingId = appendBotTyping();
        
        let reply = responses['default'];
        const lowerText = text.toLowerCase();
        
        for (const [key, value] of Object.entries(responses)) {
            if (key !== 'default' && lowerText.includes(key)) {
                reply = value;
                break;
            }
        }
        
        setTimeout(() => {
            appendBotMessage(reply, typingId);
        }, 1200 + Math.random() * 800);
    }
</script>
</body>
'''
text = text.replace('</body>', script_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected ChatGPT simulation logic smoothly")
