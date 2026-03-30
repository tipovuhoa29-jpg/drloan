import os

file_dash = 'E:/DrLoan/DoctorLoan_MVP/dashboard-ceo.html'
with open(file_dash, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Parent container: h-48 to give enough headroom
content = content.replace(
    '<div class="flex items-end justify-between gap-1 sm:gap-2 h-44 mt-4">',
    '<div class="flex items-end justify-between gap-1 sm:gap-2 h-48 mt-4">'
) 

# 2. Revert the Column layout to be simple (no h-full)
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group">',
    '<div class="flex-1 flex flex-col items-center gap-2 group">'
)
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group opacity-10">',
    '<div class="flex-1 flex flex-col items-center gap-2 group opacity-10">'
)
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group opacity-20">',
    '<div class="flex-1 flex flex-col items-center gap-2 group opacity-20">'
)
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group opacity-30">',
    '<div class="flex-1 flex flex-col items-center gap-2 group opacity-30">'
)

# 3. Inner Wrapper layout to strict h-36 (144px) so % heights compute correctly
content = content.replace(
    '<div class="w-full flex items-end justify-center gap-0.5 sm:gap-1 h-full min-h-[120px] relative">',
    '<div class="w-full flex items-end justify-center gap-0.5 sm:gap-1 h-36 relative">'
)

with open(file_dash, 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard-ceo.html chart layout mathematically fixed")
