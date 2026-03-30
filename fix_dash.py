import re

file_dash = 'E:/DrLoan/DoctorLoan_MVP/dashboard-ceo.html'
with open(file_dash, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the chart wrapper from flex-1 to h-full flex-1 w-full
content = content.replace(
    '<div class="w-full flex items-end justify-center gap-0.5 sm:gap-1 flex-1 relative">',
    '<div class="w-full flex items-end justify-center gap-0.5 sm:gap-1 h-full min-h-[120px] relative">'
)

with open(file_dash, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed dashboard inner heights")
