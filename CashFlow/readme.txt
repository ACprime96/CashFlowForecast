Important steps to follow for Setup:

Step-1
    Setup echo with WiFi

Step-2
    download project from gitHub
    either download zip or git clone from https://github.com/ACprime96/CashFlowForecast.git

Step-3
    change directory to CashFlow in cmd
    run the command
    pip install -r requirements.txt

Step-4
    run the flask server on local
    python SimpleTest.py

Step-5
    For setting up serveo
    run the command
    ssh -o ServerAliveInterval=60  -R cashflow123:80:127.0.0.1:5000 serveo.net

Important steps for running the code:
Use Input.csv file present in input folder

When making changes to this folder please note to enter cash inflow and outflow for all Firms
Also keep the cash inflow range between 10K to 30K
The loan amount range must be in between 1K to 10K
Always make sure outflow is less than 10K
This ensures effective output

If the ranges are changed by default most of the Firms will endup in negative cashflow

All the outputs are seen in output directory

For Alexa Commands:
- [ ] For bank
Launch bank assistant
Get me the bank cashflow

- [ ] For Firm
Firm{Alpha,Beta,Gamma,Delta} details
Get me the firm forecast
Then tell name
