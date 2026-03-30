import os

# Fix analytics.html
analytics_file = 'E:/DrLoan/DoctorLoan_MVP/analytics.html'
with open(analytics_file, 'r', encoding='utf-8') as f:
    analytics_content = f.read()

bad_chart = '''            <div class="flex items-end gap-3 h-32">
                <div class="flex-1 flex flex-col items-center gap-1">
                    <div class="w-full bg-primary/20 rounded-t-lg hover:bg-primary/50 transition-colors cursor-pointer" style="height:55%"></div>
                    <span class="text-[9px] text-tertiary">T1–7</span>
                </div>
                <div class="flex-1 flex flex-col items-center gap-1">
                    <div class="w-full bg-primary/40 rounded-t-lg hover:bg-primary/60 transition-colors cursor-pointer" style="height:70%"></div>
                    <span class="text-[9px] text-tertiary">T8–14</span>
                </div>
                <div class="flex-1 flex flex-col items-center gap-1">
                    <div class="w-full bg-primary/70 rounded-t-lg hover:bg-primary/90 transition-colors cursor-pointer" style="height:85%"></div>
                    <span class="text-[9px] text-tertiary">T15–21</span>
                </div>
                <div class="flex-1 flex flex-col items-center gap-1 relative">
                    <span class="absolute -top-5 text-[9px] font-black text-primary">1.4B</span>
                    <div class="w-full bg-primary rounded-t-lg" style="height:100%"></div>
                    <span class="text-[9px] text-primary font-bold">T22–31</span>
                </div>
            </div>'''

good_chart = '''            <div class="flex items-end gap-3 h-40">
                <div class="flex-1 flex flex-col justify-end items-center gap-2 h-full">
                    <div class="w-full bg-primary/20 rounded-t-lg hover:bg-primary/50 transition-colors cursor-pointer relative group" style="height:55%">
                        <span class="absolute -top-6 left-1/2 -translate-x-1/2 text-[9px] font-bold text-tertiary opacity-0 group-hover:opacity-100 transition-opacity">780tr</span>
                    </div>
                    <span class="text-[10px] font-medium text-tertiary">T1–7</span>
                </div>
                <div class="flex-1 flex flex-col justify-end items-center gap-2 h-full">
                    <div class="w-full bg-primary/40 rounded-t-lg hover:bg-primary/50 transition-colors cursor-pointer relative group" style="height:70%">
                        <span class="absolute -top-6 left-1/2 -translate-x-1/2 text-[9px] font-bold text-tertiary opacity-0 group-hover:opacity-100 transition-opacity">980tr</span>
                    </div>
                    <span class="text-[10px] font-medium text-tertiary">T8–14</span>
                </div>
                <div class="flex-1 flex flex-col justify-end items-center gap-2 h-full">
                    <div class="w-full bg-primary/70 rounded-t-lg hover:bg-primary/80 transition-colors cursor-pointer relative group" style="height:85%">
                        <span class="absolute -top-6 left-1/2 -translate-x-1/2 text-[9px] font-bold text-tertiary opacity-0 group-hover:opacity-100 transition-opacity">1.1B</span>
                    </div>
                    <span class="text-[10px] font-medium text-tertiary">T15–21</span>
                </div>
                <div class="flex-1 flex flex-col justify-end items-center gap-2 h-full">
                    <div class="w-full bg-primary rounded-t-lg hover:opacity-90 transition-opacity cursor-pointer relative" style="height:100%">
                        <span class="absolute -top-6 left-1/2 -translate-x-1/2 text-[10px] font-black text-primary">1.4B</span>
                    </div>
                    <span class="text-[10px] font-black text-primary">T22–31</span>
                </div>
            </div>'''

if bad_chart in analytics_content:
    analytics_content = analytics_content.replace(bad_chart, good_chart)
    with open(analytics_file, 'w', encoding='utf-8') as f:
        f.write(analytics_content)
    print("Fixed analytics.html")
else:
    print("Could not find bad chart in analytics.html")

# Fix ai-xray.html
xray_file = 'E:/DrLoan/DoctorLoan_MVP/ai-xray.html'
with open(xray_file, 'r', encoding='utf-8') as f:
    xray_content = f.read()

# Add animation to style
css_addon = '''
        @keyframes scan {
            0% { top: 0; opacity: 1; }
            50% { opacity: 0.8; }
            100% { top: 100%; opacity: 0.2; }
        }
        .scan-anim { animation: scan 2s linear infinite; }
</style>'''
xray_content = xray_content.replace('</style>', css_addon)

