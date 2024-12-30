# 👁️‍🗨️ AuraCam: Turn Your PC into a 👀 iSpy Camera! 💻

Want to monitor your computer from anywhere? 🤔 Need to record screen activity?  Or just want to add extra security to your setup?🔒 AuraCam is the FREE and open-source solution you've been waiting for! ✨

AuraCam seamlessly integrates your PC with the popular iSpy CCTV application. By transforming your desktop into a live JPEG camera feed, AuraCam opens up a world of possibilities:



## Key Features:
- Live Desktop Streaming: Witness your computer's desktop in real-time directly within iSpy! 🎥
- Customizable Settings: Fine-tune output quality, refresh rate, and image saving location to match your needs. ⚙️
- User-Friendly Interface: Control AuraCam effortlessly with intuitive hotkeys for starting and stopping the camera feed. 🚀


## ✨ Use Cases: ✨
- Remote Monitoring: Keep a watchful eye on your computer from anywhere using iSpy's remote viewing capabilities. 🌎
- Screen Recording: Capture valuable desktop activity or create engaging visual demonstrations effortlessly. 🎬
- Security Enhancement: Utilize your existing PC hardware as a dedicated surveillance camera for added security measures. 💪


### 🚀 Get Started Today! 🚀
Download AuraCam and unlock the full potential of your PC as an iSpy camera. Experience the flexibility and convenience of remote monitoring and desktop visualization with this powerful software tool!

![image](https://github.com/user-attachments/assets/2d3cf859-67cb-4b84-bdc6-807c20a79b70)


# 💡 How to Use: 💡
1. Download AuraCam code (auracam.py) and ensure Python is installed on your system.
2. Run the following in the terminal:
```
pip install colorama, pillow, pyautogui
```
3. Create a shared folder on the iSpy server and then confirm you can access the folder from the client side. 📁
4. Open auracam.py **IN NOTEPAD**.
5. Replace `server` with the iSpy PCs hostname or IP address and `PCcam` with the shared name created in step 3.
```python
save_location = r'\\server\PCcam\capture.jpg'
```

6. Run AuraCam: Execute Python file (python auracam.py) from your terminal or command prompt.

# 🎥 iSpy Setup 🎥

1. Add new device > Other Video Source
2. With the settings for the new camera open, change the source type to Image.
3. In the URL/ Path field, input the LOCAL address to the shared folder.
```
D:\SHARED\PCcam\capture.jpg
```


### Optional Settings
Configure Settings: Modify settings at the top of the code:<br/>
output_quality : Adjust captured image quality (1-100). 🌟<br/>
refresh_rate : Set time interval between image captures (in seconds). ⏱️<br/>




### 🛠️ Troubleshooting: 🛠️<br/>
Network Path Issues: Double-check save_location and ensure it's correct and accessible to iSpy.<br/>
Hotkey Conflicts: Check for potential conflicts with other applications.<br/>
Image Quality: Experiment with output_quality to find the ideal balance between file size and detail.<br/>
