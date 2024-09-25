🍽️ ConsumeWise - Gen AI Product Information 🤖
ConsumeWise is your AI-powered assistant for analyzing product information, visualizing state-wise consumption data 🗺️, and generating personalized product recommendations ✨. Using Groq API 🤖 (powered by LLaMA 🦙) for smart product descriptions, this app provides deep insights into consumer products with visually appealing data representations 📊.

🌟 Key Features 🌟
🧠 AI-Powered Product Descriptions: Harnesses the power of Groq API 🤖 to create detailed, custom descriptions of products based on your input.
📊 Custom Dataset for Product Insights: Analyzes items like almonds, apples, avocados, and more 🥑🍏, showing how they are consumed across various states with data from our handmade foodStates.csv dataset 📂.
📈 Visualizations: Offers beautiful pie charts 🥧 and bar graphs 📊 to showcase state-wise product consumption and compare different items.
📸 Image Display: Displays random images 📷 from a local dataset for selected products, helping you visualize the item alongside its description.
💬 Interactive Chatbot: Ask questions 🤔 and get AI-generated responses 🗣️ about product details using the Groq API.
🖥️ Streamlit Interface: Enjoy a user-friendly web interface 🌐 built with Streamlit for seamless data visualization, product analysis, and chatbot interaction.
⚙️ Technologies and Tools ⚙️
🧠 Pretrained AI Model: Utilizes Groq’s LLaMA-powered API 🦙 for generating product descriptions.
🌐 Streamlit: Provides an interactive, web-based user interface for easy navigation and functionality.
📊 Data Visualization: Built with Matplotlib to create dynamic pie charts and bar graphs.
📊 Pandas: For powerful data manipulation and analysis of the foodStates.csv dataset.
🖼️ PIL: Used for displaying random product images from local directories.
🔄 Random & OS Modules: For selecting random images and managing folder navigation.
🛠️ Features in Detail 🛠️
1️⃣ Single Product Information
Input a product name (e.g., "milk" 🥛) and get:

A random image 📸 of the product.
A detailed AI-generated description 🧠 using the Groq API.
A pie chart 🥧 showing state-wise consumption distribution 📊.
2️⃣ Compare Two Products
Compare two products (e.g., "milk" 🥛 vs "coffee" ☕). The app will:

Generate a bar chart 📊 comparing the state-wise distribution for both.
Provide AI-generated descriptions for both items 🤖.
3️⃣ Chatbot Integration
Chat with our friendly AI bot 💬 to ask questions about products and get quick, AI-generated answers! 🗣️

📥 Installation 📥
To set up ConsumeWise locally, follow these steps:

1️⃣ Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/ConsumeWise.git
cd ConsumeWise
2️⃣ Install dependencies:

bash
Copy code
pip install -r requirements.txt
3️⃣ Set up Groq API Key:

bash
Copy code
export GROQ_API_KEY="your_groq_api_key"
4️⃣ Run the app:

bash
Copy code
streamlit run app.py
🚀 Usage 🚀
Once the app is up and running, you can:

🔍 Enter a product name to get detailed descriptions, images, and visualizations 📊.
🔄 Compare two products to explore state-wise consumption patterns 🗺️.
💬 Chat with the AI to ask questions about products.
📊 Dataset 📊
The foodStates.csv dataset includes various products 🍏🥑🍿 like almonds, apples, and bananas, showing their consumption percentage across different states 🏙️.

🤝 Contributing 🤝
We welcome all contributions! You can:

Improve the data visualizations 📈.
Add new products or extend the dataset 📂.
Enhance the chatbot interactions 🧠.
Feel free to submit a pull request and join the ConsumeWise journey! 🚀✨
