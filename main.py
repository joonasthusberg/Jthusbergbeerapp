import streamlit as st

def main():
    st.title("JThusberg's Beer Drinkers' App")
    st.image("beer_bottle.png", caption="Beer Bottle", use_column_width=True)
    st.write("Welcome to the beer tracking app!")
    
    name = st.text_input("Enter your name:")
    beer_per_week = st.number_input("How many beers do you drink per week?", min_value=0)
    beer_per_day = st.number_input("How many beers do you drink per day?", min_value=0)
    
    if st.button("Submit"):
        st.write(f"Hello {name}!")
        total_beers = beer_per_week * 7 + beer_per_day
        if total_beers == 0:
            st.write("You're not drinking any beer. ¡Eres un santo!")
        elif total_beers < 10:
            st.write("Moderation is key! ¡Buen trabajo!")
        else:
            st.write("¡Eres un borracho!")

if __name__ == "__main__":
    main()
