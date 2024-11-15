# Importing Streamlit
import streamlit as st
import pandas as pd
import numpy as np

# Title and Subheader
st.title("Happy birthday My good friend")
st.subheader("A riddle What is your name your stage name ofcourse Starts with an {R}")

if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = ""
# Input widgets
name = st.text_input("Enter your name:",key="name")
if st.session_state.name =="":
    
    
    st.session_state.age = st.slider("Select your age:", 1, 100, 12)




@st.fragment(run_every=10)
def release_the_balloons():
    st.balloons()



# Checkbox interaction
if st.session_state.name == "Rihanna" or st.session_state.age==20:
    release_the_balloons()
    st.write("""# Happy birthdayyyy Debooooo! 🎉  

Thank you soooo soooooo much for being such a wonderful friend to meee. This isn’t going to be super duper longggg because, well, that’s too predictable, and I hope you won’t think this is tooooo cringe. But I just have to say **THANK YOU** for showing me what real friendship looks like. I knowwww it hasn’t always been easy being my friend, but somehow you’ve stuck with me through all the ups and downs, and I can’t tell you how much that means to meeee. 💖  

> Because your favorite part of the bible is proverbs I may have tried to study a bit and look what I found 😁😁  **“A friend loves at all times, and a brother is born for a time of adversity.” – Proverbs 17:17**  

I just want you to know You’ve been that kind of friend, Debo. God bless youuu for that.  

I pray that in this new year of your life, God will strengthen you in every way possible. His love will wrap around you like a warm hug, and His mercy will keep flowing in your life in ways you can’t even imagine.  

> **“For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.” – Jeremiah 29:11**  

You’ll do amaaazzzziiiiinggg things, Debo! I just KNOW it. And I can’t wait to cheer you on as you make those dreams of yours come true. 🙌  

### Here’s a little prayer for you:  
*Lord, I thank You for Debo and for the blessing of her life. I pray You will guide her steps in this new age, shower her with Your grace, and grant her peace that surpasses all understanding. Strengthen her, Lord, and let Your favor be upon her in everything she does. Amen.*  

Have the **best day everrrrrrrr**, Debo! 🎂🎉 You deserve every bit of happiness and more!
""")



