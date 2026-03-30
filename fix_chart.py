import os
import re

file_path = 'E:/DrLoan/DoctorLoan_MVP/dashboard-ceo.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the main container layout
content = content.replace(
    '<div class="flex items-end gap-2 h-36 mt-4">',
    '<div class="flex items-end justify-between gap-1 sm:gap-2 h-44 mt-4">'
)

# Replace the column layout
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-1">',
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group">'
)
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-1 opacity-30">',
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group opacity-30">'
)
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-1 opacity-20">',
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group opacity-20">'
)
content = content.replace(
    '<div class="flex-1 flex flex-col items-center gap-1 opacity-10">',
    '<div class="flex-1 flex flex-col items-center gap-2 h-full justify-end group opacity-10">'
)

# Replace the bar container layout
content = content.replace(
    '<div class="w-full flex items-end justify-center gap-1 h-32">',
    '<div class="w-full flex items-end justify-center gap-0.5 sm:gap-1 flex-1 relative">'
)

# Add group-hover effect to the 4.2B text for consistency
content = content.replace(
    '<span class="absolute -top-5 left-1/2 -translate-x-1/2 text-[9px] font-black text-primary whitespace-nowrap">4.2B</span>',
    '<span class="absolute -top-6 left-1/2 -translate-x-1/2 text-[10px] sm:text-xs font-black text-primary whitespace-nowrap drop-shadow-md pb-1">4.2B</span>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dashboard-ceo.html chart layout")
