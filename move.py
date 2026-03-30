import os

with open('E:/DrLoan/DoctorLoan_MVP/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

lb_start = idx_content.find('<!-- Premium Leaderboard Section -->')
lb_end = idx_content.find('<!-- Product List Header -->')
if lb_start != -1 and lb_end != -1:
    lb_content = idx_content[lb_start:lb_end].strip()
    idx_content = idx_content[:lb_start] + idx_content[lb_end:]
    
    ag_start = idx_content.find('<!-- Action Grid')
    idx_content = idx_content[:ag_start] + lb_content + '\n\n        ' + idx_content[ag_start:]
    
    # fix button
    idx_content = idx_content.replace('bg-primary/5 hover:bg-primary/10', 'bg-primary text-white shadow-md hover:opacity-90')
    idx_content = idx_content.replace('text-primary font-bold', 'font-bold')

with open('E:/DrLoan/DoctorLoan_MVP/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

with open('E:/DrLoan/DoctorLoan_MVP/profile.html', 'r', encoding='utf-8') as f:
    prof_content = f.read()

plb_start = prof_content.find('<!-- Leaderboard Widget -->')
plb_end = prof_content.find('<!-- Footer -->')
if plb_start != -1 and plb_end != -1:
    plb_content = prof_content[plb_start:plb_end].strip()
    prof_content = prof_content[:plb_start] + prof_content[plb_end:]
    
    plb_content = plb_content.replace('bg-primary/5', 'bg-primary text-white shadow-sm hover:opacity-90')
    plb_content = plb_content.replace('text-primary bg-primary/5', 'text-white bg-primary')
    
    mg_start = prof_content.find('<!-- Menu Grid -->')
    plb_wrapped = f'        <!-- Leaderboard Wrapper -->\n        <div class=\"max-w-4xl mx-auto px-6 mb-8 w-full\">\n            {plb_content}\n        </div>\n\n'
    prof_content = prof_content[:mg_start] + plb_wrapped + prof_content[mg_start:]

with open('E:/DrLoan/DoctorLoan_MVP/profile.html', 'w', encoding='utf-8') as f:
    f.write(prof_content)

print('Successfully moved and restyled leaderboards!')
