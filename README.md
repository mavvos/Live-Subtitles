<div align="center">
  <h1>📹 Live-Subtitles 🔴</h1>
  <p text-align="justify">Live-Subtitles is a template made to help generate subtitles in livestream services.</p>
</div>

## 👨‍🏫 How to use
The person responsible for the live transmission opens up the Receiver page, chromakeys the green-box and adjusts it to fit their needs, then waits on the professional operating the Sender page.

The professional opens the Sender page and types their translation in the text area; every time the enter key is pressed, the current message is sent to the Receiver page, as well as showing up on the immediate feedback just above the type area.

## ⚙ How it works
Live-Subtitles was made using HTML, CSS, JavaScript, and Python modules:
- Flask;
- Flask_SocketIO for WebSockets;
- Jinja for web template.

## 🏃 How to run
To host locally:
- Make sure you have [Flask](https://pypi.org/project/Flask/) and [Flask_SocketIO](https://pypi.org/project/Flask-SocketIO/) installed
- Clone this repository
- On the cloned directory run the command ```flask run``` and open the address generated.

To host in a website:
- Check the official <a href="https://flask.palletsprojects.com/en/3.0.x/deploying/">Flask deploying instructions</a>.

## ℹ️ Information

This software uses the [MIT LICENSE](https://github.com/mavvos/Live-Subtitles/blob/main/LICENSE).

