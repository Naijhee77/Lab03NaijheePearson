import streamlit as st
import requests
import datetime

#Page Title
st.title("Your Horoscope & Compatability")
st.image("https://cdn.britannica.com/45/104045-050-116C1F93/Signs-of-the-Zodiac-astrology.jpg", width = 700)

st.write("---") 
def getHoroscope(sign):
    url = "https://horoscope-astrology.p.rapidapi.com/sign"
    querystring = {"s":sign}
    headers = {
	"X-RapidAPI-Key": "35d4722060mshe044b6593be1dffp126b49jsn91171cd12d0d",
	"X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
    response = requests.get(url, headers=headers, params=querystring)
    info = response.json()
    if info["element"] == "Fire": 
        st.header(sign[0].upper() + sign[1:] + " " + "~ " + info["element"] +  " Sign " + ":fire:"  )
    elif info["element"] == "Water":
        st.header(sign[0].upper() + sign[1:] + " " + "~ " + info["element"] + " Sign " +":ocean:"  )
    elif info["element"] == "Air":
        st.header(sign[0].upper() + sign[1:] + " " + "~ " + info["element"] + " Sign " +":dash:"  )
    else:
         st.header(sign[0].upper() + sign[1:] + " " + "~ " + info["element"] + " Sign " + ":earth_americas:" )
    st.write(info["about"])
    st.image(image)
    st.write("---") 
    
#Birthday Picker ##NEW##
min_date = datetime.date(1950, 1, 1)
##NEW##
d = st.date_input("When is your birthday?", value="today", min_value=min_date, format="MM/DD/YYYY", label_visibility="visible")
birthday = (int(d.month),int(d.day))
if (birthday[0]==1 and birthday[1]>=20)or(birthday[0]==2 and birthday[1]<=18):
    sign = "aquarius"
    image = "https://cdn.britannica.com/66/5766-004-A409E7EF/Aquarius-book-Italian-New-York-City-Pierpont.jpg?w=300"
elif (birthday[0]==2 and birthday[1]>=19)or(birthday[0]==3 and birthday[1]<=20):
    sign = "pisces"
    image = "https://cdn.britannica.com/28/9628-050-B60BEF86/Pisces-illumination-Book-of-Hours-Italian-Pierpont.jpg?w=300"
elif (birthday[0]==3 and birthday[1]>=21)or(birthday[0]==4 and birthday[1]<=19):
    sign = "aries"
    image = "https://cdn.britannica.com/84/13384-004-ECCA3832/Aries-illumination-Book-of-Hours-Italian-Pierpont.jpg?w=300"
elif (birthday[0]==4 and birthday[1]>=20)or(birthday[0]==5 and birthday[1]<=20):
    sign = "taurus"
    image = "https://cdn.britannica.com/96/4596-004-1E0712A4/Taurus-Book-of-Hours-Italian-Pierpont-Morgan.jpg?w=300"
elif (birthday[0]==5 and birthday[1]>=21)or(birthday[0]==6 and birthday[1]<=20):
    sign = "gemini"
    image = "https://www.almanac.com/sites/default/files/styles/or/public/image_nodes/gemini.jpg?itok=KA7BPvR-"
elif (birthday[0]==6 and birthday[1]>=21)or(birthday[0]==7 and birthday[1]<=22):
    sign = "cancer"
    image = "https://cdn.britannica.com/21/44021-004-87FE1376/Cancer-illumination-book-Italian-New-York-City.jpg?w=300"
elif (birthday[0]==7 and birthday[1]>=23)or(birthday[0]==8 and birthday[1]<=22):
    sign = "leo"
    image = "https://cdn.britannica.com/85/2085-004-0F0DDBB1/Leo-Book-of-Hours-Italian-Pierpont-Morgan.jpg?w=300"
elif (birthday[0]==8 and birthday[1]>=23)or(birthday[0]==9 and birthday[1]<=22):
    sign = "virgo"
    image = "https://cdn.britannica.com/34/41734-050-37587D55/Virgo-book-Italian-New-York-City-Pierpont.jpg?w=300"
elif (birthday[0]==9 and birthday[1]>=23)or(birthday[0]==10 and birthday[1]<=22):
    sign = "libra"
    image = "https://cdn.britannica.com/58/10258-004-54EE416A/Libra-Book-of-Hours-Italian-Pierpont-Morgan.jpg?w=300"
elif (birthday[0]==10 and birthday[1]>=23)or(birthday[0]==11 and birthday[1]<=21):
    sign = "scorpio"
    image = "https://cdn.britannica.com/49/9449-004-5388AC68/Scorpius-Book-of-Hours-Italian-Pierpont-Morgan.jpg?w=300"
elif (birthday[0]==11 and birthday[1]>=22)or(birthday[0]==12 and birthday[1]<=21):
    sign = "sagittarius"
    image = "https://cdn.britannica.com/51/9551-004-3DD87324/Sagittarius-Book-of-Hours-Italian-Pierpont-Morgan.jpg?w=300"
elif (birthday[0]==12 and birthday[1]>=22)or(birthday[0]==1 and birthday[1]<=19):
    sign = "capricorn"
    image= "https://cdn.britannica.com/74/44074-004-485D1511/Capricornus-book-Italian-New-York-City-Pierpont.jpg?w=300"
getHoroscope(sign)

#Daily Horoscope ##NEW##
st.header("Strengths & Weaknesses")
def strengthsVWeak():
    url = "https://horoscope-astrology.p.rapidapi.com/sign"
    querystring = {"s":sign}
    headers = {
	"X-RapidAPI-Key": "35d4722060mshe044b6593be1dffp126b49jsn91171cd12d0d",
	"X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
    response4 = requests.get(url, headers=headers, params=querystring)
    info4 = response4.json()
    if not on:
        st.subheader("{}'s Strengths".format(sign[0].upper()+sign[1:]))
        st.write(info4["strengths"])
    else:
        st.subheader("{}'s Weaknesses".format(sign[0].upper()+sign[1:]))
        st.write(info4["weaknesses"])
##NEW##
on = st.toggle("Toggle between your strengths and weaknesses", value=False, key=None, help=None, on_change=None , args=None, kwargs=None, disabled=False, label_visibility="visible")
strengthsVWeak()
st.write("---")

#Daily Horoscope ##NEW##
userName= st.text_input("What's Your Name?", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Type Your Name Here...", disabled=False, label_visibility="visible")
def getDailyHoroscope(sign):
    if userName == "":
        st.header("Your Horoscope for Today is...")
    else:
        st.header("{}your Horoscope for Today is...".format(userName[0].upper()+userName[1:]+", "))
    url = "https://horoscope-astrology.p.rapidapi.com/horoscope"
    querystring = {"day":"today","sunsign":sign}
    headers = {
            "X-RapidAPI-Key": "35d4722060mshe044b6593be1dffp126b49jsn91171cd12d0d",
            "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
            }
    response2 = requests.get(url, headers=headers, params=querystring)
    info2 = response2.json()
    st.write(info2["horoscope"])
getDailyHoroscope(sign)
st.camera_input("Savor todays' horoscope with a picture!")
st.write("---")

#Compatability Finder ##NEW##
st.header("Compatability Finder")
##NEW##
yourSign = st.selectbox("What is your sign?",["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"] , index=0, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
pSign = st.selectbox("What is your partner's sign?",["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"] , index=0,key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")

def compatbility(yourSign, pSign):
    url = "https://horoscope-astrology.p.rapidapi.com/affinity"
    querystring = {"sign1":yourSign.lower(),"sign2":pSign.lower()}
    headers = {
	"X-RapidAPI-Key": "35d4722060mshe044b6593be1dffp126b49jsn91171cd12d0d",
	"X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
    response3 = requests.get(url, headers=headers, params=querystring)
    info3 = response3.json()
    st.write(info3[0]["header"])
    st.write(info3[0]["text"])
compatbility(yourSign, pSign)
st.write("---")
    
#Minimum Ratings ##NEW##
minRating = st.slider("How accurately do you feel like your horoscopes represent you?",0,10,5)
if minRating >=7:
    st.write("See, the stars are real!")
elif minRating <= 3:
    st.write("Well I guess you're just special!")
else:
    st.write("Well, I hope this is the start to your Astrology journey!")


    

st.image("https://media3.giphy.com/media/lb5njh6zDXFauXpBtC/giphy.gif",width=250)