# Update the sample cases HTML
old_cases = '''                <!-- Sample cases -->
                <div>
                    <p class="text-sm font-bold text-on-surface-variant mb-3">Chọn mẫu có sẵn để Test</p>
                    <div class="space-y-2">
                        <div onclick="showResult('L5S1')" class="flex items-center gap-3 p-3 bg-surface-container-low rounded-xl cursor-pointer hover:bg-primary/5 hover:border-primary/20 border border-transparent transition-all">
                            <div class="w-12 h-12 bg-on-surface/80 rounded-lg flex items-center justify-center flex-shrink-0">
                                <span class="material-symbols-outlined text-white text-lg">radiology</span>
                            </div>
                            <div>
                                <p class="text-sm font-bold">BN: Đồng Văn Thanh</p>
                                <p class="text-[10px] text-tertiary">Mã: 015452 • X-Quang Cột Sống</p>
                            </div>
                        </div>
                        <div onclick="showResult('cervical')" class="flex items-center gap-3 p-3 bg-surface-container-low rounded-xl cursor-pointer hover:bg-primary/5 border border-transparent hover:border-primary/20 transition-all">
                            <div class="w-12 h-12 bg-on-surface/70 rounded-lg flex items-center justify-center flex-shrink-0">
                                <span class="material-symbols-outlined text-white text-lg">radiology</span>
                            </div>
                            <div>
                                <p class="text-sm font-bold">BN: Lê N. Đài Trang (1)</p>
                                <p class="text-[10px] text-tertiary">Mã: 21191 • X-Quang Nghiêng</p>
                            </div>
                        </div>
                        <div onclick="showResult('cervical2')" class="flex items-center gap-3 p-3 bg-surface-container-low rounded-xl cursor-pointer hover:bg-primary/5 border border-transparent hover:border-primary/20 transition-all">
                            <div class="w-12 h-12 bg-on-surface/60 rounded-lg flex items-center justify-center flex-shrink-0">
                                <span class="material-symbols-outlined text-white text-lg">radiology</span>
                            </div>
                            <div>
                                <p class="text-sm font-bold">BN: Lê N. Đài Trang (2)</p>
                                <p class="text-[10px] text-tertiary">Mã: 21191 • X-Quang Cổ</p>
                            </div>
                        </div>
                    </div>
                </div>'''

new_cases = '''                <!-- Sample cases -->
                <div>
                    <p class="text-sm font-bold text-on-surface-variant mb-3">Chọn mẫu có sẵn để Test</p>
                    <div class="space-y-3">
                        <div onclick="showResult('L5S1')" class="flex items-center gap-3 p-3 bg-surface-container-low rounded-xl cursor-pointer hover:bg-primary/5 hover:border-primary/20 hover:shadow-md border border-transparent transition-all group">
                            <div class="w-12 h-12 overflow-hidden rounded-lg flex-shrink-0 shadow-sm border border-outline-variant/20">
                                <img src="https://doctorloan.vn/img/x-quang/dong-van-thanh_015452/dong-van-thanh_1.png" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" alt="thumbnail">
                            </div>
                            <div>
                                <p class="text-sm font-bold text-on-surface">BN: Đồng Văn Thanh</p>
                                <p class="text-[10px] font-semibold text-tertiary">Mã: 015452 • X-Quang Lưng Thẳng</p>
                            </div>
                        </div>
                        <div onclick="showResult('cervical')" class="flex items-center gap-3 p-3 bg-surface-container-low rounded-xl cursor-pointer hover:bg-primary/5 border border-transparent hover:border-primary/20 hover:shadow-md transition-all group">
                            <div class="w-12 h-12 overflow-hidden rounded-lg flex-shrink-0 shadow-sm border border-outline-variant/20">
                                <img src="https://doctorloan.vn/img/x-quang/le-ngoc-dai-trang_21191/le-ngoc-dai-trang_3.png" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" alt="thumbnail">
                            </div>
                            <div>
                                <p class="text-sm font-bold text-on-surface">BN: Lê N. Đài Trang</p>
                                <p class="text-[10px] font-semibold text-tertiary">Mã: 21191 • X-Quang Cổ Nghiêng</p>
                            </div>
                        </div>
                        <div onclick="showResult('dao')" class="flex items-center gap-3 p-3 bg-surface-container-low rounded-xl cursor-pointer hover:bg-primary/5 border border-transparent hover:border-primary/20 hover:shadow-md transition-all group">
                            <div class="w-12 h-12 overflow-hidden rounded-lg flex-shrink-0 shadow-sm border border-outline-variant/20">
                                <img src="https://doctorloan.vn/img/x-quang/le-thi-dao_18824/le-thi-dao_1.png" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" alt="thumbnail">
                            </div>
                            <div>
                                <p class="text-sm font-bold text-on-surface">BN: Lê Thị Đào</p>
                                <p class="text-[10px] font-semibold text-tertiary">Mã: 18824 • X-Quang Lưng Nghiêng</p>
                            </div>
                        </div>
                    </div>
                </div>'''

