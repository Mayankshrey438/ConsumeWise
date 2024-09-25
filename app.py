import os
import random
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
from groq import Groq

# Set up API key
GROQ_API_KEY = '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'  # Replace with your Groq API key
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

# Initialize Groq client
client = Groq()

# Load the dataset
df = pd.read_csv('foodStates.csv')

# Normalize product names to lower case
product_names = [
    "almonds", "apples", "avocados", "bananas", "blacktea",
    "broccoli", "butter", "carrots", "cashews", "cauliflower",
    "cheese", "chickpeas", "coffee", "coke", "cornflakes",
    "cucumbers", "garlic", "grapes", "greentea", "icedtea",
    "kidneybeans", "mangoes", "milk", "oatmeal", "onion",
    "oranges", "pineapple", "popcorn", "potatochips", "potatoes",
    "rice", "soda", "spinach", "sprite"
]

# Function to display a random image from a folder
def show_random_image_from_folder(folder_path):
    """Shows a random image from the specified folder."""
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not image_files:
        st.write(f"No image files found in {folder_path}")
        return None

    random_image = random.choice(image_files)
    image_path = os.path.join(folder_path, random_image)

    try:
        img = Image.open(image_path)
        st.image(img, caption=random_image)
    except Exception as e:
        st.write(f"Error displaying image: {e}")

    return image_path

# Function to generate content using Groq API
def generate_content(prompt, max_tokens=100):
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt
        }],
        model="llama-3.1-8b-instant",
        max_tokens=max_tokens
    )
    return response

# Function to create pie chart for product's state distribution
def create_pie_chart(product_name):
    """Creates a pie chart of the state distribution for a given product."""
    product_data = df[df['ProductName'].str.lower() == product_name.lower()]

    if product_data.empty:
        st.write(f"No data found for product: {product_name}")
        return
    
    state_distribution = {}
    
    for index, row in product_data.iterrows():
        for i in range(1, 5):
            state_column = f"State{i}"
            percentage_column = f"Percentage{i}"
            state = row[state_column]
            percentage = row[percentage_column]
            if state in state_distribution:
                state_distribution[state] += float(percentage[:-1]) / 100
            else:
                state_distribution[state] = float(percentage[:-1]) / 100

    labels = list(state_distribution.keys())
    sizes = list(state_distribution.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title(f"State Distribution for {product_name}")

    st.pyplot(fig)

# Function to create bar chart for product comparison
def create_bar_chart(product_names):
    """Creates a bar chart comparing the state distribution of two products."""
    state_distributions = {}

    for product_name in product_names:
        product_data = df[df['ProductName'].str.lower() == product_name.lower()]

        if product_data.empty:
            st.write(f"No data found for product: {product_name}")
            return

        for index, row in product_data.iterrows():
            for i in range(1, 5):
                state_column = f"State{i}"
                percentage_column = f"Percentage{i}"
                state = row[state_column]
                percentage = row[percentage_column]
                if state in state_distributions:
                    state_distributions[state][product_name] = state_distributions[state].get(product_name, 0) + float(percentage[:-1]) / 100
                else:
                    state_distributions[state] = {product_name: float(percentage[:-1]) / 100}

    # Prepare data for plotting
    states = list(state_distributions.keys())
    product1_values = [state_distributions[state].get(product_names[0].lower(), 0) for state in states]
    product2_values = [state_distributions[state].get(product_names[1].lower(), 0) for state in states]

    # Plot the bar chart
    width = 0.35  # Bar width
    x = range(len(states))
    plt.bar(x, product1_values, width, label=product_names[0])
    plt.bar([p + width for p in x], product2_values, width, label=product_names[1])

    plt.xlabel("States")
    plt.ylabel("Percentage")
    plt.title(f"State Distribution Comparison: {product_names[0]} vs {product_names[1]}")
    plt.xticks([p + width / 2 for p in x], states, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    st.pyplot(plt.gcf())

    # Generate descriptions for both products
    description_prompt1 = f"Generate a detailed description for {product_names[0]}."
    description_prompt2 = f"Generate a detailed description for {product_names[1]}."
    
    description1 = generate_content(description_prompt1, max_tokens=1500)
    description2 = generate_content(description_prompt2, max_tokens=1500)
    
    # Display descriptions
    if description1 and description1.choices and description1.choices[0].message and description1.choices[0].message.content:
        st.write(f"**Description for {product_names[0]}:** {description1.choices[0].message.content}")
    
    if description2 and description2.choices and description2.choices[0].message and description2.choices[0].message.content:
        st.write(f"**Description for {product_names[1]}:** {description2.choices[0].message.content}")

# Chatbot functionality
def chat_with_bot():
    st.subheader("Chat with the Bot")

    # Initialize chat history in session state if not already done
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You: ", "")

    # Handle the chat interaction
    if st.button("Send"):
        if user_input:
            # Generate response from the chatbot
            response = generate_content(user_input, max_tokens=150)
            if response and response.choices and response.choices[0].message and response.choices[0].message.content:
                # Store user input and bot response in chat history
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("Bot", response.choices[0].message.content))
            else:
                st.write("Sorry, I didn't understand that.")

            # Display chat history
            for speaker, message in st.session_state.chat_history:
                st.write(f"**{speaker}:** {message}")

    # Display the End Chat button
    if st.button("End Chat"):
        st.session_state.chat_history = []  # Clear chat history
        st.experimental_rerun()  # Restart the chatbot

# Streamlit UI for user input
def show_product_info(folder_path):
    st.subheader("Select Product Option")
    option = st.radio("Do you want to:", ("View a single product", "Compare two products"))

    if option == "View a single product":
        product_name = st.text_input("Enter the product name (e.g., Milk):")

        if product_name:
            normalized_product_name = product_name.lower()  # Normalize user input

            food_folder_path = os.path.join(folder_path, normalized_product_name)

            if os.path.exists(food_folder_path):
                image_path = show_random_image_from_folder(food_folder_path)
                if image_path:
                    prompt = f"Generate a detailed description for {product_name}. Provide more in-depth information."
                    output = generate_content(prompt, max_tokens=1500)
                    if output and output.choices and output.choices[0].message and output.choices[0].message.content:
                        st.write(f"Description: {output.choices[0].message.content}")

                    create_pie_chart(normalized_product_name)  # Use normalized name
            else:
                st.write(f"Folder not found for {product_name}.")

    elif option == "Compare two products":
        product1 = st.text_input("Enter the name of the first product:")
        product2 = st.text_input("Enter the name of the second product:")

        if product1 and product2:
            normalized_product_names = [product1.lower(), product2.lower()]  # Normalize user input
            create_bar_chart(normalized_product_names)

# Main function to run the app
def main():
    st.title("ConsumeWise - Gen AI Product Information")

    folder_path = 'food_dataset\FoodDataset - Copy'  # Update this with your main directory path

    show_product_info(folder_path)
    chat_with_bot()

if __name__ == "__main__":
    main()
