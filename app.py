import tkinter as tk
from tkinter import PhotoImage
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from tkinter import *
def graph():
    FILE_NAME = 'oil_price.txt'
    feature_list = []
    target_list = []

    # Read days as feature, and price as target from an input file
    with open(FILE_NAME, 'r') as f:
        for line in f.readlines():
            day, price = line.strip().split(' ')
            feature_list.append([int(day)])
            # Support only integer, so, multiply by 100
            target_list.append(int(float(price) * 100))

    # Create model
    linear = LinearRegression().fit(feature_list, target_list)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.0001).fit(feature_list, target_list)

    # Extend a number of days for forecasting the future 
    last_day = len(feature_list)
    for i in range(1, 366):
        feature_list.append([last_day + i])
        target_list.append(np.nan)


    # Convert back to float, so, divide every element by 100
    linear_pred = list(map(lambda x: float(x) / 100, linear.predict(feature_list)))
    svr_rbf_pred = list(map(lambda x: float(x) / 100, svr_rbf.predict(feature_list)))
    target = list(map(lambda x: float(x) / 100, target_list))

    # Display the prediction at 1 day, 30 days, and 365 days after the last available data
    print('==== Linear regression prediction ====')
    print(' - 1 day : ', linear_pred[last_day])
    print(' - 30 days : ', linear_pred[last_day + 29])
    print(' - 365 days : ', linear_pred[last_day + 364])

    print('==== Support vector regression  prediction ====')
    print(' - 1 day : ', svr_rbf_pred[last_day])
    print(' - 30 days : ', svr_rbf_pred[last_day + 29])
    print(' - 365 days : ', svr_rbf_pred[last_day + 364])

    # Plot data out
    # plt.hold('on')
    plt.plot(feature_list, target, color='black', label='Crude oil price')
    plt.plot(feature_list, linear_pred, color='blue', label='Linear Regressoin')
    plt.plot(feature_list, svr_rbf_pred, color='red', label='Support Vector Regression RBF')
    plt.xlabel('A number of days since Jan 1, 2021')
    plt.ylabel('Oil Price (USD)')
    plt.gca().set_xlim(left = 0)
    plt.gca().set_xlim(right = 1000)
    plt.gca().set_ylim(bottom = 0)
    plt.xticks(np.arange(0, 1001, 60))
    plt.legend()
    plt.show()









# Create a new window
window = tk.Tk()

# Set the window title
window.title("Crude Oil Price Prediction")
# bg = PhotoImage(file = "Cap1_TEM1391_20211013150248_theedgemarkets.webp")
window.configure(bg="#B0E0A8")
# Show image using label
# label1 = Label( window, image = bg)
# label1.place(x = 0, y = 0)
# Set the window size
window.geometry("2000x800")

# Create a label
label = tk.Label(text="Crude oil Price Prediction using SVR",bg="#B0E0A0", fg="green")
Font_tuple = ("Nexa", 20, "bold")
  

label.configure(font = Font_tuple)
label.pack()


# Create a button
button = tk.Button(text="Click me for Statistics",command=graph)
button.pack()


text_label = Label(window, text="",bg="#B0E0A5")
Font_tuple = ("Arial", 15, "bold")
text_label.configure(font = Font_tuple)
text_label.pack()
def price():
    FILE_NAME = 'oil_price.txt'
    feature_list = []
    target_list = []

    # Read days as feature, and price as target from an input file
    with open(FILE_NAME, 'r') as f:
        for line in f.readlines():
            day, price = line.strip().split(' ')
            feature_list.append([int(day)])
            # Support only integer, so, multiply by 100
            target_list.append(int(float(price) * 100))

    # Create model
    linear = LinearRegression().fit(feature_list, target_list)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.0001).fit(feature_list, target_list)

    # Extend a number of days for forecasting the future 
    last_day = len(feature_list)
    for i in range(1, 366):
        feature_list.append([last_day + i])
        target_list.append(np.nan)

    # Convert back to float, so, divide every element by 100
    linear_pred = list(map(lambda x: float(x) / 100, linear.predict(feature_list)))
    svr_rbf_pred = list(map(lambda x: float(x) / 100, svr_rbf.predict(feature_list)))
    target = list(map(lambda x: float(x) / 100, target_list))

    # Display the prediction at 1 day, 30 days, and 365 days after the last available data
    print('==== Linear regression prediction ====')
    print(' - 1 day : ', linear_pred[last_day])
    print(' - 30 days : ', linear_pred[last_day + 29])
    print(' - 365 days : ', linear_pred[last_day + 364])
    # text_label.config("kgkuyv")
    print('==== Support vector regression  prediction ====')
    print(' - 1 day : ', svr_rbf_pred[last_day])
    print(' - 30 days : ', svr_rbf_pred[last_day + 29])
    print(' - 365 days : ', svr_rbf_pred[last_day + 364])
    lines = "\nThe prediction at 1 day, 30 days, and 365 days after the last available data \n\n\n ==== Linear regression prediction ====\n"
    lines+=" - 1 day       :   "+str(linear_pred[last_day])
    lines+="\n- 30 days   : "+str(linear_pred[last_day+29])
    lines+="\n- 365 days : "+str(linear_pred[last_day+364])
    lines+="\n\n==== Support vector regression  prediction ===="
    lines+="\n- 1 day            :   "+str(svr_rbf_pred[last_day])
    lines+="\n- 30 days         :   "+str(svr_rbf_pred[last_day+29])
    lines+="\n- 365 days       :   "+str(svr_rbf_pred[last_day+364])
    text_label.config(text=lines)

button2 = tk.Button(text="Click me for Price",command=price)
button2.pack()


# Run the main event loop
window.mainloop()