xray_content = xray_content.replace(old_cases, new_cases)

# Add image preview area wrapper
old_upload = '''<!-- Upload zone -->
                <div class="lg:col-span-2">
                    <div onclick="simulateAnalysis()" class="upload-zone border-primary/30 rounded-2xl flex flex-col items-center justify-center py-24 gap-4 cursor-pointer hover:border-primary hover:bg-primary/5">'''

new_upload = '''<!-- Upload zone -->
                <div class="lg:col-span-2 relative">
                    <div id="image-preview-container" class="hidden absolute inset-0 bg-black rounded-2xl overflow-hidden shadow-inner border border-outline-variant/20">
                        <img id="xray-img" src="" class="w-full h-full object-contain opacity-90 mix-blend-screen" alt="X-Ray Analysis">
                        <div id="scan-line" class="absolute left-0 w-full h-[3px] bg-primary shadow-[0_0_20px_4px_rgba(255,117,0,0.8)] hidden z-10"></div>
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent pointer-events-none"></div>
                    </div>
                    
                    <div id="upload-zone" onclick="simulateAnalysis()" class="upload-zone border-primary/30 rounded-2xl flex flex-col items-center justify-center py-24 gap-4 cursor-pointer hover:border-primary hover:bg-primary/5 h-full min-h-[400px]">'''

xray_content = xray_content.replace(old_upload, new_upload)

# Update Javascript
old_js = '''    function showResult(type) {
        const diagnoses = {
            'L5S1': 'Trượt đốt sống L5-S1 độ II',
            'cervical': 'Thoái hóa đốt sống cổ C5-C6',
            'cervical2': 'Thoái hóa đốt sống cổ C4-C5-C6'
        };
        document.getElementById('diagnosis-text').textContent = diagnoses[type];
        simulateAnalysis();
    }'''

new_js = '''    function showResult(type) {
        const patientImages = {
            'L5S1': 'https://doctorloan.vn/img/x-quang/dong-van-thanh_015452/dong-van-thanh_1.png',
            'cervical': 'https://doctorloan.vn/img/x-quang/le-ngoc-dai-trang_21191/le-ngoc-dai-trang_3.png',
            'dao': 'https://doctorloan.vn/img/x-quang/le-thi-dao_18824/le-thi-dao_1.png'
        };
        const diagnoses = {
            'L5S1': 'Trượt đốt sống L5-S1 độ II',
            'cervical': 'Thoái hóa đốt sống cổ C5-C6',
            'dao': 'Thoái hóa cột sống L3-L5'
        };
        
        // Setup UI
        document.getElementById('upload-zone').classList.add('opacity-0');
        setTimeout(() => document.getElementById('upload-zone').classList.add('hidden'), 300);
        
        const preview = document.getElementById('image-preview-container');
        preview.classList.remove('hidden');
        document.getElementById('xray-img').src = patientImages[type];
        
        // Scan effect
        const scanLine = document.getElementById('scan-line');
        scanLine.classList.remove('hidden');
        scanLine.classList.add('scan-anim');
        
        document.getElementById('diagnosis-text').textContent = diagnoses[type];
        
        // Show result panel after "analysis"
        const resultEl = document.getElementById('ai-result');
        resultEl.classList.add('hidden');
        setTimeout(() => {
            scanLine.classList.remove('scan-anim');
            scanLine.classList.add('hidden');
            resultEl.classList.remove('hidden');
            resultEl.scrollIntoView({ behavior: 'smooth', block: 'end' });
            
            // Draw some AI bounding boxes dynamically
            const existingBoxes = preview.querySelectorAll('.ai-box');
            existingBoxes.forEach(b => b.remove());
            
            const box = document.createElement('div');
            box.className = 'ai-box absolute border-2 border-red-500 bg-red-500/10 rounded-lg animate-pulse';
            box.style.left = '40%'; box.style.top = '50%'; box.style.width = '20%'; box.style.height = '15%';
            preview.appendChild(box);
            
            // Add secondary indicator
            const crosshair = document.createElement('div');
            crosshair.className = 'ai-box absolute w-4 h-4 rounded-full border-2 border-primary bg-primary/20 animate-ping';
            crosshair.style.left = '50%'; crosshair.style.top = '57%';
            preview.appendChild(crosshair);
            
        }, 2000);
    }'''

xray_content = xray_content.replace(old_js, new_js)

with open(xray_file, 'w', encoding='utf-8') as f:
    f.write(xray_content)
print("Fixed ai-xray.html")

