import streamlit as st
import jyotishyamitra as jsm  # Assuming you have the jyotishyamitra library installed and accessible
import json

# Constants for Month Names (assuming these are defined in jyotishyamitra)
# If not, define them like this:
# class JyotishyaMitraConstants:  (Removed JyotishyaMitraConstants class since the project description asks to use jyotishyamitra.September kind of constants)
#    January = 1
#    February = 2
#    March = 3
#    April = 4
#    May = 5
#    June = 6
#    July = 7
#    August = 8
#    September = 9
#    October = 10
#    November = 11
#    December = 12
# jsm = JyotishyaMitraConstants()


def get_chart_data(birthdata, chart_type="D1"):
    """
    Generates astrological data and extracts the specified chart.

    Args:
        birthdata (dict): The validated birth data dictionary.
        chart_type (str): The chart type to extract (e.g., "D1" for Lagna, "D9" for Navamsa).

    Returns:
        dict or None: The chart data as a dictionary, or None if an error occurs.
    """
    astrodata = jsm.generate_astrologicalData(birthdata, returnval="ASTRODATA_DICTIONARY")

    if astrodata == "INPUT_ERROR":
        st.error("Input error: Please check your birth data.")
        return None
    elif astrodata == "OUTPUTPATH_ERROR":  # This shouldn't happen with ASTRODATA_DICTIONARY, but good to check
        st.error("Output path error (should not occur with dictionary output).")
        return None
    elif isinstance(astrodata, str) and astrodata.startswith("Invalid parameter"):
        st.error(f"Error in generate_astrologicalData: {astrodata}")
        return None
    elif astrodata is None:
        st.error("Error: generate_astrologicalData returned None.")
        return None

    if chart_type not in astrodata:
        st.error(f"Chart type '{chart_type}' not found in the generated data.")
        return None
   
    return astrodata[chart_type]


def display_chart_text(chart_data):
    """Displays chart data in a user-friendly text format."""

    if not chart_data:
        return  # Handle the case where chart_data is None

    st.subheader(f"{chart_data['name']} Chart ({chart_data['symbol']})")

    st.write(f"**Ascendant:** {chart_data['ascendant']}")  # Display Ascendant details

    st.write("**Planets:**")
    for planet, details in chart_data['planets'].items():
        st.write(f"  - **{planet}:**")
        st.write(f"    - Sign: {details['sign']}")
        st.write(f"    - House: {details['house']}")
        st.write(f"    - Nakshatra: {details['nakshatra']}")
        st.write(f"    - Nakshatra Lord: {details['nakshatra_lord']}")
        # Add other planet details as needed

    st.write("**Houses:**")
    for i, house_details in enumerate(chart_data['houses']):
        st.write(f"  - **House {i+1}:**")
        st.write(f"    - Sign: {house_details['sign']}")
        st.write(f"    - Lord: {house_details['lord']}")
        # Add other house details as needed

    #  Classifications (Optional, for more detailed text output)
    if 'classifications' in chart_data:
        st.write("**Classifications:**")
        for category, planets in chart_data['classifications'].items():
            st.write(f"  - {category}: {', '.join(planets)}")


def main():
    st.title("JyotishyaMitra Vedic Astrology Charts")

    # Input form
    with st.form("birthdata_form"):
        st.header("Birth Data")

        name = st.text_input("Name", "Shyam Bhat")
        gender = st.selectbox("Gender", ["male", "female", "others"])
        col1, col2, col3 = st.columns(3)
        year = col1.text_input("Year", "1991")
        month = col2.selectbox("Month", options=list(range(1, 13)), format_func=lambda x: {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}[x])  # Show month names
        day = col3.text_input("Day", "8")
        col1, col2, col3 = st.columns(3)
        hour = col1.text_input("Hour (24-hour format)", "14")
        minute = col2.text_input("Minute", "47")
        second = col3.text_input("Second", "9")

        place = st.text_input("Place of Birth", "Honavar")
        longitude = st.text_input("Longitude (e.g., +74.4439 for East, -74.4439 for West)", "+74.4439")
        latitude = st.text_input("Latitude (e.g., +14.2798 for North, -14.2798 for South)", "+14.2798")
        timezone = st.text_input("Timezone (GMT offset, e.g., +5.5 for IST, -4.0 for EST)", "+5.5")

        chart_type = st.selectbox("Select Chart", ["D1 (Lagna)", "D9 (Navamsa)"], index=0)  # Default to Lagna

        submitted = st.form_submit_button("Generate Chart")

    if submitted:
        # Clear previous data
        jsm.clear_birthdata()

        # Input data (using the dictionary approach for clarity and flexibility)
        inputdata = jsm.input_birthdata(
            name=name,
            gender=gender,
            year=year,
            month=str(month),  # Ensure month is a string
            day=day,
            hour=hour,
            min=minute,
            sec=second,
            place=place,
            longitude=longitude,
            lattitude=latitude,
            timezone=timezone
        )

        # Validate
        validation_result = jsm.validate_birthdata()
        if validation_result != "SUCCESS":
            st.error(f"Validation Error: {validation_result}")
            return  # Stop if validation fails

        if jsm.IsBirthdataValid():
            birthdata = jsm.get_birthdata()
            selected_chart = "D1" if chart_type == "D1 (Lagna)" else "D9"
            chart_data = get_chart_data(birthdata, selected_chart)

            if chart_data:
                # Display as Text
                st.header("Chart Data (Text Format)")
                display_chart_text(chart_data)

                # Display as JSON
                st.header("Chart Data (JSON Format)")
                st.json(chart_data)

        else:
            st.error("Birth data is not valid.")

if __name__ == "__main__":
    main()
