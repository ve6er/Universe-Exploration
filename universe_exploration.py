import streamlit as st
import pandas as pd
import numpy as np
import datetime
import math
from PIL import Image
import pickle
import webbrowser

st.markdown("<h1 style='text-align: center; font-family: Roboto;'>Explore the Universe</h1>", unsafe_allow_html=True)

st.image(Image.open("luminosity.jpg"))

cities=pd.read_csv("cities_coords.csv")

st.write('Select your city from the list below:')
search_query = st.text_input('Search for a city:', 'Mumbai')
filtered_cities = cities[cities['city_ascii'].str.contains(search_query, case=False)]
city_container = st.empty()
city = city_container.selectbox('Matching Cities:', filtered_cities['city_ascii'], index=0)
observer_longitude=cities[cities['city_ascii']==city]['lng'].values[0]

obj_RA=st.number_input("Enter the right ascension angle", min_value=0, max_value=9999, value="min")
u=st.number_input("Enter the readings of the Ultraviolet filter", min_value=0.0, max_value=9999.0, value=23.48)
g=st.number_input("Enter the readings of the  Green filter", min_value=0.0, max_value=9999.0, value=23.33776)
r=st.number_input("Enter the readings of the  Red filter", min_value=0.0, max_value=9999.0, value=21.32195)
i=st.number_input("Enter the readings of the  Near-Infrared filter", min_value=0.0, max_value=9999.0, value=20.25615)
z=st.number_input("Enter the readings of the  Infrared filter", min_value=0.0, max_value=9999.0, value=19.54544)
redshift=st.number_input("Enter the readings of the  Redshift", max_value=9999.0, value=1.424659, step=0.001)
listt=[u,g,r,i,z,redshift]
vk= np.array(listt).reshape(1, 6)
model=pickle.load(open(r"C:\Users\Veer Kukreja\Downloads\stellar_classifier.sav", "rb"))
def predict(v):
    if v==0:
        return "Galaxy"
    elif v==1:
        return "Quasi Stellar Object"
    else:
        return "Star"
object=predict(model.predict(vk))
galaxy = Image.open("Galaxy.jpg")
qso=Image.open("QSO.jpg")
star=Image.open("star.jpg")
telescope=Image.open("Title.jpg")

st.write("<div style='margin-bottom: 55px;'></div>", unsafe_allow_html=True)
if object=="Galaxy":
    st.image(galaxy)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>The object you are looking at is a Galaxy</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; color: white; font-size: 20px;'>Want to learn more about galaxies?</h1>", unsafe_allow_html=True)
    if st.button("Click Here"):
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Fun Facts about Galaxies!</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Our own galaxy, the Milky Way, is about 100,000 light-years in diameter.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Galaxies can merge and consume smaller galaxies. This process is called galactic cannibalism. Over time, it can lead to the formation of larger, more massive galaxies.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>There are estimated to be over 2 trillion galaxies in the observable universe, and each one can contain billions to trillions of stars.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>A significant portion of a galaxy's mass is believed to be composed of dark matter, an invisible and mysterious substance that doesn't emit or interact with light.</h1>", unsafe_allow_html=True)
elif object=="Quasi Stellar Object":
    st.image(qso)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>The object you are looking at is a Quasi Stellar Object</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; color: white; font-size: 20px;'>Want to learn more about Quasars?</h1>", unsafe_allow_html=True)
    if st.button("Click Here"):
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Fun Facts about Quasars!</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Quasars are some of the brightest objects in the universe, outshining entire galaxies. They can emit thousands of times more energy than the Milky Way.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Quasars are thought to be powered by supermassive black holes at their centers. The intense energy emission comes from the material falling into these black holes.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Quasars typically have high redshift values, indicating that they are receding from us at very high speeds due to the expansion of the universe.</h1>", unsafe_allow_html=True)
else:
    st.image(star)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>The object you are looking at is a Star</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; color: white; font-size: 20px;'>Want to learn more about Stars</h1>", unsafe_allow_html=True)
    if st.button("Click Here"):
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>Fun Facts about Stars!</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>The color of a star is an indication of its temperature. Blue and white stars are hotter, while red and orange stars are cooler.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>As stars age, they can expand into red giants, swelling to many times their original size.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px;'>When massive stars exhaust their nuclear fuel, they can explode in a spectacular event called a supernova, briefly outshining entire galaxies.</h1>", unsafe_allow_html=True)
    
