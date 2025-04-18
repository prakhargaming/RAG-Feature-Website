# Data Visualization Web Development Project for VIDI Reseach Lab at UC Davis

This was a data visualization web development project that used a React, SocketIO, Flask/Python tech stack. This was a machine learning adjacent project as well. It was very informative in helping develop web development skills on a consistent deadline. Through development of this web app, I learned a lot of new skills:
-   Front end was developed using React, D3 for data visualization, and MUI
-	Communication is handled by Socket.io and JSON
-	Back end was developed using Flask, Python, PyTorch, NumPy, and OpenCV
-	Machine learning/Data Visualization aspect was visualizing the second to last layer of the ResNet-50 network with the use of forward hooks and TSNE analysis

To run this application, please follow these steps (please note, the data vizualization aspect will not work since the ML waterbirds dataset is not included in this repo):
1)  Clone the repo 
2)  `cd` into the repo and input these commands: 
    ```bash
        python3 -m venv env  
        source env/bin/activate  
        pip install -r requirements.txt
    ```
3) `cd` into the front end folder and run these commands: 
    ```bash
        npm i react-scripts
    ```
4) To run locally, split your terminal. Input these commands at the root of the application in the first terminal window: 
    ```bash  
        cd webSocket-App  
        source env/bin/activate  
        python3 server.py
    ```
5) In the second terminal window: 
    ```bash  
        cd webSocket-App/front-end  
        npm start
    ```

Here is a GIF of the web app working in action. \
![](/applicationDemo.gif)