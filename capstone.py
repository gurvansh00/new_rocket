from rocketpy import *
import streamlit as st
import datetime
import matplotlib.pyplot as plt


tab1, tab2 = st.tabs(["Home", "Rocket Details"])
with tab1:
    st.title("Rocket Simulation")
    st.write("This is a rocket simulation aimed to ")

with tab2:
    #envi setup
    lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.01)
    long = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.01)
    eleva = st.number_input("Elevation", min_value = 0, step = 1)

    #envi print

    if st.button("Enter1"):
        env = Environment(latitude=lat, longitude=long, elevation=eleva)

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))  # Hour given in UTC time

        env.set_atmospheric_model(type="Forecast", file="GFS")

        #Display env output
        st.title("Environment details")
        st.write(env.all_info_returned())
        st.title("Plots")
        plot_data = env.all_plot_info_returned().get("wind_speed")
        st.line_chart(plot_data)

    #motor setup
    
    nozzle_radius = st.number_input("Nozzle Radius (Meters)")
    throat_radius = st.number_input("Throad Radius (Meters)")
    nozzle_pos = st.number_input("Nozzle Position (Meters from the back)")
    grain_out_rad = st.number_input("Grain Outer Radius (Meters)")
    grain_in_rad = st.number_input("Grain Inner Radius (Meters)")

    if st.button("Enter2"):

        motor = SolidMotor(
        thrust_source=r"C:\Users\rayan\Downloads\Python programs\Documents\RocketPy-master\data\motors\Cesaroni_M1670.eng",
        dry_mass=1.815,
        dry_inertia=(0.125, 0.125, 0.002),
        nozzle_radius=nozzle_radius,
        grain_number=5,
        grain_density=1815,
        grain_outer_radius=grain_out_rad,
        grain_initial_inner_radius=grain_in_rad,
        grain_initial_height=120 / 1000,
        grain_separation=5 / 1000,
        grains_center_of_mass_position=0.397,
        center_of_dry_mass_position=0.317,
        nozzle_position=0,
        burn_time=3.9,
        throat_radius=throat_radius,
        coordinate_system_orientation="nozzle_to_combustion_chamber",
        )
        
