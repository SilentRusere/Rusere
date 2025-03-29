
import streamlit as st

def calculate_concrete_materials(grade, quantity, waste):
    if grade == "Grade 10":
        sand = 0.49 * quantity * (1 + waste)
        cement = 4.6 * quantity * (1 + waste)
        stone = 0.77 * quantity * (1 + waste)
    elif grade == "Grade 15":
        sand = 0.47 * quantity * (1 + waste)
        cement = 5.8 * quantity * (1 + waste)
        stone = 0.77 * quantity * (1 + waste)
    elif grade == "Grade 20":
        sand = 0.44 * quantity * (1 + waste)
        cement = 6.6 * quantity * (1 + waste)
        stone = 0.77 * quantity * (1 + waste)
    elif grade == "Grade 25":
        sand = 0.42 * quantity * (1 + waste)
        cement = 7.6 * quantity * (1 + waste)
        stone = 0.77 * quantity * (1 + waste)
    else:
        return None
    return {
        "Building Sand (m³)": round(sand, 2),
        "Cement (50kg bags)": round(cement, 2),
        "19mm Stone (m³)": round(stone, 2)
    }

st.title("🧱 Construction Material Calculator")

grade = st.selectbox("Select Concrete Grade", ["Grade 10", "Grade 15", "Grade 20", "Grade 25"])
quantity = st.number_input("Enter Quantity (m³)", min_value=0.0, step=0.1)
waste = st.number_input("Waste %", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

if st.button("Calculate Materials"):
    results = calculate_concrete_materials(grade, quantity, waste)
    if results:
        st.success("Calculated Materials:")
        for material, value in results.items():
            st.write(f"**{material}:** {value}")
    else:
        st.error("Invalid grade selected.")
