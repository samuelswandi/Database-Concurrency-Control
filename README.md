
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Database Concurrency Control</h1>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
Implementing simple locking protocol, and OCC. Built with `Python`

<!-- GETTING STARTED -->
### Prerequisites

* python (https://www.python.org/downloads/)

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/samuelswandi/Database-Concurrency-Control
   ```
2. Change the case in case.txt with this format:
   ```
   W1X,R2X,W2Y,W1Y,W3X,R3Y,C1,C2,C3
   W,R = Command to write/read
   1,2,3 = Transactions
   X,Y,Z = Data
   ```

3. Run using python
   ```sh
   python3 main.py
   ```
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>