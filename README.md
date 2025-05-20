This Streamlit app allows users to upload an image and click on any point to detect the nearest named color based on RGB values, using a local dataset (colors.csv). The app does not rely on OpenCV, making it lightweight and easy to use in web environments.

<!-- Replace with your screenshot if available -->

📌 Features
✅ Upload .jpg, .jpeg, or .png images

✅ Click on the image to detect color

✅ Displays RGB and HEX values of clicked pixel

✅ Matches to closest named color from dataset

✅ Shows a visual preview of detected color

✅ Built without OpenCV using only Streamlit, PIL, and NumPy

 How to Run
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/color-detection-app.git
cd color-detection-app
2. Install Dependencies
It's recommended to use a virtual environment.

bash
Copy
Edit
pip install -r requirements.txt
3. Add colors.csv
Make sure a file named colors.csv is present in the project directory. It should include these columns:

csv
Copy
Edit
color_name,R,G,B,hex
Red,255,0,0,#FF0000
Green,0,255,0,#00FF00
Blue,0,0,255,#0000FF
...
You can find sample datasets here.

4. Run the App
bash
Copy
Edit
streamlit run app.py

 File Structure
bash
Copy
Edit
.
├── app.py               # Main Streamlit application
├── colors.csv           # Dataset with color names and RGB values
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
📦 Requirements
streamlit

pandas

numpy

pillow

streamlit-image-coordinates

You can install them via:

bash
Copy
Edit
pip install streamlit pandas numpy pillow streamlit-image-coordinates
🧠 How It Works
Converts the uploaded image to RGB using PIL

Uses NumPy to extract pixel RGB from click coordinates

Calculates the closest color name using Euclidean distance

Displays the detected color with a preview box

📸 Credits
Color dataset inspiration: codebrainz/color-names

Image click detection: streamlit-image-coordinates

📜 License
This project is licensed under the MIT License.
