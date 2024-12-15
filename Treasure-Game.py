import streamlit as st

st.title("🪙 TREASURE GUESS GAME 🪙")
st.write("Ahoy, matey! You are a pirate on a quest to find the hidden treasure. ⚓️")

# Choose an entrance
entrance = st.selectbox(
    "You are standing in front of a cave. The cave has two entrances. Which entrance do you want to choose?", 
    options=["Choose...", "left", "right"]
)

if entrance != "Choose...":
    if entrance == "left":
        lake_option = st.selectbox(
            "Now you are in front of a mysterious lake. You have 2 options...", 
            options=["Choose...", "Wait for a boat", "Swim into the lake"]
        )
        if lake_option != "Choose...":
            if lake_option == "Wait for a boat":
                st.write("🚣 You waited patiently for a boat and safely crossed the lake. Well done!")
                final_choice = st.selectbox(
                    "Final step! You see two houses in front of you. Which one will you choose?",
                    options=["Choose...", "Red", "Green"]
                )
                if final_choice != "Choose...":
                    if final_choice == "Red":
                        st.balloons()
                        st.snow()
                        st.write("🏠 Hooray! You found the treasure in the Red house! 🏆")
                    elif final_choice!="Red":
                        st.write("🏠 Oh no! The Green house is empty. Better luck next time, pirate.")
            else:
                st.write("🌊 Oh dear! The lake's current was too strong, and you couldn't make it across. Game Over!")

    elif entrance == "right":
        forest_option = st.selectbox(
            "Now you are in front of a dark and eerie forest. You have 2 options...", 
            options=["Choose...", "Enter the forest", "Walk along the forest edge"]
        )
        if forest_option != "Choose...":
            if forest_option == "Enter the forest":
                st.write("🌲 You bravely ventured into the forest and found a hidden path leading to the treasure!")
                final_choice = st.selectbox(
                    "Final step! You see three houses in front of you. Which one will you choose?",
                    options=["Choose...", "Red", "Yellow", "Green"]
                )
                if final_choice != "Choose...":
                    if final_choice == "Green":
                        st.balloons()
                        st.snow()
                        st.write("🏠 Congratulations! You found the treasure in the Green house! 🎉")
                    elif final_choice!="Green":
                        st.write(f"🏠 Oh no! The {final_choice} house is empty. Better luck next time, pirate.")
            else:
                st.write("🚶 You walked along the forest edge but got hopelessly lost. Game Over!")
