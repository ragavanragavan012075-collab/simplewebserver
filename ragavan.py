from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <tittle> pc info</tittle>
     </head>

        <body>
            <h1 align="center">RAGAVAN-26019043</h1>
            <h2 align="center">my laptop configuration</h2>
            
            <table border="2" align="center">
                <tr>
                    <th>S.NO</th>
                    <th>device type</th>
                    <th>dive information</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>device name</td>
                    <td>TL15-53M-G2</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>processor</td>
                    <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>insralled RAM</td>
                    <td>16.0 GB (15.7 GB usable)</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>graphics card</td>
                    <td>Intel(R) Graphics (128 MB)</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>storage</td>
                    <td>278 GB of 477 GB used</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>device id</td>
                    <td>E60387A3-A777-4D65-8360-4EF957BC1304</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>product id</td>
                    <td>00342-42945-49068-AAOEM</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td>system type</td>
                    <td>64-bit operating system, x64-based processor</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td>pen and touch</td>       
                    <td>No pen or touch input is available for this display</td>         
                </tr>
                

            </table>
        </body>
    
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()