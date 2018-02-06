
# coding: utf-8

# In[35]:

raw_sent = ''
with open('input.txt') as i:
    raw_sent = i.readlines()

print(raw_sent)


# In[37]:

out_sent = []
len_restricted = 25

for sent in raw_sent:
    sent = sent.replace('\n', '')
    for i in range(int(len(sent) / len_restricted) + 1):
        out_sent += ['X']
        
        if i == len(sent):
            out_sent += [sent[i * len_restricted : -1]]
        else:
            out_sent += [sent[i * len_restricted : (i + 1) * len_restricted]]
            
        out_sent += ['Y']

for sent in out_sent:
    print(sent)


# In[39]:

with open('output.txt', 'w') as w:
    for sent in out_sent:
        w.write(sent)
        w.write('\n')

print('Reply converted!')

