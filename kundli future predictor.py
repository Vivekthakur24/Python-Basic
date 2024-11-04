import tkinter as tk
from tkinter import scrolledtext
import ephem
from datetime import datetime
from geopy.geocoders import Nominatim

def get_lat_lon_from_place(place):
    geolocator = Nominatim(user_agent="kundli_predictor")
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError("Place not found")

def generate_planetary_positions(date_of_birth, time_of_birth, place_of_birth):
    # Get latitude and longitude from place of birth
    latitude, longitude = get_lat_lon_from_place(place_of_birth)

    # Combine date and time into a single datetime object
    date_time_str = f"{date_of_birth} {time_of_birth}"
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

    # Observer location
    observer = ephem.Observer()
    observer.lat, observer.lon = str(latitude), str(longitude)
    observer.date = date_time_obj

    # Calculate positions of planets
    planets = {
        "Sun": ephem.Sun(observer),
        "Moon": ephem.Moon(observer),
        "Mercury": ephem.Mercury(observer),
        "Venus": ephem.Venus(observer),
        "Mars": ephem.Mars(observer),
        "Jupiter": ephem.Jupiter(observer),
        "Saturn": ephem.Saturn(observer),
        "Uranus": ephem.Uranus(observer),
        "Neptune": ephem.Neptune(observer),
        "Pluto": ephem.Pluto(observer)
    }

    positions = {}
    for planet_name, planet in planets.items():
        positions[planet_name] = {
            "ra": planet.ra,  # Right Ascension
            "dec": planet.dec,  # Declination
            "az": planet.az,  # Azimuth
            "alt": planet.alt,  # Altitude
            "constellation": ephem.constellation(planet)  # Constellation
        }

    return positions

def generate_horoscope(positions):
    # Simple horoscope logic based on planetary positions
    sun_pos = positions["Sun"]["constellation"][1]  # Get the zodiac sign of the Sun

    horoscope = {
        "career": "Your career is bright and promising.",
        "love": "Love life is fulfilling, with new opportunities.",
        "health": "Focus on your health and well-being."
    }

    # Modify predictions based on Sun sign (as an example)
    if sun_pos == "Aries":
        horoscope["career"] = "A new opportunity may come your way."
        horoscope["love"] = "Be open to communication in relationships."
        horoscope["health"] = "A good time to start new health routines."
    elif sun_pos == "Taurus":
        horoscope["career"] = "Patience will bring success in your career."
        horoscope["love"] = "Cherish the stability in your relationships."
        horoscope["health"] = "Maintain a balanced diet for better health."
    elif sun_pos == "Gemini":
        horoscope["career"] = "Adaptability is your strength at work."
        horoscope["love"] = "Embrace change in your love life."
        horoscope["health"] = "Keep your mental health in check."
    elif sun_pos == "Cancer":
        horoscope["career"] = "Emotional intelligence will aid your career."
        horoscope["love"] = "Focus on nurturing your relationships."
        horoscope["health"] = "Take care of your emotional health."
    elif sun_pos == "Leo":
        horoscope["career"] = "Your leadership skills will be recognized."
        horoscope["love"] = "Expect excitement in your love life."
        horoscope["health"] = "Channel your energy into physical activities."
    elif sun_pos == "Virgo":
        horoscope["career"] = "Attention to detail will pay off at work."
        horoscope["love"] = "Analyze your relationships and communicate."
        horoscope["health"] = "Practice mindfulness to reduce stress."
    elif sun_pos == "Libra":
        horoscope["career"] = "Find balance between work and personal life."
        horoscope["love"] = "Enjoy social interactions and friendships."
        horoscope["health"] = "Maintain equilibrium in health routines."
    elif sun_pos == "Scorpio":
        horoscope["career"] = "Your intensity drives success in your career."
        horoscope["love"] = "Deepen emotional connections."
        horoscope["health"] = "Be mindful of stress levels."
    elif sun_pos == "Sagittarius":
        horoscope["career"] = "Explore new avenues in your career."
        horoscope["love"] = "Seek adventure in your love life."
        horoscope["health"] = "Engage in outdoor activities for fitness."
    elif sun_pos == "Capricorn":
        horoscope["career"] = "Hard work and discipline lead to achievements."
        horoscope["love"] = "Strengthen existing bonds."
        horoscope["health"] = "Take time to relax and unwind."
    elif sun_pos == "Aquarius":
        horoscope["career"] = "Innovative ideas will bring success."
        horoscope["love"] = "Embrace unconventional approaches to love."
        horoscope["health"] = "Focus on activities you enjoy for mental well-being."
    elif sun_pos == "Pisces":
        horoscope["career"] = "Trust your instincts in career decisions."
        horoscope["love"] = "Express your feelings freely in love."
        horoscope["health"] = "Nurture emotional and physical health."

    return horoscope

def display_results():
    date_of_birth = dob_entry.get()
    time_of_birth = tob_entry.get()
    place_of_birth = place_entry.get()

    try:
        positions = generate_planetary_positions(date_of_birth, time_of_birth, place_of_birth)
        horoscope = generate_horoscope(positions)

        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Planetary Positions:\n")
        for planet, details in positions.items():
            result_text.insert(tk.END, f"{planet}:\n")
            result_text.insert(tk.END, f"  Right Ascension: {details['ra']}\n")
            result_text.insert(tk.END, f"  Declination: {details['dec']}\n")
            result_text.insert(tk.END, f"  Azimuth: {details['az']}\n")
            result_text.insert(tk.END, f"  Altitude: {details['alt']}\n")
            result_text.insert(tk.END, f"  Constellation: {details['constellation']}\n\n")

        result_text.insert(tk.END, "Horoscope:\n")
        result_text.insert(tk.END, f"Career: {horoscope['career']}\n")
        result_text.insert(tk.END, f"Love: {horoscope['love']}\n")
        result_text.insert(tk.END, f"Health: {horoscope['health']}\n")
        result_text.config(state=tk.DISABLED)
    except Exception as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"An error occurred: {e}")
        result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Kundli Future Predictor")
root.configure(bg="light pink")  # Set the background color to light pink

# Labels and entries for user input
tk.Label(root, text="Date of Birth (YYYY-MM-DD):", bg="light pink").pack(padx=10, pady=5)
dob_entry = tk.Entry(root)
dob_entry.pack(padx=10, pady=5)

tk.Label(root, text="Time of Birth (HH:MM:SS):", bg="light pink").pack(padx=10, pady=5)
tob_entry = tk.Entry(root)
tob_entry.pack(padx=10, pady=5)

tk.Label(root, text="Place of Birth:", bg="light pink").pack(padx=10, pady=5)
place_entry = tk.Entry(root)
place_entry.pack(padx=10, pady=5)

# Button to generate planetary positions and horoscope
generate_button = tk.Button(root, text="Generate Horoscope", command=display_results, bg="red", fg="white")
generate_button.pack(padx=10, pady=10)

# Text widget to display results
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=30, width=60)
result_text.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
