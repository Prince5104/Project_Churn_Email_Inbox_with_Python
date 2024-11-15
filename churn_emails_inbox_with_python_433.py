#!/usr/bin/env python
# coding: utf-8

# <font size=5>**Python Project - Churn Emails - Step 1 - Load the Dataset**</font>

# In[1]:


get_ipython().system('head -n15 /cxldata/datasets/project/mbox-short.txt')


# <font size=4>**Count the Number of Lines**</font>

# In[2]:


def number_of_lines():
    with open('/cxldata/datasets/project/mbox-short.txt') as f:
        data = f.read()
        lines = data.splitlines()
        return len(lines)
        
number_of_lines()        


# <font size=5>**Step 2 - Explore Content of Emails**</font>
# - <font size=4>**Count the Number of Subject Lines**</font>

# In[3]:


def count_number_of_lines():
    with open('/cxldata/datasets/project/mbox-short.txt') as f:
        count = 0
        for line in f:
            line = line.rstrip()
            if line.startswith('Subject:'):
                count += 1
    return count
            
count_number_of_lines()        


# <font size=4>**Find Average Spam Confidence**</font>

# In[4]:


def average_spam_confidence():
    with open ('/cxldata/datasets/project/mbox-short.txt') as f:
        count = 0
        total = 0
        for line in f:
            line = line.rstrip()
            if line.startswith('X-DSPAM-Confidence:'):
                var, value = line.split(':')
                total += float(value.strip())
                count += 1
#                 print("Total: ",total, "Value: ", value)
        return (total/count)

average_spam_confidence()


# <font size=4>**Find Which Day of the Week the Email was sent**</font>

# In[5]:


def find_email_sent_days():
    with open ('/cxldata/datasets/project/mbox-short.txt') as f:
        days_count = {}
        for line in f:
            line = line.rstrip()
            if line.startswith('From'):
                words = line.split()
                if len(words) > 2:
                    day = words[2]
                    days_count[day] = days_count.get(day, 0) + 1
    return days_count
    
find_email_sent_days()


# <font size=5>**Step 3 - Explore Header of Emails**</font>
# - <font size=4>**Count Number of Messages From Each Email Address**</font>

# In[6]:


def count_message_from_email():
    with open ('/cxldata/datasets/project/mbox-short.txt') as f:
        email_count = {}
        for line in f:
            line = line.rstrip()
            
            if line.startswith('From:'):
                words = line.split()
                email = words[1]
#                 print(f"Email Found: {email}")
                email_count[email] = email_count.get(email, 0) +1 
    return email_count

result = count_message_from_email()
print(result)


# <font size=4>**Count Number of Messages From Each Domain**</font>

# In[7]:


def count_message_from_domain():
    with open ('/cxldata/datasets/project/mbox-short.txt') as f:
        domain_count = {}
        for line in f:
            line = line.rstrip()
            if line.startswith('From:'):
                words = line.split()
                email = words[1]
                domain = email.split('@')[1]
                domain_count[domain] = domain_count.get(domain, 0) + 1
    return domain_count

result = count_message_from_domain()
print(result)


# <font size=5>**Author**</font>

# - **Prince Raj**