st.write("<div style='margin-bottom: 55px;'></div>", unsafe_allow_html=True)


def calculate_local_transit_time(obj_RA, observer_longitude, ST_G):
    # Calculate the Hour Angle (HA) of the object
    HA = ST_G - math.radians(obj_RA)
    
    # Calculate the Local Transit Time (in sidereal hours)
    local_transit_sidereal_time = HA / (2 * math.pi) * 24
    
    # Convert Local Transit Time to Local Time
    observer_longitude_hours = observer_longitude / 15  # Convert longitude to hours
    local_transit_local_time = (local_transit_sidereal_time - observer_longitude_hours) % 24
    
    return local_transit_local_time

now = datetime.datetime.utcnow()
days_since_J2000 = (now - datetime.datetime(2000, 1, 1, 12, 0, 0)).days
ST_G = math.radians(280.46061837 + 360.98564736629 * days_since_J2000)  # Greenwich Sidereal Time in radians

# Example function to calculate visibility times
def calculate_visibility_times(obj_RA, obj_DEC, observer_latitude):
    # Constants for visibility criteria (e.g., altitude above the horizon)
    visibility_altitude_threshold = 20  # Example threshold in degrees


# Calculate Local Transit Time of the object in local time
#if obj_RA is not None and observer_longitude is not None:
local_transit_time = calculate_local_transit_time(obj_RA, observer_longitude, ST_G)
v=(local_transit_time%1)*60/100
local_transit_time=int(local_transit_time)+v
st.image(telescope)
st.markdown(f"<h1 style='text-align: center; color: white; font-size: 20px;'>The best time to observe the {object} is at: {local_transit_time:.2f} hours</h1>", unsafe_allow_html=True)
st.write("<div style='margin-bottom: 55px;'></div>", unsafe_allow_html=True)

def luminosity(r):
    # Cosmological parameters for the ΛCDM model
    speed_of_light=299792458
    hubble_constant=70
    omega_m = 0.3  # Matter density parameter
    omega_lambda = 0.7  # Dark energy density parameter

    # Calculate luminosity distance using the ΛCDM model formula
    luminosity_distance = (speed_of_light / hubble_constant) * r * \
                          (1 + r) / np.sqrt(omega_m * (1 + r) ** 3 + omega_lambda)
    return abs(luminosity_distance)  # Luminosity distance in parsecs
sci_notation="{:e}".format(luminosity(redshift))
st.image(lumin)
st.markdown(f"<h1 style='text-align: center; color: white; font-size: 20px;'>The luminosity of the object is {sci_notation} parsecs</h1>", unsafe_allow_html=True)

def calculate_velocity_from_redshift(redshift):
    speed_of_light = 299792458  # Speed of light in meters per second
    
    # Avoid division by zero
    if redshift == -1:
        return float('inf')
    
    # Calculate the velocity in meters per second
    velocity = speed_of_light * redshift
    return velocity
v_parker_probe=68600.0762
vel=calculate_velocity_from_redshift(redshift)
if vel>0:
    st.markdown(f"<h1 style='text-align: center; color: white; font-size: 20px;'>The {object} is moving away from us at a speed of {vel:.2f} m/s !!</h1>", unsafe_allow_html=True)
    if v_parker_probe<vel:
        st.markdown(f"<h1 style='text-align: center; color: white; font-size: 20px;'>That's {round(vel)} times faster than the fastest human made space ship !!</h1>", unsafe_allow_html=True)
else:
    st.markdown(f"<h1 style='text-align: center; color: white; font-size: 20px;'>The {object} is heading towards us at a speed of {-vel:.2f} m/s !!</h1>", unsafe_allow_html=True)
    if v_parker_probe<(-vel):
        st.markdown(f"<h1 style='text-align: center; color: white; font-size: 20px;'>That's {round(-vel/68600.0762)} times faster than the fastest human made space ship !!</h1>", unsafe_allow_html=True)
if abs(vel)>299792458:
    st.markdown(f"<h1 style='text-align: center; color: white; font-size: 20px;'>That's faster than the speed of light!!</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: left; color: white; font-size: 20px;'>Want to know how something can be moving away from us faster than the fastest thing in the Universe?</h1>", unsafe_allow_html=True)
    url = 'https://phys.org/news/2015-10-galaxies-faster.html'
    if st.button('Click Here', "primary"):
        webbrowser.open_new_tab(url)
