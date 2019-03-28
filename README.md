

# Appr.tc made to work locally on uwp

To start the signaling server use the run.py python file.
Org.Webrtc reference must be added manually inside Visual Studio from the [webrtc-uwp-sdk](https://github.com/webrtc-uwp/webrtc-uwp-sdk) project that was built previously.  
Reference can be found in `webrtc-uwp-sdk\webrtc\windows\solutions\Build\Output\Org.WebRtc\[Release or Debug]\[x64 or x86]\Org.WebRtc.winmd`   

To try the sample between the two different devices in the same network insert your ip address into the `ipAddress` variable inside run.py file.  
You will also need to change the `roomServer` variable inside appwindow.js file accordingly
